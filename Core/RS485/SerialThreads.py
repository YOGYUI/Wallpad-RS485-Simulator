import os
import sys
import time
import queue
import serial
import threading
import traceback
from abc import ABCMeta, abstractmethod
CURPATH = os.path.dirname(os.path.abspath(__file__))  # {PROJ}/Core/RS485
INCPATH = os.path.dirname(os.path.dirname(CURPATH))  # {PROJ}/Core
sys.path.extend([CURPATH, INCPATH])
sys.path = list(set(sys.path))
del CURPATH, INCPATH
from Common import GetLogger, Callback


class ThreadCommon(threading.Thread):
    __metaclass__ = ABCMeta
    _keepAlive: bool = True

    def __init__(self, serial_: serial.Serial, name_: str = "Serial Thread Common"):
        threading.Thread.__init__(self, name=name_)
        self._serial = serial_
        self.sig_terminated = Callback()
        self.sig_exception = Callback(str)
        self.setDaemon(True)
    
    def run(self):
        GetLogger().debug(f"Started ({self._serial.port})", self)
        while self._keepAlive:
            try:
                self._process()
            except Exception as e:
                GetLogger().error("Exception::{}".format(e), self)
                traceback.print_exc()
                self.sig_exception.emit(str(e))
        GetLogger().debug(f"Terminated ({self._serial.port})", self)
        self.sig_terminated.emit()

    def stop(self):
        self._keepAlive = False

    @abstractmethod
    def _process(self):
        pass


class ThreadSend(ThreadCommon):
    def __init__(self, serial_: serial.Serial, queue_: queue.Queue):
        super().__init__(serial_, "Serial Send Thread")
        self._queue = queue_
        self._toggle_rts: bool = False
        self.sig_send_data = Callback(bytes)
    
    def _process(self):
        if not self._queue.empty():
            data = self._queue.get()
            sendLen = len(data)
            if self._toggle_rts:
                self._serial.setRTS(True)
            while sendLen > 0:
                nLen = self._serial.write(data[(len(data) - sendLen):])
                sData = data[(len(data) - sendLen):(len(data) - sendLen + nLen)]
                self.sig_send_data.emit(sData)
                sendLen -= nLen
            if self._toggle_rts:
                self._serial.setRTS(False)
        else:
            time.sleep(1e-3)


class ThreadReceive(ThreadCommon):
    def __init__(self, serial_: serial.Serial, queue_: queue.Queue):
        super().__init__(serial_, "Serial Recv Thread")
        self._queue = queue_
        self.sig_recv_data = Callback()
    
    def _process(self):
        if self._serial.isOpen():
            if self._serial.in_waiting > 0:
                rcv = self._serial.read(self._serial.in_waiting)
                self.sig_recv_data.emit()
                self._queue.put(rcv)
            else:
                time.sleep(1e-3)
        else:
            time.sleep(1e-3)


class ThreadCheckRecvQueue(ThreadCommon):
    def __init__(self, serial_: serial.Serial, queue_: queue.Queue):
        super().__init__(serial_, "Serial Check Recv Thread")
        self._queue = queue_
        self.sig_get = Callback(bytes)
    
    def _process(self):
        if not self._queue.empty():
            chunk = self._queue.get()
            self.sig_get.emit(chunk)
        else:
            time.sleep(1e-3)

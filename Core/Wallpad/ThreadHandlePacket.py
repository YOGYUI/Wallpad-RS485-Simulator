import os
import sys
import time
import queue
import threading
import traceback
CURPATH = os.path.dirname(os.path.abspath(__file__))  # {PROJ}/Core/Wallpad
INCPATH = os.path.dirname(os.path.dirname(CURPATH))  # {PROJ}/Core
sys.path.extend([CURPATH, INCPATH])
sys.path = list(set(sys.path))
del CURPATH, INCPATH
from Common import GetLogger, Callback


class ThreadHandlePacket(threading.Thread):
    _keepAlive: bool = True

    def __init__(self, queue: queue.Queue = None):
        threading.Thread.__init__(self, name="Thread Send Packet (Wallpad)")
        self._queue = queue
        self._enable_periodic_query = True
        self._periodic_query_interval_ms = 100
        self.sig_terminated = Callback()
        self.sig_exception = Callback(str)
        self.setDaemon(True)
    
    def run(self):
        GetLogger().debug(f"Started", self)
        while self._keepAlive:
            try:
                self._process()
            except Exception as e:
                GetLogger().error("Exception::{}".format(e), self)
                traceback.print_exc()
                self.sig_exception.emit(str(e))
        GetLogger().debug(f"Terminated", self)
        self.sig_terminated.emit()

    def stop(self):
        self._keepAlive = False

    def _process(self):
        time.sleep(1e-3)

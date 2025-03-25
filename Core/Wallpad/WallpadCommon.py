import os
import sys
from typing import List, Union
CURPATH = os.path.dirname(os.path.abspath(__file__))
COREPATH = os.path.dirname(CURPATH)
sys.path.extend([CURPATH, COREPATH])
sys.path = list(set(sys.path))
from Common import GetLogger, WallpadVendor
from Device import *
from RS485 import SerialComm
from Config import Config
from ThreadHandlePacket import ThreadHandlePacket


class Wallpad(object):
    _threadHandlePacket: Union[ThreadHandlePacket, None] = None

    def __init__(self, config: Config):
        self._device_list: List[DeviceCommon] = list()
        self._serial_list: List[SerialComm] = list()
        self._vendor: WallpadVendor = WallpadVendor.UNSPECIFIED
        self._config: Config = config
        GetLogger().info("Created", self)

    def initialize(self):
        self._device_list.clear()
        for cfg in self._config.device_config_list:
            dev = createDeviceInstance(cfg.dev_type, cfg.name, cfg.index, cfg.room_index, cfg.rs485_index)
            self._device_list.append(dev)
        self._serial_list.clear()
        for cfg in self._config.rs485_config_list:
            ser = SerialComm(cfg.port, cfg.name, cfg.baudrate, cfg.bytesize, cfg.parity, cfg.stopbits)
            if ser.connect():
                self._serial_list.append(ser)
            else:
                self._handleException(f"Failed to connect serial (port: {cfg.port})")
        self.setVendor(WallpadVendor(self._config.wallpad_vendor))
        self._startThreadHandlePacket()
        GetLogger().info("Initialized", self)

    def release(self):
        self._stopThreadHandlePacket()
        for ser in self._serial_list:
            ser.disconnect()
        GetLogger().info("Released", self)

    def _startThreadHandlePacket(self):
        if self._threadHandlePacket is None:
            self._threadHandlePacket = ThreadHandlePacket()
            self._threadHandlePacket.sig_exception.connect(self._handleException)
            self._threadHandlePacket.sig_terminated.connect(self._onThreadHandlePacketTerminated)
            self._threadHandlePacket.start()

    def _stopThreadHandlePacket(self):
        if self._threadHandlePacket is not None:
            self._threadHandlePacket.stop()
    
    def _onThreadHandlePacketTerminated(self):
        del self._threadHandlePacket
        self._threadHandlePacket = None

    def _handleException(self, obj: object):
        GetLogger().error(f"{obj}", self)

    def setVendor(self, vendor: Union[int, WallpadVendor]):
        if isinstance(vendor, int):
            try:
                vendor = WallpadVendor(vendor)
            except Exception:
                vendor = WallpadVendor.UNSPECIFIED
        self._vendor = vendor
        # TODO: vendor 설정 후 packet generator, packet parser 인스턴스 새로 생성 필요

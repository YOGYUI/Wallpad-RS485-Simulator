import os
import sys
from abc import ABCMeta, abstractmethod
CURPATH = os.path.dirname(os.path.abspath(__file__))
COREPATH = os.path.dirname(CURPATH)
sys.path.extend([CURPATH, COREPATH])
sys.path = list(set(sys.path))
from Common import DeviceType


class DeviceCommon(object):
    __metaclass__ = ABCMeta

    def __init__(self, dev_type: DeviceType, name: str, index: int, room_index: int, rs485_index: int):
        self._dev_type = dev_type
        self._name = name
        self._index = index
        self._room_index = room_index
        self._rs485_index = rs485_index

    @abstractmethod
    def getQueryPacket(self, params: dict) -> bytearray:
        pass

    @abstractmethod
    def getCommandPacket(self, params: dict) -> bytearray:
        pass

    @abstractmethod
    def getResponsePacket(self, params: dict) -> bytearray:
        pass

    @abstractmethod
    def handleCommand(self, params: dict):
        pass

    @property
    def devType(self) -> DeviceType:
        return self._dev_type

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def index(self) -> int:
        return self._index
    
    @property
    def room_index(self) -> int:
        return self._room_index

    @property
    def rs485_index(self) -> int:
        return self._rs485_index

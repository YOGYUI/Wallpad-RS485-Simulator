import os
import sys
from abc import ABCMeta, abstractmethod
CURPATH = os.path.dirname(os.path.abspath(__file__))  # {PROJ}/Core/Packet/Parser
COREPATH = os.path.dirname(os.path.dirname(CURPATH))
sys.path.extend([CURPATH, COREPATH])
sys.path = list(set(sys.path))
from Common import DeviceType, WallpadVendor, PacketType


class PacketParserCommon(object):
    __metaclass__ = ABCMeta

    def __init__(self, vendor: WallpadVendor):
        self._vendor = vendor

    def release(self):
        pass

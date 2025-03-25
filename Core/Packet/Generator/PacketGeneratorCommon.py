import os
import sys
from abc import ABCMeta, abstractmethod
CURPATH = os.path.dirname(os.path.abspath(__file__))  # {PROJ}/Core/Packet/Generator
COREPATH = os.path.dirname(os.path.dirname(CURPATH))
sys.path.extend([CURPATH, COREPATH])
sys.path = list(set(sys.path))
from Common import DeviceType, WallpadVendor, PacketType


class PacketGeneratorCommon(object):
    __metaclass__ = ABCMeta

    def __init__(self, vendor: WallpadVendor):
        self._vendor = vendor

    def generate(self, dev_type: DeviceType, packet_type: PacketType, **kwargs) -> bytearray:
        packet = bytearray()
        if dev_type == DeviceType.LIGHT:
            if packet_type == PacketType.QUERY:
                packet.extend(self._generateLightQuery(**kwargs))
            elif packet_type == PacketType.COMMAND:
                packet.extend(self._generateLightCommand(**kwargs))
            elif packet_type == PacketType.RESPONSE:
                packet.extend(self._generateLightResponse(**kwargs))
        elif dev_type == DeviceType.DIMMINGLIGHT:
            if packet_type == PacketType.QUERY:
                packet.extend(self._generateDimmingLightQuery(**kwargs))
            elif packet_type == PacketType.COMMAND:
                packet.extend(self._generateDimmingLightCommand(**kwargs))
            elif packet_type == PacketType.RESPONSE:
                packet.extend(self._generateDimmingLightResponse(**kwargs))
        elif dev_type == DeviceType.EMOTIONLIGHT:
            if packet_type == PacketType.QUERY:
                packet.extend(self._generateEmotionLightQuery(**kwargs))
            elif packet_type == PacketType.COMMAND:
                packet.extend(self._generateEmotionLightCommand(**kwargs))
            elif packet_type == PacketType.RESPONSE:
                packet.extend(self._generateEmotionLightResponse(**kwargs))
        elif dev_type == DeviceType.OUTLET:
            if packet_type == PacketType.QUERY:
                packet.extend(self._generateOutletQuery(**kwargs))
            elif packet_type == PacketType.COMMAND:
                packet.extend(self._generateOutletCommand(**kwargs))
            elif packet_type == PacketType.RESPONSE:
                packet.extend(self._generateOutletResponse(**kwargs))
        elif dev_type == DeviceType.THERMOSTAT:
            if packet_type == PacketType.QUERY:
                packet.extend(self._generateThermostatQuery(**kwargs))
            elif packet_type == PacketType.COMMAND:
                packet.extend(self._generateThermostatCommand(**kwargs))
            elif packet_type == PacketType.RESPONSE:
                packet.extend(self._generateThermostatResponse(**kwargs))
        elif dev_type == DeviceType.AIRCONDITIONER:
            if packet_type == PacketType.QUERY:
                packet.extend(self._generateAirconditionerQuery(**kwargs))
            elif packet_type == PacketType.COMMAND:
                packet.extend(self._generateAirconditionerCommand(**kwargs))
            elif packet_type == PacketType.RESPONSE:
                packet.extend(self._generateAirconditionerResponse(**kwargs))
        elif dev_type == DeviceType.GASVALVE:
            if packet_type == PacketType.QUERY:
                packet.extend(self._generateGasvalveQuery(**kwargs))
            elif packet_type == PacketType.COMMAND:
                packet.extend(self._generateGasvalveCommand(**kwargs))
            elif packet_type == PacketType.RESPONSE:
                packet.extend(self._generateGasvalveResponse(**kwargs))
        elif dev_type == DeviceType.VENTILATOR:
            if packet_type == PacketType.QUERY:
                packet.extend(self._generateVentilatorQuery(**kwargs))
            elif packet_type == PacketType.COMMAND:
                packet.extend(self._generateVentilatorCommand(**kwargs))
            elif packet_type == PacketType.RESPONSE:
                packet.extend(self._generateVentilatorResponse(**kwargs))
        elif dev_type == DeviceType.ELEVATOR:
            if packet_type == PacketType.QUERY:
                packet.extend(self._generateElevatorQuery(**kwargs))
            elif packet_type == PacketType.COMMAND:
                packet.extend(self._generateElevatorCommand(**kwargs))
            elif packet_type == PacketType.RESPONSE:
                packet.extend(self._generateElevatorResponse(**kwargs))
        elif dev_type == DeviceType.BATCHOFFSWITCH:
            if packet_type == PacketType.QUERY:
                packet.extend(self._generateBatchoffswitchQuery(**kwargs))
            elif packet_type == PacketType.COMMAND:
                packet.extend(self._generateBatchoffswitchCommand(**kwargs))
            elif packet_type == PacketType.RESPONSE:
                packet.extend(self._generateBatchoffswitchResponse(**kwargs))
        else:
            pass
        return packet

    @abstractmethod
    def _generateLightQuery(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateLightCommand(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateLightResponse(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateDimmingLightQuery(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateDimmingLightCommand(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateDimmingLightResponse(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateEmotionLightQuery(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateEmotionLightCommand(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateEmotionLightResponse(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateOutletQuery(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateOutletCommand(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateOutletResponse(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateThermostatQuery(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateThermostatCommand(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateThermostatResponse(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateAirconditionerQuery(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateAirconditionerCommand(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateAirconditionerResponse(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateGasvalveQuery(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateGasvalveCommand(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateGasvalveResponse(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateVentilatorQuery(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateVentilatorCommand(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateVentilatorResponse(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateElevatorQuery(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateElevatorCommand(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateElevatorResponse(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateBatchoffswitchQuery(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateBatchoffswitchCommand(self, **kwargs) -> bytearray:
        return bytearray()

    @abstractmethod
    def _generateBatchoffswitchResponse(self, **kwargs) -> bytearray:
        return bytearray()

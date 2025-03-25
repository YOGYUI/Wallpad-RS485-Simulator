from DeviceCommon import DeviceCommon, DeviceType


class Elevator(DeviceCommon):
    def __init__(self, name: str, index: int, room_index: int, rs485_index: int):
        super().__init__(DeviceType.ELEVATOR, name, index, room_index, rs485_index)

    def getQueryPacket(self, params: dict) -> bytearray:
        pass

    def getCommandPacket(self, params: dict) -> bytearray:
        pass

    def getResponsePacket(self, params: dict) -> bytearray:
        pass

    def handleCommand(self, params: dict):
        pass

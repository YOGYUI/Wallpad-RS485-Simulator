from DeviceCommon import DeviceCommon, DeviceType


class Light(DeviceCommon):
    def __init__(self, name: str, index: int, room_index: int, rs485_index: int):
        super().__init__(DeviceType.LIGHT, name, index, room_index, rs485_index)

    def getQueryPacket(self, params: dict) -> bytearray:
        pass

    def getCommandPacket(self, params: dict) -> bytearray:
        pass

    def getResponsePacket(self, params: dict) -> bytearray:
        pass

    def handleCommand(self, params: dict):
        pass


class DimingLight(DeviceCommon):
    def __init__(self, name: str, index: int, room_index: int, rs485_index: int):
        super().__init__(DeviceType.DIMMINGLIGHT, name, index, room_index, rs485_index)

    def getQueryPacket(self, params: dict) -> bytearray:
        pass

    def getCommandPacket(self, params: dict) -> bytearray:
        pass

    def getResponsePacket(self, params: dict) -> bytearray:
        pass

    def handleCommand(self, params: dict):
        pass


class EmotionLight(DeviceCommon):
    def __init__(self, name: str, index: int, room_index: int, rs485_index: int):
        super().__init__(DeviceType.EMOTIONLIGHT, name, index, room_index, rs485_index)

    def getQueryPacket(self, params: dict) -> bytearray:
        pass

    def getCommandPacket(self, params: dict) -> bytearray:
        pass

    def getResponsePacket(self, params: dict) -> bytearray:
        pass

    def handleCommand(self, params: dict):
        pass

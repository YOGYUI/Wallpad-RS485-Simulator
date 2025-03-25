from PacketParserCommon import *


class PacketParserHyundai(PacketParserCommon):
    def __init__(self):
        super().__init__(WallpadVendor.HYUNDAI)

from PacketParserCommon import *


class PacketParserSamsung(PacketParserCommon):
    def __init__(self):
        super().__init__(WallpadVendor.SAMSUNG)

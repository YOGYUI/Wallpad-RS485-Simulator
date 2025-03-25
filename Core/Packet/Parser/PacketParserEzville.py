from PacketParserCommon import *


class PacketParserEzville(PacketParserCommon):
    def __init__(self):
        super().__init__(WallpadVendor.EZVILLE)

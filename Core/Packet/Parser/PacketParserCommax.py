from PacketParserCommon import *


class PacketParserCommax(PacketParserCommon):
    def __init__(self):
        super().__init__(WallpadVendor.COMMAX)

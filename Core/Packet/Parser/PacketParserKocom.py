from PacketParserCommon import *


class PacketParserKocom(PacketParserCommon):
    def __init__(self):
        super().__init__(WallpadVendor.KOCOM)

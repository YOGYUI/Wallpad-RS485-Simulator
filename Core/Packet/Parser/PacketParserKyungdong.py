from PacketParserCommon import *


class PacketParserKyungdong(PacketParserCommon):
    def __init__(self):
        super().__init__(WallpadVendor.KYUNGDONG)

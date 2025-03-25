from PacketParserCommon import *


class PacketParserCvnet(PacketParserCommon):
    def __init__(self):
        super().__init__(WallpadVendor.CVNET)

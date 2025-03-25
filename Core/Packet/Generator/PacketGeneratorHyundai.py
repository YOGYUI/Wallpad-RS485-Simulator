from PacketGeneratorCommon import *


class PacketGeneratorHyundai(PacketGeneratorCommon):
    def __init__(self):
        super().__init__(WallpadVendor.HYUNDAI)
    
    def _generateLightQuery(self, **kwargs) -> bytearray:
        return bytearray()
    
    def _generateLightCommand(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateLightResponse(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateDimmingLightQuery(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateDimmingLightCommand(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateDimmingLightResponse(self, **kwargs) -> bytearray:
        return bytearray()
    
    def _generateEmotionLightQuery(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateEmotionLightCommand(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateEmotionLightResponse(self, **kwargs) -> bytearray:
        return bytearray()
    
    def _generateOutletQuery(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateOutletCommand(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateOutletResponse(self, **kwargs) -> bytearray:
        return bytearray()
    
    def _generateThermostatQuery(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateThermostatCommand(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateThermostatResponse(self, **kwargs) -> bytearray:
        return bytearray()
    
    def _generateAirconditionerQuery(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateAirconditionerCommand(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateAirconditionerResponse(self, **kwargs) -> bytearray:
        return bytearray()
    
    def _generateGasvalveQuery(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateGasvalveCommand(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateGasvalveResponse(self, **kwargs) -> bytearray:
        return bytearray()
    
    def _generateVentilatorQuery(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateVentilatorCommand(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateVentilatorResponse(self, **kwargs) -> bytearray:
        return bytearray()
    
    def _generateElevatorQuery(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateElevatorCommand(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateElevatorResponse(self, **kwargs) -> bytearray:
        return bytearray()
    
    def _generateBatchoffswitchQuery(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateBatchoffswitchCommand(self, **kwargs) -> bytearray:
        return bytearray()

    def _generateBatchoffswitchResponse(self, **kwargs) -> bytearray:
        return bytearray()

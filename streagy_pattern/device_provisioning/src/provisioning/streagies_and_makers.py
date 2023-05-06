class FirmwareUpgradeStreagy:
    def upgrade(self, device_model: str, firmware_version: str):
        raise NotImplementedError

class CiscoFirmwareUpgradeStreagy(FirmwareUpgradeStreagy):
    def upgrade(self, device_model: str, firmware_version: str):
        print(f"Cisco device model '{device_model}' upgrade firmware to {firmware_version}")

class JuniperFirmwareUpgradeStreagy(FirmwareUpgradeStreagy):
    def upgrade(self, device_model: str, firmware_version: str):
        print(f"Juniper device model '{device_model}' upgrade firmware to {firmware_version}")
    
class FirmwareUpdater:
    def __init__(self, streagy: FirmwareUpgradeStreagy):
        self.streagy: FirmwareUpgradeStreagy = streagy

    def upgrade(self, device_model: str, firmware_version: str):
        return self.streagy.upgrade(device_model=device_model, firmware_version=firmware_version)
    
class ConfigChangeStreagy:
    def change(self, device_model: str, configs: dict):
        raise NotImplementedError
    
class CiscoConfigChangeStreagy(ConfigChangeStreagy):
    def change(self, device_model: str, configs: dict):
        print(f"Set configs to Cisco device model '{device_model}' with configs {configs}")

class JuniperConfigChangeStreagy(ConfigChangeStreagy):
    def change(self, device_model: str, configs: dict):
        print(f"Set configs to Juniper device model '{device_model}' with configs {configs}")

class ConfigChanger:
    def __init__(self, streagy: ConfigChangeStreagy):
        self.streagy: ConfigChangeStreagy = streagy

    def change(self, device_model: str, configs: dict):
        self.streagy.change(device_model=device_model, configs=configs)
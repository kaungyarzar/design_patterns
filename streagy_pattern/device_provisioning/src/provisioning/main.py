import sys
from provisioning.streagies_and_makers import (
    FirmwareUpgradeStreagy,
    CiscoFirmwareUpgradeStreagy,
    JuniperFirmwareUpgradeStreagy,
    FirmwareUpdater,
    ConfigChangeStreagy,
    CiscoConfigChangeStreagy,
    JuniperConfigChangeStreagy,
    ConfigChanger
)

support_models = ['cisco', 'juniper']

fw_updaters = {
    'cisco': FirmwareUpdater(CiscoFirmwareUpgradeStreagy()),
    'juniper': FirmwareUpdater(JuniperFirmwareUpgradeStreagy())
}

cfg_changers = {
    'cisco': ConfigChanger(CiscoConfigChangeStreagy()),
    'juniper': ConfigChanger(JuniperConfigChangeStreagy())
}

def start(model_name: str):
    if model_name not in support_models:
        print(f"Model '{model_name}' is not supported")
        sys.exit(1)
    else:
        # Firmware upgrade
        fw_updater: FirmwareUpdater = fw_updaters.get(model_name)
        fw_updater.upgrade(model_name, 'v1.2')

        # Config change
        cfg_changer: ConfigChanger = cfg_changers.get(model_name)
        cfg_changer.change(model_name, {'lan0':'enable'})
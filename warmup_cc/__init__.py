# modelled on https://developers.home-assistant.io/docs/en/dev_101_services.html
# combined with snippets from https://github.com/foxy82/warmup4IE/blob/update_all_rooms_at_once/warmup_cc/climate.py

from homeassistant.const import (
    ATTR_ENTITY_ID,
    ATTR_TEMPERATURE,
    CONF_PASSWORD,
    CONF_USERNAME,
    PRECISION_HALVES,
    TEMP_CELSIUS,
)
DOMAIN = 'warmup'

_LOGGER = logging.getLogger(__name__)

ATTR_UNTIL = "until"

CONF_LOCATION = "location"
CONF_TARGET_TEMP = "target_temp"

DEFAULT_NAME = "warmup4ie"
DEFAULT_TARGET_TEMP = 20


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the climate devices."""
    hass.data.setdefault(DOMAIN, {})

    def service_set_override(call):
        """Handle the service call."""
        entity_id = call.data.get(ATTR_ENTITY_ID)
        temperature = call.data.get(ATTR_TEMPERATURE)
        until = call.data.get(
            ATTR_UNTIL, (datetime.now() + timedelta(hours=1)).strftime("%H:%M")
        )
        target_devices = [
            dev for dev in hass.data[DOMAIN]["entities"] if dev.entity_id in entity_id
        ]
        target_device: WarmupThermostat
        for target_device in target_devices:
            target_device.set_override(temperature, until)
            target_device.schedule_update_ha_state(True)

    _LOGGER.info("Setting up platform for Warmup component")
    user = config.get(CONF_USERNAME)
    password = config.get(CONF_PASSWORD)

    warmup = Warmup4IE(user, password)

    if warmup is None or not warmup.setup_finished:
        raise PlatformNotReady
    warmup_client = WarmupClient(warmup)
    to_add = []
    for device in warmup.get_all_devices().values():
        to_add.append(WarmupThermostat(hass, device, warmup_client))
    add_entities(to_add)
    hass.data[DOMAIN]["entities"] = to_add
    hass.services.register(DOMAIN, "set_override", service_set_override)
    return True

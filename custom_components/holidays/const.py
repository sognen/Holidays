"""Define constants used in garbage_collection."""

from datetime import datetime
from typing import Any

import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.const import CONF_NAME

from .config_singularity import config_singularity

"""Constants for holidays."""
# Base component constants
DOMAIN = "holidays"
CALENDAR_PLATFORM = "calendar"
ATTRIBUTION = "Data from this is provided by holidays."

ATTR_NEXT_DATE = "next_date"
ATTR_NEXT_HOLIDAY = "next_holiday"
ATTR_LAST_UPDATED = "last_updated"
ATTR_HOLIDAYS = "holidays"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"
DEVICE_CLASS = "holidays__schedule"

# Configuration
CONF_CALENDAR = "calendar"
CONF_ICON_NORMAL = "icon_normal"
CONF_ICON_TODAY = "icon_today"
CONF_ICON_TOMORROW = "icon_tomorrow"
CONF_COUNTRY = "country"
CONF_HOLIDAY_POP_NAMED = "holiday_pop_named"
CONF_PROV = "prov"
CONF_STATE = "state"
CONF_OBSERVED = "observed"
CONF_CALENDARS = "calendars"

# Defaults
DEFAULT_NAME = DOMAIN

# Icons
DEFAULT_ICON_NORMAL = "mdi:trash-can"
DEFAULT_ICON_TODAY = "mdi:delete-restore"
DEFAULT_ICON_TOMORROW = "mdi:delete-circle"
ICON = DEFAULT_ICON_NORMAL

COUNTRY_CODES = [
    "AR",
    "AT",
    "AU",
    "AW",
    "AZ",
    "BE",
    "BG",
    "BR",
    "BY",
    "CA",
    "CH",
    "CO",
    "CZ",
    "DE",
    "DK",
    "DO",
    "ECB",
    "EE",
    "ES",
    "ET",
    "FI",
    "FRA",
    "HR",
    "HU",
    "IE",
    "IND",
    "IS",
    "IT",
    "JP",
    "KE",
    "KZ",
    "LT",
    "LU",
    "MK",
    "MX",
    "NG",
    "NI",
    "NL",
    "NO",
    "NZ",
    "PE",
    "PL",
    "PT",
    "PTE",
    "RU",
    "SE",
    "SI",
    "SK",
    "TN",
    "TW",
    "UA",
    "US",
    "ZA",
    "England",
    "Wales",
    "Scotland",
    "IsleOfMan",
    "NorthernIreland",
]


def date_text(value: Any) -> str:
    """Have to store date as text - datetime is not JSON serialisable."""
    if value is None or value == "":
        return ""
    try:
        return datetime.strptime(value, "%Y-%m-%d").date().strftime("%Y-%m-%d")
    except ValueError:
        raise vol.Invalid(f"Invalid date: {value}")


def time_text(value: Any) -> str:
    """Have to store time as text - datetime is not JSON serialisable."""
    if value is None or value == "":
        return ""
    try:
        return datetime.strptime(value, "%H:%M").time().strftime("%H:%M")
    except ValueError:
        raise vol.Invalid(f"Invalid date: {value}")


def month_day_text(value: Any) -> str:
    """Validate format month/day."""
    if value is None or value == "":
        return ""
    try:
        return datetime.strptime(value, "%m/%d").date().strftime("%m/%d")
    except ValueError:
        raise vol.Invalid(f"Invalid date: {value}")


class configuration(config_singularity):
    """Store validation schema for holidays configuration.

    Type and validation seems duplicate, but I cannot use custom validators in ShowForm
    It calls convert from voluptuous-serialize that does not accept them
    so I pass it twice - once the type, then the validator.
    """

    options = {
        CONF_NAME: {
            "step": 1,
            "method": vol.Required,
            "type": str,
            "validator": cv.string,
        },
        CONF_ICON_NORMAL: {
            "step": 1,
            "method": vol.Optional,
            "default": DEFAULT_ICON_NORMAL,
            "type": str,
            "validator": cv.icon,
        },
        CONF_ICON_TODAY: {
            "step": 1,
            "method": vol.Optional,
            "default": DEFAULT_ICON_TODAY,
            "type": str,
            "validator": cv.icon,
        },
        CONF_ICON_TOMORROW: {
            "step": 1,
            "method": vol.Optional,
            "default": DEFAULT_ICON_TOMORROW,
            "type": str,
            "validator": cv.icon,
        },
        CONF_COUNTRY: {
            "step": 1,
            "method": vol.Required,
            "type": vol.In(COUNTRY_CODES),
        },
        CONF_HOLIDAY_POP_NAMED: {
            "step": 1,
            "method": vol.Optional,
            "type": str,
            "validator": vol.All(cv.ensure_list, [str]),
        },
        CONF_PROV: {
            "step": 1,
            "method": vol.Optional,
            "type": str,
            "validator": cv.string,
        },
        CONF_STATE: {
            "step": 1,
            "method": vol.Optional,
            "type": str,
            "validator": cv.string,
        },
        CONF_OBSERVED: {
            "step": 1,
            "method": vol.Optional,
            "default": True,
            "type": bool,
            "validator": cv.boolean,
        },
    }

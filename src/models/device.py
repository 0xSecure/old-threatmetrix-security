import dataclasses

from src.enums.obfuscated_payload_key import ObfuscatedPayloadKey


@dataclasses.dataclass
class Device:
    agent_security_path_level: str
    firebase_push_token: str
    connection_type: str
    in_call_status: int
    uptime_mills: float
    charge_level: float
    language_code: str
    system_proxy: str
    selinux_mode: str
    total_space: int
    os_version: int
    timezone: str
    firmware: str
    model: str
    brand: str
    name: str
    os: str

    def as_dict(self) -> dict:
        return {
            ObfuscatedPayloadKey.DEVICE_NAME: self.name,
            ObfuscatedPayloadKey.AGENT_LANGUAGE: f"{self.language_code}-",
            ObfuscatedPayloadKey.AGENT_LOCALE: f"{self.language_code}_",
            ObfuscatedPayloadKey.AGENT_OS: self.os,
            ObfuscatedPayloadKey.AGENT_OS_VERSION: self.os_version,
            ObfuscatedPayloadKey.AGENT_CONF_OS: self.os,
            ObfuscatedPayloadKey.FIREBASE_PUSH_TOKEN: self.firebase_push_token,
            ObfuscatedPayloadKey.IN_CALL_STATUS: self.in_call_status,
            ObfuscatedPayloadKey.NETWORK_INFO_VPN: False,
            ObfuscatedPayloadKey.AGENT_SECURITY_PATCH_LEVEL: self.agent_security_path_level,
            ObfuscatedPayloadKey.TIMEZONE_NAME: self.timezone,
            ObfuscatedPayloadKey.DEVICE_DEV_ENABLED_STATUS: False,
            ObfuscatedPayloadKey.DEVICE_BATTERY_STATUS: {
                "level": self.charge_level,
                "status": "full"
            },
            ObfuscatedPayloadKey.AGENT_BRAND: f"{self.brand}, {self.brand}",
            ObfuscatedPayloadKey.DEVICE_TOTAL_SPACE: self.total_space,
            ObfuscatedPayloadKey.AGENT_DEVICE: self.firmware,
            ObfuscatedPayloadKey.AGENT_MODEL: self.model,
            ObfuscatedPayloadKey.AGENT_TYPE: "agent_mobile",
            ObfuscatedPayloadKey.SYSTEM_PROXY: self.system_proxy,
            ObfuscatedPayloadKey.NETWORK_INFO_TYPE: self.connection_type,
            ObfuscatedPayloadKey.SELINUX_MODE: self.selinux_mode,
            ObfuscatedPayloadKey.PLUGIN_PATH_STR: {
                "description": "Not cloned"
            },
            ObfuscatedPayloadKey.UPTIME_MILLIS: self.uptime_mills
        }

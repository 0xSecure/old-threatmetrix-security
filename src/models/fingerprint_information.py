import dataclasses
import hashlib

from src.enums.obfuscated_payload_key import ObfuscatedPayloadKey
from src.models.device import Device


@dataclasses.dataclass
class FingerprintInformation:
    organization_id: str
    organization_url: str
    root_paths: list[str]
    session_id: str
    user_agent: str
    device: Device
    version: str
    guid: str

    def to_urlencoded_format(self) -> str:
        data = {
            ObfuscatedPayloadKey.CHECKSUM_SESSION_ID: hashlib.md5(
                self.organization_id + self.session_id
            ).hexdigest(),
            ObfuscatedPayloadKey.ORGANIZATION_URL: self.organization_url,
            ObfuscatedPayloadKey.ORGANIZATION_URL_MOBILE: f"{self.organization_url}/mobile",
            ObfuscatedPayloadKey.AGENT_VERSION: self.version,
            ObfuscatedPayloadKey.ROOT_DETECTION_PATH_STR: ";".join(self.root_paths),
            ObfuscatedPayloadKey.ROOT_DETECTION_PATH_COUNT: len(self.root_paths),
            ObfuscatedPayloadKey.TAMPER_CODE_AUTH_MODULE: 0,
            ObfuscatedPayloadKey.USER_AGENT: self.user_agent,
            ObfuscatedPayloadKey.GUID: self.guid
        } | self.device.as_dict()
        return ""

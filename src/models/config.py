from __future__ import annotations

import base64
import dataclasses
import xml.etree.ElementTree as ElementTree

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

from src import utils


@dataclasses.dataclass
class Config:
    sn: str
    n: str
    s: str
    unique_id: str  # w parameter
    
    @classmethod
    def from_response(cls, response: str, session_id: str, organization_id: str) -> Config:
        crypted_data = base64.b64decode(response)
        data, key = utils.crypto.extract_data_and_key(crypted_data=crypted_data)
        cipher = AES.new(
            key=utils.crypto.create_payload_key(
                session_id=session_id.encode("utf-8"),
                organization_id=organization_id.encode("utf-8"),
                salt_key=key
            ),
            mode=AES.MODE_CBC,
            iv=bytes.fromhex("00000000000000000000000000000000")
        )
        tree = ElementTree.fromstring(unpad(
            padded_data=cipher.decrypt(data),
            block_size=16
        ).decode("utf-8"))
        return cls(
            sn=tree.find("SN").text,
            n=tree.find("N").text,
            s=tree.find("S").text,
            unique_id=tree.find("w").text
        )

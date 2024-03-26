import itertools
import zlib

KEY_LENGTH = 16


def extract_data_and_key(crypted_data: bytes, length: int = KEY_LENGTH) -> tuple[bytearray, bytearray]:
    data, key = bytearray(), bytearray()

    for i in range(0, length * 2, 2):
        data.append(crypted_data[i])
        key.append(crypted_data[i + 1])

    data.extend(crypted_data[length * 2:])
    return data, key


def get_crc32(data: bytes) -> bytes:
    return zlib.crc32(data).to_bytes(4, "big")


def create_payload_key(session_id: bytes, organization_id: bytes, salt_key: bytes) -> bytes:
    return b"".join([
        get_crc32(salt_key + session_id),
        get_crc32(salt_key + organization_id),
        get_crc32(session_id + salt_key),
        get_crc32(organization_id + salt_key)
    ])


def xor(data: bytes, key: bytes) -> bytearray:
    xored_data = bytearray()
    for data_byte, key_byte in zip(data, itertools.cycle(key)):
        xored_data.append(data_byte ^ (key_byte & 10))
    return xored_data

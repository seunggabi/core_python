import hashlib
import base64

from seunggabi_core_python.util import date_util

ENCODE = "utf-8"
DELIMITER = "$"


def md5(plain: str, seed: str) -> str:
    h = hashlib.md5()
    h.update(plain.encode(ENCODE) + seed.encode(ENCODE))
    return h.hexdigest()


def sha256(plain: str, seed: str) -> str:
    h = hashlib.sha256()
    h.update(plain.encode(ENCODE) + seed.encode(ENCODE))
    return h.hexdigest()


def encode(plain: str) -> str:
    return base64.b64encode(plain).decode(ENCODE)


def decode(cipher: str) -> str:
    return base64.b64decode(cipher).decode(ENCODE)


def crypt(
    plain: str,
    seed: str = "",
    seed2: str = ""
) -> str:
    if not seed2:
        seed2 = seed

    c = md5(plain, seed)
    c = sha256(c, seed2)

    return encode(c + DELIMITER + date_util.timestamp())

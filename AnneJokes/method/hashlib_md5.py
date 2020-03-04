import hashlib
import base64
# md5¼ÓÃÜ,·µ»Ø¼ÓÃÜ×Ö·û´®


def str_md5(str_obj):
    md5_obj = hashlib.md5()
    byte_str = str_obj.encode("utf-8")
    md5_obj.update(byte_str)

    return md5_obj.hexdigest()


def base64_encode(string):
    return base64.b64encode(string)


def base64_decode(string):
    return base64.b64decode(string)

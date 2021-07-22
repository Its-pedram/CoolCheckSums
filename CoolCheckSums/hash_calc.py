import hashlib
from config import CONFIG
from ccs_utils import clear_terminal, credit


def md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(CONFIG["BUFFER_SIZE"])
            if not data:
                break
            md5_hash.update(data)
    return md5_hash.hexdigest()


def sha1(file_path):
    sha1_hash = hashlib.sha1()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(CONFIG["BUFFER_SIZE"])
            if not data:
                break
            sha1_hash.update(data)
    return sha1_hash.hexdigest()


def sha224(file_path):
    sha224_hash = hashlib.sha224()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(CONFIG["BUFFER_SIZE"])
            if not data:
                break
            sha224_hash.update(data)
    return sha224_hash.hexdigest()


def sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(CONFIG["BUFFER_SIZE"])
            if not data:
                break
            sha256_hash.update(data)
    return sha256_hash.hexdigest()


def sha384(file_path):
    sha384_hash = hashlib.sha384()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(CONFIG["BUFFER_SIZE"])
            if not data:
                break
            sha384_hash.update(data)
    return sha384_hash.hexdigest()


def sha512(file_path):
    sha512_hash = hashlib.sha512()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(CONFIG["BUFFER_SIZE"])
            if not data:
                break
            sha512_hash.update(data)
    return sha512_hash.hexdigest()


def auto(file_path, checksum, type):
    pos = 0

    print(f"Entered Checksum: [{type}] {checksum}\n"
          "Calculated Checksum(s):")
    for hash_func in hash_funcs_list:
        calculated_sum = hash_func(file_path)
        if calculated_sum == checksum:
            print("[✔] Found A Matching Checksum:")
            print(hash_funcs_names[pos] + f" {calculated_sum}")
            return True
        else:
            print(hash_funcs_names[pos] + f" {calculated_sum}")
        pos += 1
    print("[❌] No Matching Checksums Found.")


def all(file_path, type):
    pos = 0
    print("[✔] Calculated Checksum(s):")
    for hash_func in hash_funcs_list:
        print(hash_funcs_names[pos] + " " + hash_func(file_path))
        pos += 1


hash_funcs_list = [md5, sha1, sha224, sha256, sha384, sha512]
hash_funcs_names = ["[MD5]:", "[SHA1]:", "[SHA224]:", "[SHA256]:", "[SHA384]:", "[SHA512]:"]

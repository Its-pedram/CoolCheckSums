import os
import sys
import hashlib
from os import system

config = {
    "VER": 1.0,
    "BUFFER_SIZE": 65536
}


def credit():
    print(f"""
      ____ _               _        _    ____                  
     / ___| |__   ___  ___| | __   / \  / ___| _   _ _ __ ___  
    | |   | '_ \ / _ \/ __| |/ /  / _ \ \___ \| | | | '_ ` _ \ 
    | |___| | | |  __/ (__|   <  / ___ \ ___) | |_| | | | | | |
     \____|_| |_|\___|\___|_|\_\/_/   \_\____/ \__,_|_| |_| |_|
                            ItsPedram                                                       
       """)


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def calc_md5(file_path):
    md5 = hashlib.md5()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(config["BUFFER_SIZE"])
            if not data:
                break
            md5.update(data)
    return "[MD5] " + md5.hexdigest()


def calc_sha1(file_path):
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(config["BUFFER_SIZE"])
            if not data:
                break
            sha1.update(data)
    return "[SHA1] " + sha1.hexdigest()


def calc_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(config["BUFFER_SIZE"])
            if not data:
                break
            sha256.update(data)
    return "[SHA256] " + sha256.hexdigest()


def auto(file_path, checksum):
    clear_terminal()
    credit()
    hash_funcs_list = [calc_md5, calc_sha1, calc_sha256]
    print(f"Entered Checksum:    {checksum}\n"
          "Calculated Checksum(s):")
    for hash_func in hash_funcs_list:
        calculated_sum = hash_func(file_path)
        if calculated_sum.split()[1] == checksum:
            print("[✔] Found A Matching Checksum:\n"
                  f"{calculated_sum}")
            return True
        else:
            print(f"{calculated_sum}")
    print("[❌] No Matching Checksums Found.")


def verify(checksum, calculated_sum):
    clear_terminal()
    credit()
    print(f"Entered Checksum:    {checksum}\n"
          f"Calculated Checksum: {calculated_sum}")
    if checksum == calculated_sum.split()[1]:
        print("[✔] The Checksums Match!")
        return True
    else:
        print("[❌] The Checksums Don't Match.")
        return False


def check(file_path, checksum, type):
    clear_terminal()
    print("Calculating....")
    if not type or type == "auto":
        print("Selected Type: Auto")
        auto(file_path, checksum)
    elif type == "md5":
        print(f"Selected Type: {type.upper()}")
        verify(checksum, calc_md5(file_path))
    elif type == "sha1":
        print(f"Selected Type: {type.upper()}")
        verify(checksum, calc_sha1(file_path))
    elif type == "sha256":
        print(f"Selected Type: {type.upper()}")
        verify(checksum, calc_sha256(file_path))
    else:
        clear_terminal()
        print("Selected An Unknown Type! \n"
              "Known Types: MD5, SHA1, SHA256, Auto")


credit()
if "-help" in sys.argv:
    print("[INFO] Usages: \n"
          "cas [FileName.Ext] [checksum] [Type] \n"
          "Types (Default: Auto): MD5, SHA1, SHA256, Auto")
elif len(sys.argv) < 3:
    print("[ERROR] Not Enough Arguments Found! Usages: \n"
          "cas [FileName.Ext] [checksum] [Type] \n"
          "Types (Default: Auto): MD5, SHA1, SHA256, Auto")
elif len(sys.argv) == 3:
    check(sys.argv[1], sys.argv[2], "")
elif len(sys.argv) == 4:
    check(sys.argv[1], sys.argv[2], sys.argv[3].lower())

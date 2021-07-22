import math
import os
import sys

from config import CONFIG


def credit():
    print(f"""\
|___________________________________________________________________________|
|   ____            _  ____ _               _     ____                      |
|  / ___|___   ___ | |/ ___| |__   ___  ___| | __/ ___| _   _ _ __ ___  ___ |
| | |   / _ \ / _ \| | |   | '_ \ / _ \/ __| |/ /\___ \| | | | '_ ` _ \/ __||
| | |__| (_) | (_) | | |___| | | |  __/ (__|   <  ___) | |_| | | | | | \__ \| 
| \____\___/ \___/|_|\____|_| |_|\___|\___|_|\_\|____/ \__,_|_| |_| |_|___/ |
|                    VERSION: 2.0 |  By ItsPedram | 2021                    |
|___________________________________________________________________________|
 """)


# If you wonder why this isn't working in your IDE, it's because it's not supposed to!
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_help():
    print("[INFO] Usages: \n"
          "ccs -c (-compare) [FileName.Ext] [checksum] [Type] \n"
          "Types (Default: Auto): MD5, SHA1, SHA224, SHA256, SHA384, SHA512, Auto \n"
          "ccs -g (-get) [FileName.Ext] [Type] \n"
          "Types (Default: All): MD5, SHA1, SHA224, SHA256, SHA384, SHA512, All")


def file_info():
    print("FileName: " + os.path.basename(sys.argv[2]))
    print("FileSize: " + convert_size(os.path.getsize(sys.argv[2])))


# Credits to Stackoverflow & The Author For This Code
def convert_size(size_bytes):
    if size_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

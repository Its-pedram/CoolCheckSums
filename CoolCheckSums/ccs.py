import os
import sys
import hash_calc
from ccs_utils import clear_terminal, credit, show_help, file_info


def verify(checksum, calculated_sum):
    clear_terminal()
    credit()
    print(f"Entered Checksum:    {checksum}\n"
          f"Calculated Checksum: {calculated_sum}")
    if checksum == calculated_sum:
        print("[✔] The Checksums Match!")
        return True
    else:
        print("[❌] The Checksums Don't Match.")
        return False


def compare(file_path, checksum, type):
    if not os.path.isfile(file_path):
        print("[ERROR] The Selected File Does NOT Exist!")
        return None
    clear_terminal()
    credit()
    file_info()
    print("Calculating....")
    if not type or type == "auto":
        print("Selected Type: Auto")
        hash_calc.auto(file_path, checksum, "Auto")
    elif type == "md5":
        print(f"Selected Type: {type.upper()}")
        verify(checksum, hash_calc.md5(file_path))
    elif type == "sha1":
        print(f"Selected Type: {type.upper()}")
        verify(checksum, hash_calc.sha1(file_path))
    elif type == "sha224":
        print(f"Selected Type: {type.upper()}")
        verify(checksum, hash_calc.sha224(file_path))
    elif type == "sha256":
        print(f"Selected Type: {type.upper()}")
        verify(checksum, hash_calc.sha256(file_path))
    elif type == "sha384":
        print(f"Selected Type: {type.upper()}")
        verify(checksum, hash_calc.sha384(file_path))
    elif type == "sha512":
        print(f"Selected Type: {type.upper()}")
        verify(checksum, hash_calc.sha512(file_path))
    else:
        clear_terminal()
        print("Selected An Unknown Type! \n"
              "Known Types: MD5, SHA1, SHA224, SHA256, SHA384, SHA512, Auto")


def get(file_path, type):
    if not os.path.isfile(file_path):
        print("[ERROR] The Selected File Does NOT Exist!")
        return None
    clear_terminal()
    credit()
    print("Calculating....")
    file_info()
    if not type or type == "all":
        print("Selected Type: All")
        hash_calc.all(file_path, "All")
    elif type == "md5":
        print(f"Selected Type: {type.upper()}")
        print(hash_calc.md5(file_path))
    elif type == "sha1":
        print(f"Selected Type: {type.upper()}")
        print(hash_calc.sha1(file_path))
    elif type == "sha224":
        print(f"Selected Type: {type.upper()}")
        print(hash_calc.sha224(file_path))
    elif type == "sha256":
        print(f"Selected Type: {type.upper()}")
        print(hash_calc.sha256(file_path))
    elif type == "sha384":
        print(f"Selected Type: {type.upper()}")
        print(hash_calc.sha384(file_path))
    elif type == "sha512":
        print(f"Selected Type: {type.upper()}")
        print(hash_calc.sha512(file_path))
    else:
        clear_terminal()
        print("Selected An Unknown Type! \n"
              "Known Types: MD5, SHA1, SHA224, SHA256, SHA384, SHA512, All \n"
              "Use -help For More Information.")


credit()
try:
    if "-help" == sys.argv[1].lower():
        show_help()
    elif "-compare" == sys.argv[1].lower() or "-c" == sys.argv[1].lower():
        if len(sys.argv) < 4:
            show_help()
        elif len(sys.argv) == 4:
            compare(sys.argv[2], sys.argv[3], "")
        elif len(sys.argv) == 5:
            compare(sys.argv[2], sys.argv[3], sys.argv[4].lower())
    elif "-get" == sys.argv[1].lower() or "-g" == sys.argv[1].lower():
        if len(sys.argv) < 3:
            show_help()
        elif len(sys.argv) == 3:
            get(sys.argv[2], "")
        elif len(sys.argv) == 4:
            get(sys.argv[2], sys.argv[3].lower())
    else:
        print("Unknown Argument Detected! Showing Help:\n")
        show_help()
except IndexError:
    print("Missing Argument Detected! Showing Help:\n")
    show_help()

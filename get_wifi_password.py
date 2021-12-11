import subprocess
import re
import os

command_ouput = subprocess.run(["netsh" , "wlan" , "show" , "profile"] , capture_output=True).stdout.decode()

profile_name = (re.findall("All User Profile      :(.*)\r" , command_ouput))

wifi_list = []

if len(profile_name) != 0 :
    for name in profile_name:
        wifi_profile = {}

        profile_info = subprocess.run(["netsh" , "wlan" , "show" , "profile" , name ] , capture_output=True).stdout.decode()

        if re.search("Security key             :Absent" , profile_info):
            continue
        else:
            wifi_profile["ssid"] = name

            profile_info_pass = os.system(f"netsh wlan show profile {name} key=clear")

            password = re.search("Key content           :(.*)\r" , profile_info_pass)

            if password == None:
                wifi_profile["password"] = None

            else:

                wifi_profile["password"] = password[1]

            wifi_list.append(wifi_profile)

for x in range(len(wifi_list)):
    print(wifi_list[x])
    
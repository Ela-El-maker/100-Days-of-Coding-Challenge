import colorama
from colorama import Fore, Style

def print_cool_name():
    colorama.init(autoreset=True)
    print(Fore.GREEN + r"""
    ██╗   ██╗ ██████╗ ██╗   ██╗███████╗██╗   ██╗
    ██║   ██║██╔═══██╗██║   ██║██╔════╝╚██╗ ██╔╝
    ██║   ██║██║   ██║██║   ██║█████╗   ╚████╔╝ 
    ╚██╗ ██╔╝██║   ██║██║   ██║██╔══╝    ╚██╔╝  
     ╚████╔╝ ╚██████╔╝╚██████╔╝███████╗   ██║   
      ╚═══╝   ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   
    """ + Style.RESET_ALL)
    print(Fore.CYAN + "          - " + Fore.YELLOW + "Ela Kali" + Fore.CYAN + " -")

# Call the subroutine to print your cool name
print_cool_name()

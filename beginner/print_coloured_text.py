import colorama
from colorama import Fore, Back, Style


colorama.init(autoreset=True)

print(f"{Fore.BLUE + Back.YELLOW} Hi my name is Johnny, {Fore.YELLOW + Back.BLUE} I am your machine learning instructor")
print(f'{Back.CYAN} Hi my name is Johnny')
print(f'{Fore.RED + Back.GREEN} Hi my name is Johnny')
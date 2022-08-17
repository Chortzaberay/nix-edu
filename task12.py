import os
import colorama
from colorama import init, Fore, Style

init(autoreset=True)


def delete_files_func(path, file_extension=".txt"):
    for root, dirs, files in os.walk(path):
        list_ = []
        for file in files:
            if file.endswith(file_extension):
                list_.append(file)
                os.remove(root + "\\" + file)
                
        
        print("root: --> ", Style.BRIGHT + Fore.YELLOW + root)
        print(Style.BRIGHT + Fore.RED + f"{list_}", "\n" + "-" * 15) if list_ != [] else None
                
        


delete_files_func(path="test_folder", file_extension=".txt")

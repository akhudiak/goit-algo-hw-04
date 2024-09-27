from colorama import Fore, init
from pathlib import Path
import sys


init()


def show_content(directory: Path, indent=""):
    for path in directory.iterdir():
        if path.is_dir():
            print(indent + Fore.YELLOW + path.name)
            show_content(path, indent + "   ")
        else:
            print(indent + Fore.GREEN + path.name)


try:
    directory = Path(sys.argv[1])
    show_content(directory)
except (FileNotFoundError, NotADirectoryError) as error:
    print(error)
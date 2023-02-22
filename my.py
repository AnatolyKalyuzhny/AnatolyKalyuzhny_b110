import os
import sys

def print_help():
    print("help - получение справки")
    print("mkdir <dirname> - создание папки")
    print("ping - игра в пинг-понг")

def play_ping():
    print("pong!")

def make_dir():
    try:
        dir_name = sys.argv[2]
    except IndexError:
        print("не указана папка!")
        print_help()
        sys.exit()

    if dir_name:
        try:
            os.mkdir(dir_name)
        except FileExistsError:
            print("такая папка уже есть!")
    else:
        print("нужно было ввести название!")

do_variants = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": play_ping,
}

try:
    key = sys.argv[1]
except IndexError:
    print_help()
    sys.exit()

func_to_do = do_variants.get(key, do_variants["help"])
func_to_do()

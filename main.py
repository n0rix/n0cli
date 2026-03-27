import argparse
import hashlib
import random
import string
from datetime import datetime

__version__ = "v1.0.0"


def hello():
    print(f"hello from n0cli {__version__}")


def time():
    print(datetime.now())


def version():
    print(f"n0cli version: {__version__}")


def hash_text(text):
    result = hashlib.sha256(text.encode())
    print(result.hexdigest())


def gen(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    result = ''.join(random.choice(chars) for _ in range(length))
    print(result)


def run_interactive():
    print(f"n0CLI [{__version__}]")

    while True:
        cmd_input = input("n0cli CMD > ").strip()

        # continue, if input is empty
        if not cmd_input:
            continue

        #  exit check
        if cmd_input.lower() in ["exit", "quit"]:
            print("Exiting n0cli ... Bye")
            break

        # split string into command + args
        parts = cmd_input.split()
        cmd = parts[0].lower()
        args = parts[1:]

        # dispatch commands
        if cmd == "hello":
            hello()
        elif cmd == "version":
            version()
        elif cmd == "time":
            time()
        elif cmd == "hash":
            if args:
                hash_text(" ".join(args))
            else:
                print("No arguments provided. Usage: hash <text>")
        elif cmd == "gen":
            if args and args[0].isdigit():
                gen(int(args[0]))
            else:
                print("No arguments provided. Usage: gen <length>")
        else:
            print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    run_interactive()

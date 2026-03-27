import argparse
import hashlib
import random
import string
from datetime import datetime


def hello():
    print("hello from n0cli")


def time():
    print(datetime.now())


def hash_text(text):
    result = hashlib.sha256(text.encode())
    print(result.hexdigest())


def gen(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    result = ''.join(random.choice(chars) for _ in range(length))
    print(result)


def main():
    parser = argparse.ArgumentParser(prog="n0cli", description="simple CLI tools")

    subparsers = parser.add_subparsers(dest="command")

    # hello command
    subparsers.add_parser("hello")

    # time command
    subparsers.add_parser("time")

    # hash command
    hash_parser = subparsers.add_parser("hash")
    hash_parser.add_argument("text")

    # gen command
    gen_parser = subparsers.add_parser("gen")
    gen_parser.add_argument("length", type=int, nargs="?", default=8)

    args = parser.parse_args()

    if args.command == "hello":
        hello()

    elif args.command == "time":
        time()

    elif args.command == "hash":
        hash_text(args.text)

    elif args.command == "gen":
        gen(args.length)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()

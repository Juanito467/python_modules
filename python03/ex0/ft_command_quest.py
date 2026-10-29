import sys


def put_args(argv: list) -> None:
    i = 0
    print(f"Program name: {argv[i]}")
    i += 1
    j = len(argv)
    if j > i:
        print(f"Arguments received: {j}")
    else:
        print("No arguments provided!")
    while i < j:
        print(f"Argument {i}: {argv[i]}")
        i += 1


def menu():
    print("=== Command Quest ===")
    argv = sys.argv
    len_ar = len(argv)
    put_args(argv)
    print(f"Total arguments: {len_ar}")


if __name__ == "__main__":

    menu()

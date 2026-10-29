import sys


def validate_arguments() -> list | None:
    argv = sys.argv
    int_array = []
    try:
        for i in argv:
            int_array.append(int(i))
        return int_array
    except ValueError:
        for arg in argv:
            print(f"Invalid parameter: {arg}")
        sys.exit(1)
    except IndexError:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ..")


def menu():
    print("=== Player Score Analytics ===")
    validate_arguments()



if __name__ == "__main__":

    menu()

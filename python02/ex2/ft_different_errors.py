

def garden_operations(operation_number) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abs" + 2


def test_operation(number):
    try:
        garden_operations(number)
        print("Operation completed successfully")
    except ValueError as a:
        print(f"Caught ValueError: {a}")
    except ZeroDivisionError as b:
        print(f"Caught ZeroDivisionError: {b}")
    except FileNotFoundError as c:
        print(f"Caught FileNotFoundError: {c}")
    except TypeError as d:
        print(f"Caught TypeError: {d}")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    print("Testing operation 0...")
    test_operation(0)
    print("Testing operation 1...")
    test_operation(1)
    print("Testing operation 2...")
    test_operation(2)
    print("Testing operation 3...")
    test_operation(3)
    print("Testing operation 4...")
    test_operation(4)
    print("\nAll error types tested successfully!")


if __name__ == "__main__":

    main()

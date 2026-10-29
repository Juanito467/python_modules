
def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(temp_str: str) -> int:
    try:
        safe_data = input_temperature(temp_str)
        print(f"Temperature is now {safe_data}°C")
        return safe_data
    except ValueError as e:
        print(
            f"Caught input_temperature error:"
            f" invalid literal for int() with base 10: {e}"
            )


def main():
    print("=== Garden Temperature ===")

    print("\nInput data is '25'")
    test_temperature("25")
    print("\nInput data is 'abc'")
    test_temperature("abc")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":

    main()

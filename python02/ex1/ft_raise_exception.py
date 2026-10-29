
def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise Exception(f"{temp_str}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise Exception(f"{temp_str}°C is too cold for plants (min 0°C)")
    else:
        return temp


def test_temperature(temp_str: str) -> int:
    try:
        safe_data = input_temperature(temp_str)
        print(f"Temperature is now {safe_data}°C")
        return safe_data
    except Exception as e:
        print(f"Caught {temp_str} error: {e}")
    return None


def main():
    print("=== Garden Temperature ===")
    print("\nInput data is '25'")
    test_temperature("25")
    print("\nInput data is 'abc'")
    test_temperature("abc")
    print("\nInput data is '100'")
    test_temperature("100")
    print("\nInput data is '-50'")
    test_temperature("-50")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":

    main()

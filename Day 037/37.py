def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        raise ValueError("The input string cannot be converted into an integer.")

# Test cases
assert string_to_int("1234") == 1234
assert string_to_int("-1234") == -1234
try:
    string_to_int("123a")
except ValueError as v:
    assert str(v) == "The input string cannot be converted into an integer."

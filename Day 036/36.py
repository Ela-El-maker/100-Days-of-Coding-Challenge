def compare_string_lengths(str1, str2):
    """
    This function takes two strings and returns True if the first string is longer than the second one, otherwise False.
    """
    # Your code here
    if len(str1) == len(str2):
        print(f"{str1} and {str2} are both equal in length")
    elif len(str1) < len(str2):
        print(f"{str2} is longer than {str1}.")
    else:
        print(f"{str1} is longer than {str2}")


print(compare_string_lengths('Hello','How are you'))

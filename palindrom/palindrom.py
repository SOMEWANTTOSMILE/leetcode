def get_number():
    number = input("enter a number that is a palindromo: ")
    return number


def get_palindrome():
    number = get_number()
    reversed_number = number[::-1]
    return reversed_number, number


def check_palindrome():
    reversed_number = get_palindrome()
    rever_number, number = reversed_number[0], reversed_number[1]
    if rever_number == number:
        return True
    else:
        return False


print(check_palindrome())

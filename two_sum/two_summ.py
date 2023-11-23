def get_user_numbers():
    numbers = []
    while len(numbers) != 4:
        number = int(input("Enter number: "))
        numbers.append(number)
    return numbers


def get_target():
    target = int(input("Enter target: "))
    return target


def get_number():
    target = get_target()
    numbers = get_user_numbers()
    for first_number in numbers:
        for second_number in numbers:
            if first_number + second_number == target:
                return [numbers.index(first_number), numbers.index(second_number)]


print(get_number())

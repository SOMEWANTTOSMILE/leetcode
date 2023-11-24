def get_user_string():
    user_data = list()
    for i in range(3):
        user_string = input("Enter strings: ")
        user_data.append(user_string)
    return user_data


def find_command_prefix():
    user_data = get_user_string()
    prefix = user_data[0]
    for strings in user_data[1:]:
        while strings.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
        return prefix


print(find_command_prefix())

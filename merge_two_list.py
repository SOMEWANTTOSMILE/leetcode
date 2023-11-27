list_one = [1, 2, 10]
list_two = [2, 5, 4]


def sort_list():
    list_merge = [*list_one, *list_two]
    list_merge.sort()
    return list_merge


print(sort_list())

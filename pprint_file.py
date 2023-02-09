print('This is a file from GitHub repository')


def quick_sort(lst: list):
    if len(lst) <= 1:
        return lst

    return quick_sort([i for i in lst[1:] if i < lst[0]])\
        + [lst[0]]\
        + quick_sort([i for i in lst[1:] if i >= lst[0]])


print(quick_sort([-6, 1, 2]))

print()

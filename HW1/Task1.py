def sort_list_imperative(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key > numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key


def sort_list_declarative(numbers):
    numbers.sort(reverse=True)


if __name__ == "__main__":
    list_one = [1, 3, 2, 6, 9, 4, 4, 2]
    sort_list_imperative(list_one)
    print(list_one)

    list_two = [4, 6, 5, 8, 12, 3, 3, 0]
    sort_list_imperative(list_two)
    print(list_two)

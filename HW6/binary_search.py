def merge_sort(numbers: list[int]) -> list[int]:
    list_length = len(numbers)
    if list_length == 1:
        return numbers
    left_list = merge_sort(numbers[:list_length // 2])
    right_list = merge_sort(numbers[list_length // 2:])
    left_index = 0
    right_index = 0
    result_list = []
    while left_index < len(left_list) and right_index < len(right_list):
        left_number, right_number = left_list[left_index], right_list[right_index]
        if left_number <= right_number:
            result_list.append(left_number)
            left_index += 1
        else:
            result_list.append(right_number)
            right_index += 1
    if left_index < len(left_list):
        result_list += left_list[left_index:]
    if right_index < len(right_list):
        result_list += right_list[right_index:]

    return result_list


def binary_search(element: int, numbers: list[int]) -> int:
    if len(numbers) == 0:
        raise ValueError('Empty list')
    left_index = 0
    right_index = len(numbers) - 1
    while left_index <= right_index:
        cur_index = left_index + (right_index - left_index) // 2
        cur_number = numbers[cur_index]
        if element == cur_number:
            return cur_index
        if element < cur_number:
            right_index = cur_index - 1
        else:
            left_index = cur_index + 1
    return -1


test_list = [38, 7, 55, 88, 43, 98, 63, 72, 31, 85, 75, 60, 99, 28, 2, 53, 87, 77, 79, 32, 27, 94, 17, 42, 37, 73, 39,
             59, 1, 92, 87, 16, 96, 82, 92, 43, 36, 73, 17, 41, 84, 74, 99, 12, 48, 20, 31, 63, 46, 40, 82, 58, 50, 16,
             61, 97, 23, 47, 57, 96, 77, 20, 2, 27, 17, 54, 67, 85, 62, 30, 94]
test_element = 99

if __name__ == "__main__":
    sorted_list = merge_sort(test_list)
    print(binary_search(test_element, sorted_list))

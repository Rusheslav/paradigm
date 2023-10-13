def print_row(start, end):
    for i in range(1, 11):
        for j in range(start, end):
            print(f"{j:>2} X {i:<2} = {i * j:>2}", end="\t")
        print()
    print()


def print_table(num):
    rows_number = round(num ** 0.5)
    start = 1
    end = rows_number
    for row in range(rows_number + 1):
        if start <= end:
            print_row(start, end + 1)
        start += rows_number
        end = min(end + rows_number, num)


if __name__ == "__main__":
    print_table(50)

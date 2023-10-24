def calculate_mean(arr):
    return sum(arr) / len(arr)


def calculate_covariance(x, y, mean_x, mean_y):
    return sum(map(lambda xi, yi: (xi - mean_x) * (yi - mean_y), x, y))


def calculate_correlation(x, y):
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)

    covariance = calculate_covariance(x, y, mean_x, mean_y)
    variance_x = sum(map(lambda xi: (xi - mean_x) ** 2, x))
    variance_y = sum(map(lambda yi: (yi - mean_y) ** 2, y))

    correlation = covariance / (variance_x ** 0.5 * variance_y ** 0.5)
    return correlation


x = [1, 2, 3, 4, 51]
y = [2, 3, 4, 5, 6]

correlation_coefficient = calculate_correlation(x, y)
print(f"Корреляция Пирсона между массивами x и y: {correlation_coefficient}")

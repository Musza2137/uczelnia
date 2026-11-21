def sort_copy(arr):
    copy = []
    for x in arr:
        copy.append(x)
    n = len(copy)
    for i in range(n):
        for j in range(0, n - i - 1):
            if copy[j] > copy[j + 1]:
                temp = copy[j]
                copy[j] = copy[j + 1]
                copy[j + 1] = temp
    return copy


def second_largest(arr):
    s = sort_copy(arr)
    return s[len(s) - 2]


def min_max_diff(arr):
    s = sort_copy(arr)
    return s[len(s) - 1] - s[0]


def median(arr):
    s = sort_copy(arr)
    n = len(s)
    if n % 2 == 1:
        return s[n // 2]
    else:
        return (s[n // 2 - 1] + s[n // 2]) / 2


def min_max_array(arr):
    s = sort_copy(arr)
    return [s[0], s[len(s) - 1]]


def to_minus_string(arr):
    result = ""
    for i in range(len(arr)):
        if i > 0:
            result += "-"
        result += str(arr[i])
    return result

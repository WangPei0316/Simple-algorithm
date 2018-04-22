def binary_search_l(l, v):
    left, right = 0, len(l) - 1

    while left <= right:
        mid = (left + right) // 2
        if l[mid] < v:
            left = mid + 1
        else:
            right = mid - 1

    if l[left] == v:
        return left


def binary_search_r(l, v):
    left, right = 0, len(l) - 1

    while left <= right:
        mid = (left + right) // 2
        if l[mid] <= v:
            left = mid + 1
        else:
            right = mid - 1

    if l[right] == v:
        return right


def range_search(l, v):
    return binary_search_l(l, v), binary_search_r(l, v)


A = [1, 3, 3, 5, 7, 7, 7, 7, 8, 14, 14]
if __name__ == '__main__':
    print(range_search(A, 7))
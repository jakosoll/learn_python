

def binary_search_circle(arr, item):
    low = 0  # индекс первого элемента
    high = len(arr) - 1  # индекс последнего элемента
    count = 0
    while low <= high:
        mid = int((low + high) / 2)
        guess = arr[mid]
        count += 1
        print(f'step: {count}')
        if guess == item:
            return mid
        elif item > guess:
            low = mid + 1
        else:
            high = mid - 1
    return None


def binary_search_rec(arr, item):
    pass



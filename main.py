FULL_NAME = "Mark Anthony Beroy"


def build_unsorted_array(name):


    letters = []
    for ch in name.upper():
        if not ch.isalpha():
            continue
        if ch in letters:
            continue
        letters.append(ch)
    return letters


def insertion_sort(arr):

    result = arr[:]
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def main():
    unsorted_array = build_unsorted_array(FULL_NAME)
    sorted_array = insertion_sort(unsorted_array)

    print("Full Name      :", FULL_NAME)
    print("Unsorted array :", unsorted_array)
    print("Sorted array   :", sorted_array)


if __name__ == "__main__":
    main()
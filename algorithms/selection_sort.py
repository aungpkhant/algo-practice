# Traverses through array elements
# Find minimum element in remaining unsorted array
# Swap places to current index
# Repeat until end of list


def selection_sort(array):
    for i in range(len(array)):
        idx_of_smallest = i
        for j in range(i + 1, len(array)):
            if array[idx_of_smallest] > array[j]:
                idx_of_smallest = j

        # Swap places
        placeholder = array[i]
        array[i] = array[idx_of_smallest]
        array[idx_of_smallest] = placeholder

    return array


if __name__ == "__main__":
    assert selection_sort([2, 3, 1]) == [1, 2, 3]
    assert selection_sort([]) == []
    assert selection_sort([1, 1, 1, 1]) == [1, 1, 1, 1]


# 2, 3, 1
# 1, 3, 2
# 1, 2, 3

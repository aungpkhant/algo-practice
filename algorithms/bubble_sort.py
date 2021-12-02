from typing import Mapping


def bubble_sort(array):
    sorted = False
    while sorted == False:
        sorted = True
        for i in range(len(array)):
            if i == len(array) - 1:
                continue

            if array[i] > array[i + 1]:
                biggerNum = array[i]
                array[i] = array[i + 1]
                array[i + 1] = biggerNum
                sorted = False
    return array


if __name__ == "__main__":
    print(bubble_sort([3, 1, 2]))

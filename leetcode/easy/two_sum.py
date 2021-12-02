# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# TODO return index instead
# O(n squared) solution
# for n numbers we check n-1 numbers
def naive_two_sum(nums, target):
    for firstIndex, firstNum in enumerate(nums):
        for secondIndex, secondNum in enumerate(nums):
            if firstIndex == secondIndex:
                continue
            if(firstNum + secondNum) == target:
                return [firstIndex, secondIndex]
    # Should never happen according to question specs
    return "No Pairings"

# O(n) but dictionary makes time complexity more complex
# O(n) + O(m) if we opt for an array as a dictionary where m is the value of the largest integer in the list
def better_two_sum(nums, target):
    numDictionary = {}
    for numIndex, num in enumerate(nums):
        difference = target-num
        if difference in numDictionary.keys():
            return [numDictionary[difference], numIndex]
        else:
            numDictionary[num] = numIndex

# Mostly an edge case: We can make potentially another version of a more efficient two_sum by sorting the list and slicing off numbers larger than target

if __name__ == '__main__':
    nums = [-3,4,3,90]
    target = 0
    print(better_two_sum(nums, target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

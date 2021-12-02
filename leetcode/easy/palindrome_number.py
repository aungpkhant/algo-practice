# To Clarify Edge cases - negative numbers
# -101
# Tricky inputs: 1,


def get_suffix_first_index(length: int) -> int:
    if length % 2 == 0:
        return int(length / 2)
    else:
        return int((length + 1) / 2)


def palindrome_number(num: int) -> bool:
    numInStringFormat = str(num)
    numSuffix = numInStringFormat[get_suffix_first_index(len(numInStringFormat)) :]
    numPrefix = numInStringFormat[0 : len(numInStringFormat) // 2][::-1]
    return numSuffix == numPrefix


if __name__ == "__main__":
    print(palindrome_number(1331))

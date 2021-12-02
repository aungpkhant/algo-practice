def naive_longest_common_prefix(strs) -> str:
    # Check for the 0 case
    if (len(strs)) == 0:
        return ""

    # Main logic here
    # Starting with index 0, check for letter at index 0 for each of the strings
    # If its the same go to index + 1
    # If not the same, return the first nth letters of any string
    longest_common_prefix = ""

    first_string_in_list = strs[0]

    for index, letter in enumerate(first_string_in_list):
        current_string_is_prefix = True

        # TODO optimize by not checking the first string later
        for string in strs:
            try:
                if string[index] != letter:
                    current_string_is_prefix = False
            except IndexError:
                current_string_is_prefix = False

        if current_string_is_prefix == False:
            return longest_common_prefix
        else:
            longest_common_prefix += letter

    return longest_common_prefix


def longest_common_prefix(strs):
    # Check for the 0 case
    if not strs:
        return ""

    shortest_string_in_list = min(strs, key=len)

    for index, letter in enumerate(shortest_string_in_list):
        for other_string in strs:
            if other_string[index] != letter:
                return shortest_string_in_list[:index]

    return shortest_string_in_list


if __name__ == "__main__":
    print(longest_common_prefix(["dog", "dogg", "dog3"]))

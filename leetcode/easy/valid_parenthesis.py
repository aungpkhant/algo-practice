bracket_map = {")": "(", "]": "[", "}": "{"}


def isValid(s: str) -> bool:
    if len(s) == 0:
        return True

    # Initialize stack
    stack = []

    # While string still has some characters in it,
    # Push to stack if any of (, [ or {
    # If any of ), ], }
    # Pop from stack and check if current brace type matches the popped brace type
    # If matches, continue,
    # If no match, return False
    while len(s) != 0:
        front_letter = s[0]
        s = s[1:]

        if front_letter in bracket_map.values():
            stack.append(front_letter)
        elif front_letter in bracket_map.keys():
            if len(stack) == 0:
                return False
            brace = stack.pop()
            # i should get an opening brace
            if bracket_map[front_letter] != brace:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    print(isValid("()[]][["))

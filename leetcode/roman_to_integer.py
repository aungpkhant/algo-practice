normal_numerals = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

edge_case_numerals = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}


def roman_to_integer(roman_numeral: str) -> int:
    # Edge case check for empty string
    if len(roman_numeral) == 0:
        raise Exception("Empty string input")

    parsed_numbers = []

    while len(roman_numeral) != 0:

        if roman_numeral[0:2] in edge_case_numerals.keys():
            parsed_numbers.append(edge_case_numerals[roman_numeral[0: 2]])
            roman_numeral = roman_numeral[2:]
        else:
            if roman_numeral[0: 1] in normal_numerals.keys():
                parsed_numbers.append(normal_numerals[roman_numeral[0: 1]])
                roman_numeral = roman_numeral[1:]
            else:
                raise Exception("Invalid letter in the roman numeral")

    # Return sum of array here
    return sum(parsed_numbers)


if __name__ == '__main__':
    print(roman_to_integer('MCMXCIV'))
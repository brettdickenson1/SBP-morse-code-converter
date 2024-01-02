inputText = input(f'Please enter string here:\n')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.']

# convertText = list(inputText)
# print(convertText)


# CHECK input letter and how many times its in list and which index its at
matched_indexes = []
i = 0
length = len(letters)


def check_values_in_string(input_string, values_array):
    for value in values_array:
        if value in input_string:
            # print(f'Index is {letters.index(value)}')
            indexVal = letters.index(value)
            # print(morse[indexVal])
            matched_indexes.append(morse[indexVal])
        # else:
        #     print(f"{value} is not present in the string.")


check_values_in_string(inputText, letters)

print(matched_indexes, 'MORSE CODE CONVERTED')

# while i < length:
#     if inputText == letters[i]:
#         matched_indexes.append(i)
#     i += 1

#     print(f'{inputText} is present in {letters} at indexes {matched_indexes}')

# #Convert array value to string
# turn_to_string = "''".join(str(x) for x in matched_indexes)

#Convert string to number
# print(morse[int(turn_to_string)])



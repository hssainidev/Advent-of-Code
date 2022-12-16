sum_of_priorities = 0
with open('input.txt', 'r', encoding='UTF-8') as input_file:
    lines = input_file.readlines()

    for line in lines:
        char_to_int = 0
        first_half, second_half = line[: len(line) // 2], line[len(line) // 2:]
        common_char = ''.join(set(first_half).intersection(second_half))

        char_to_int = (ord(common_char) - 96) if common_char.islower() else (ord(common_char) - 38)

        sum_of_priorities += char_to_int

print(sum_of_priorities)

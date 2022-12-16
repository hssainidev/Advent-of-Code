from itertools import islice

sum_of_priorities = 0
with open('input.txt', 'r', encoding='UTF-8') as input_file:
    while True:
        next_lines = list(islice(input_file, 3))
        if len(next_lines) < 3:
            break
        [first, second, third] = next_lines

        common_char = ''.join(set(first).intersection(second).intersection(third)).strip()

        char_to_int = (ord(common_char) - 96) if common_char.islower() else (ord(common_char) - 38)

        sum_of_priorities += char_to_int

print(sum_of_priorities)

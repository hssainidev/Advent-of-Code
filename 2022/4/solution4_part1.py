contains = 0
with open('4/input.txt', 'r', encoding='UTF-8') as input_file:
    lines = input_file.readlines()
    for line in lines:
        first_elf, second_elf = line.strip().split(',')
        first_elf_low, first_elf_high = map(int, first_elf.split('-'))
        second_elf_low, second_elf_high = map(int, second_elf.split('-'))
        if ((first_elf_low >= second_elf_low) and (first_elf_high <= second_elf_high)):
            contains += 1
        elif ((first_elf_low <= second_elf_low) and (first_elf_high >= second_elf_high)):
            contains += 1
print(contains)

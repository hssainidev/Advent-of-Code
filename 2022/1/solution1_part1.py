
maxCal = 0
with open('input.txt', 'r', encoding='UTF-8') as input_file:
    currentCal = 0
    lines = input_file.readlines()
    for line in lines:
        if line.isspace():
            if currentCal > maxCal:
                maxCal = currentCal
            currentCal = 0
        else:
            currentCal = currentCal + int(line)

print(maxCal)

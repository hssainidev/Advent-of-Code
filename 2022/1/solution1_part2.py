
maxCal = [0]*3
with open('input.txt', 'r', encoding='UTF-8') as input_file:
    currentCal = 0
    lines = input_file.readlines()
    for line in lines:
        if line.isspace():
            for i in range(len(maxCal)):
                if currentCal > maxCal[i]:
                    maxCal.insert(i, currentCal)
                    maxCal.pop()
                    currentCal = 0
            currentCal = 0
        else:
            currentCal = currentCal + int(line)
print(sum(maxCal))

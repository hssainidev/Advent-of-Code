import re

if __name__ == '__main__':
    sum_mul = 0
    do_sum = True
    with open(r"input.txt", "r") as infile:
        for line in infile:
            mem_tuple = re.finditer("do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)", line)
            for x in mem_tuple:
                match x.group():
                    case 'do()':
                        do_sum = True
                    case 'don\'t()':
                        do_sum = False
                    case _:
                        if do_sum:
                            sum_mul += int(x[1]) * int(x[2])

    print(sum_mul)

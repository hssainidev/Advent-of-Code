import re

if __name__ == '__main__':
    with open(r"input.txt", "r") as infile:
        print(sum(
            sum(int(mul[0]) * int(mul[1]) for mul in (re.findall("mul\((\d{1,3}),(\d{1,3})\)", line))) for line in
            infile))

# if __name__ == '__main__':
#     sum_mul = 0
#     with open(r"input.txt", "r") as infile:
#         for line in infile:
#             mem_tuple = re.findall("mul\((\d{1,3}),(\d{1,3})\)", line)
#             print(mem_tuple)
#             for x, y in mem_tuple:
#                 print(x,y)
#                 sum_mul += int(x) * int(y)
#
#     print(sum_mul)
#     182619815

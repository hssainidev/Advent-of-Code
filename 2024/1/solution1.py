import bisect

distance = 0
left_list = []
right_list = []


def insert_in_sorted_order(lst, num):
    bisect.insort(lst, int(num))


with open(r"input.txt", "r") as infile:
    for line in infile:
        split_nums = line.split()
        insert_in_sorted_order(left_list, split_nums[0])
        insert_in_sorted_order(right_list, split_nums[1])

for idx, item in enumerate(left_list):
    if left_list[idx] > right_list[idx]:
        distance += left_list[idx] - right_list[idx]
    else:
        distance += right_list[idx] - left_list[idx]

    print(distance)

print("distance is: {0}".format(distance))

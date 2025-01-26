import bisect

similarity_score = 0
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
    occurrence = right_list.count(left_list[idx])
    similarity_score += (left_list[idx] * occurrence)
    print(similarity_score)

print("similarity_score is: {0}".format(similarity_score))




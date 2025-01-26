safe_count = []


def check_if_safe(left_num, right_num, inc_dec, is_first):
    if left_num > right_num:
        order = 'decreasing'
        if (is_first == 0 or (is_first != 0 and inc_dec == order)) and left_num - right_num <= 3:
            return True, order
        else:
            return False, ''
    elif left_num < right_num:
        order = 'increasing'
        if (is_first == 0 or (is_first != 0 and inc_dec == order)) and right_num - left_num <= 3:
            return True, order
        else:
            return False, ''
    else:
        return False, ''


def check_safe(levels):
    increasing_decreasing = ''
    safe = None
    for idx in range(len(levels) - 1):
        safe, increasing_decreasing = check_if_safe(int(levels[idx]), int(levels[idx + 1]),
                                                    increasing_decreasing, int(idx))
        # print(levels[idx], levels[idx + 1], increasing_decreasing, safe)
        if not safe:
            return False
    return safe


with open(r"input.txt", "r") as infile:
    for line in infile:
        split_levels = line.split()
        safe_or_not = check_safe(split_levels)
        safe_count.append(safe_or_not)

print(safe_count.count(True))
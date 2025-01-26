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
    curr_idx = 0
    safe = None
    for idx in range(len(levels) - 1):
        safe, increasing_decreasing = check_if_safe(int(levels[idx]), int(levels[idx + 1]), increasing_decreasing,
                                                    int(idx))
        if not safe:
            return False, idx + 1, True
    return safe, curr_idx, False


def check_fault(arg_arr):
    global safe_or_not
    fault_counter = 0
    single_fault = False
    safe_or_not, index, single_fault = check_safe(arg_arr)
    if single_fault:
        fault_counter += 1
    if not safe_or_not and fault_counter == 1:
        popped = arg_arr[:index - 1] + arg_arr[index:]
        safe_or_not, *rest = check_safe(popped)
        if index < len(arg_arr):
            popped = arg_arr[:index] + arg_arr[index + 1:]
            safe_or_not = safe_or_not or check_safe(popped)[0]
    return safe_or_not

if __name__ == '__main__':
    with open(r"input.txt", "r") as infile:
        for line in infile:
            split_levels = line.split()
            safe_or_not = check_fault(split_levels)
            if not safe_or_not:
                safe_or_not = check_fault(list(reversed(split_levels)))
            safe_count.append(safe_or_not)

    print(safe_count.count(True))

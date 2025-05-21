import re
import time


def check_order(order):
    in_order = True
    for x in range(len(order), 0, -1):
        if not in_order:
            break
        if order[x:]:
            for y in order[x:]:
                if y in page_orders.get(order[x - 1:x][0]):
                    in_order = True
                else:
                    order.insert(x - 1, order.pop(order.index(y)))
                    check_order(order)
    return in_order


if __name__ == '__main__':
    start_time = time.time()
    page_orders = {}
    middle_page = 0
    with open(r"input.txt", "r") as infile:
        for line in infile:
            mem_tuple = re.findall("(\d{2})\|(\d{2})", line)
            if mem_tuple:
                # print(mem_tuple[0][0])
                if mem_tuple[0][0] not in page_orders:
                    page_orders[mem_tuple[0][0]] = [mem_tuple[0][1]]
                else:
                    page_orders.get(mem_tuple[0][0]).append(mem_tuple[0][1])
            elif not re.match("^\s*$", line):
                update_order = line.strip().split(',')
                result = check_order(update_order)

                if result:
                    middle_page += int(update_order[len(update_order) // 2])

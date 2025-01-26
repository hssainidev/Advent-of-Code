import re

contains = 0


def create_stacks(stack_str):
    *crates, stack_num = stack_str.split('\n')
    number_of_stacks = len(stack_num.split())
    stacks = [[] for _ in range(number_of_stacks)]
    crates.reverse()
    for line in crates:
        for stack_idx, i in enumerate(range(1, len(crates[0]), 4)):
            if line[i].strip():
                stacks[stack_idx].append(line[i])
    return stacks


with open('input.txt', 'r', encoding='UTF-8') as input_file:
    stack_str, procedures = input_file.read().split('\n\n')
    stacks = create_stacks(stack_str)
    print(stacks)
    for procedure in procedures.split('\n'):
        if str(procedure).strip():
            move_crates, from_stack, to_stack = map(int, re.findall(r"\d+", procedure))
            print(f"{move_crates=}, {from_stack=}, {to_stack=}")
            for _ in range(move_crates):
                print(f"{len(stacks[from_stack-1])=}, {len(stacks[to_stack-1])=}")
                stacks[to_stack-1].append(stacks[from_stack-1].pop())
    [print(stack[-1], end="") for stack in stacks]

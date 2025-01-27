from collections import defaultdict

if __name__ == '__main__':

    make_grid = defaultdict(str) | {(i, j): c for i, r in enumerate(open('input.txt')) for j, c in enumerate(r)}
    get_coord = list(make_grid.keys())
    diagonal = -1, 0, 1
    xmas_counter = 0

    T = list('MAS'), list('SAM')

    for i, j in get_coord:
        if [make_grid[i + d, j + d] for d in diagonal] in T and [make_grid[i + d, j - d] for d in diagonal] in T:
            xmas_counter += 1

    print(xmas_counter)

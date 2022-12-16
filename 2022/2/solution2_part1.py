encrypted_strategy_guide = {'A': "rock", 'X': "rock", 'B': "paper", 'Y': "paper", 'C': "scissor", 'Z': "scissor"}

winners = {"rock": "scissor", "paper": "rock", "scissor": "paper"}

shape_points = {"rock": 1, "paper": 2, "scissor": 3}

outcome_points = {"loss": 0, "draw": 3, "win": 6}

grand_total_points = 0


def get_outcome_points(real_opponent_shape):
    if winners[real_opponent_shape] == real_my_pick:
        outcome = "loss"
        points_this_round = outcome_points[outcome]
        pass
    elif real_opponent_shape == real_my_pick:
        outcome = "draw"
        points_this_round = outcome_points[outcome]
    else:
        outcome = "win"
        points_this_round = outcome_points[outcome]
    return points_this_round


with open('input.txt', 'r', encoding='UTF-8') as input_file:
    lines = input_file.readlines()
    for line in lines:
        opponent_pick, my_pick = line.split()
        real_opponent_pick = encrypted_strategy_guide[opponent_pick]
        real_my_pick = encrypted_strategy_guide[my_pick]

        shape_points_this_round = shape_points[real_my_pick]
        outcome_points_this_round = get_outcome_points(real_opponent_pick)

        total_points_this_round = shape_points_this_round + outcome_points_this_round
        grand_total_points += total_points_this_round

print(grand_total_points)

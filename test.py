import itertools

game_rule_win_set = [[1, 2, 3], [4, 5, 6], [7, 8, 9], #Horizontal Set
					 [1, 4, 7], [2, 5, 8], [3, 6, 9], #Vertical Set
					 [1, 5, 9], [3, 5, 7]] #Diagonal Set

all_game_rule_win_set = [list(itertools.permutations(i)) for i in game_rule_win_set]
print all_game_rule_win_set

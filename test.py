# import itertools

# game_rule_win_set = [[1, 2, 3], [4, 5, 6], [7, 8, 9], #Horizontal Set
# 					 [1, 4, 7], [2, 5, 8], [3, 6, 9], #Vertical Set
# 					 [1, 5, 9], [3, 5, 7]] #Diagonal Set

# all_game_rule_win_set = [list(itertools.permutations(i)) for i in game_rule_win_set]
# print all_game_rule_win_set


a = [3, 5, 7]
game_rule_win_set = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1], 
					 [4, 5, 6], [4, 6, 5], [5, 4, 6], [5, 6, 4], [6, 4, 5], [6, 5, 4], 
					 [7, 8, 9], [7, 9, 8], [8, 7, 9], [8, 9, 7], [9, 7, 8], [9, 8, 7], 
					 [1, 4, 7], [1, 7, 4], [4, 1, 7], [4, 7, 1], [7, 1, 4], [7, 4, 1], 
					 [2, 5, 8], [2, 8, 5], [5, 2, 8], [5, 8, 2], [8, 2, 5], [8, 5, 2], 
					 [3, 6, 9], [3, 9, 6], [6, 3, 9], [6, 9, 3], [9, 3, 6], [9, 6, 3], 
					 [1, 5, 9], [1, 9, 5], [5, 1, 9], [5, 9, 1], [9, 1, 5], [9, 5, 1], 
					 [3, 5, 7], [3, 7, 5], [5, 3, 7], [5, 7, 3], [7, 3, 5], [7, 5, 3]]			

print a
print game_rule_win_set
print a in game_rule_win_set					
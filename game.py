#!/usr/bin/python
import sys
import itertools

####
# game_rule_win_set = [[1, 2, 3], [4, 5, 6], [7, 8, 9], #Horizontal Set
# 					 [1, 4, 7], [2, 5, 8], [3, 6, 9], #Vertical Set
# 					 [1, 5, 9], [3, 5, 7]] #Diagonal Set
game_rule_win_set = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1], 
					 [4, 5, 6], [4, 6, 5], [5, 4, 6], [5, 6, 4], [6, 4, 5], [6, 5, 4], 
					 [7, 8, 9], [7, 9, 8], [8, 7, 9], [8, 9, 7], [9, 7, 8], [9, 8, 7], 
					 [1, 4, 7], [1, 7, 4], [4, 1, 7], [4, 7, 1], [7, 1, 4], [7, 4, 1], 
					 [2, 5, 8], [2, 8, 5], [5, 2, 8], [5, 8, 2], [8, 2, 5], [8, 5, 2], 
					 [3, 6, 9], [3, 9, 6], [6, 3, 9], [6, 9, 3], [9, 3, 6], [9, 6, 3], 
					 [1, 5, 9], [1, 9, 5], [5, 1, 9], [5, 9, 1], [9, 1, 5], [9, 5, 1], 
					 [3, 5, 7], [3, 7, 5], [5, 3, 7], [5, 7, 3], [7, 3, 5], [7, 5, 3]]			

# all_game_rule_win_set = [list(itertools.permutations(for i in game_rule_win_set))]
o_player = []
x_player = []
#x player = 0 o player = 1
player_turn = itertools.cycle(range(2))
board = []

def check_game_rule(player_list):
	if len(player_list) >= 3:
		for i in itertools.combinations(player_list, 3):
			if list(i) in game_rule_win_set:
				return True
	return False

def check_piece_exist(squre_position):
	if squre_position in board:
		return True
	else: 
		return False

def check_grid(squre_number):
	if squre_number in o_player:
		return "O"
	elif squre_number in x_player:
		return "X"
	else:
		return " "

def print_board():
	print("----BOARD----")
	print "| {0} | {1} | {2} |".format(check_grid(1), check_grid(2), check_grid(3))
	print("-------------")
	print "| {0} | {1} | {2} |".format(check_grid(4), check_grid(5), check_grid(6))
	print("-------------")
	print "| {0} | {1} | {2} |".format(check_grid(7), check_grid(8), check_grid(9))
	print("-------------")
	print("O Player: ", o_player)
	print("X Player: ", x_player)
	return

# print("####SYSTEM VERSION####")
# print(sys.version)
# print("######################")

print("Game Start.");
while len(board) < 9:
	#check player turn
	if player_turn.next() == 0:
		#turn player X
		i = int(raw_input("X turn: "))
		if check_piece_exist(i):
			print "Error: this position grid have already piece."
			player_turn.next() #flip player turn again
			continue
		o_player.append(i)
	else:
		#Turn player O
		i = int(raw_input("Y turn: "))
		if check_piece_exist(i):
			print "Error: this position grid have already piece."
			player_turn.next() #flip player turn again
			continue
		x_player.append(i)

	board.append(i)
	# Display Board
	# [1, 2, 3]
	# [4, 5, 6]
	# [7, 8, 9]
	################
	print_board()
	if check_game_rule(o_player): 
		print "O Player win this game."
		break
	if check_game_rule(x_player):
		print "X Player win this game."
		break

print("End Game.")
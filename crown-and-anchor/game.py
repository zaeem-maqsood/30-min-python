


def check_symbol(randomly_chosen_symbols, symbol, bet):

	counter = 0
	for random_symbol in randomly_chosen_symbols:
		if symbol == random_symbol:
			counter += 1

	return counter 




def place_bet_and_check_for_win(randomly_chosen_symbols, symbol, money_available):

	increments = [0, 1, 2, 5, 10]
	money_gained = 0
	money_gained_and_bet_dict = {}
	
	bet = -1
	while bet == -1:
		bet = input("How much would you like to bet on {0}s? (You have ${1} left) :".format(symbol, money_available))

		try:
			bet = int(bet)
			if bet not in increments:
				print("Please place a bet of either $0, $1, $2, $5 or $10")
				bet = -1
			else:
				if bet > money_available:
					print("You do not have enough money to bet that much, your available funds are {0}".format(money_available))
					bet = -1
				else:
					check = check_symbol(randomly_chosen_symbols, symbol, bet)
					if check == 0:
						money_gained = 0
					elif check == 1:
						money_gained = (check * bet) 
					elif check == 2:
						money_gained = (check * bet) 
					else:
						if symbol == "anchor":
							print("Winner on Anchors -- Ahoy !!!!")
						money_gained = (check * bet) 
		

		except Exception as e:
			print(e)
			print("{0} is not an integer, please enter an integer.".format(bet))
			bet = -1

	money_gained_and_bet_dict["money_gained"] = money_gained
	money_gained_and_bet_dict["bet"] = bet
	return money_gained_and_bet_dict



def update_money_for_player(symbols, randomly_chosen_symbols, money_available):

	print("You have ${0} available!".format(money_available))
	print("Remember you can bet in increments of $1, $2, %5 or $10 for each symbol or bet $0 for nothing\n")

	money_gained = 0

	for symbol in symbols:
		if money_available > 0:
			money_gained_and_bet = place_bet_and_check_for_win(randomly_chosen_symbols, symbol, money_available)
			money_available = money_available - money_gained_and_bet["bet"]
			money_gained = money_gained + money_gained_and_bet["money_gained"]


	return money_gained







def generate_symbols(symbols):
	
	randomly_chosen_symbols = []

	from random import randint
	for symbol in range(3):
		symbol = symbols[randint(0, 5)]
		randomly_chosen_symbols.append(symbol)

	return randomly_chosen_symbols





def game(players):

	symbols = ["heart", "spade", "diamond", "club", "crown", "anchor"]
	total_sum = players * 10
	player_money = []
	game_round = 0

	# Fill the players available money with 10$ each
	for player in range(players):
		player_money.append(10)
	
	# Start the cycling process until the total sum of money equals 0
	while total_sum != 0:

		game_round += 1
		randomly_chosen_symbols = generate_symbols(symbols)

		print("Round {0}\n".format(game_round))

		for player in range(players):
			print("Player {0}".format(player+1))
			money_available = player_money[player]
			player_money[player] =  update_money_for_player(symbols, randomly_chosen_symbols, money_available)
			print("\n")
			
		
		with open("output.txt", "a") as text_file:
			print("Round {0}".format(game_round), file=text_file)
			for player in range(players):
				print("Player {0} ${1}".format(player+1, player_money[player]), file=text_file)
			print("\n", file=text_file)


		
		print("The winning slot was {0}".format(randomly_chosen_symbols))
		for player in range(players):
			print("Player {0} won ${1}".format(player+1, player_money[player]))
		print("\n-------------------------------------------------------")

		
		total_sum = sum(player_money)






def main():

	print("Welcome to Crown and Anchor!")

	players = 0
	# Do a quick check to make sure the user has entered an integer
	while players == 0:
		players = input("Players :")

		try:
			players = int(players)
		except:
			print("{0} is not an integer, please enter an integer.".format(players))
			players = 0

	
	print("\n-------------------------------------------------------")
	# Start the game
	game(players)



main()
	
	

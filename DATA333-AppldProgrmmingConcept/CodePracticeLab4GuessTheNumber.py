import random
import os

# Use OS-level entropy to generate a random seed
# More randomer then a static seed or time
random.seed(int.from_bytes(os.urandom(8), 'big'))

# The Great Zulton
guessmaster = r"""
                 0                 
________________/?\________________
|  ___________ /???\___________   |
|  |          /?????\          |  |
|  |         /???????\         |  |
|  |        /?????????\        |  |
|  |       /___________\       |  |
|  |        /         \        |  |
|  |       |   @   @   |       |  |
|  |  (    |     <     |       |  |
|  | ( )   \   _____   /       |  |
|  |  Y     \  \___/  /        |  |
|  | |"|    __|_____|__        |  |
|  | | |   / /       \ \    __ |  |
|  | | |  /___       ___\   || |  |
|  |_| |_/____{&%%&}_____\_(__)|  |
|  |_'-'_______________________|  |
|                                 |
|  |=-=-=-=-=-=-=-=-=-=-=-=-=-=|  |
|  |    ╔════════════════╗     |  |
|  |    ║Guess the number║     |  |
|  |    ╚════════════════╝     |  |
|  |                           |  |
|__|=-=-=-=-=-=-=-=-=-=-=-=-=-=|__|
"""



victory = r"""
         \         .  ./
       \      .:";'.:.."   /
           (M^^.^~~:.'").
     -   (/  .    . . \ \)  -
        ((| :. ~ ^  :. .|))
     -   (\- |  \ /  |  /)  -
          -\  \     /  /-
____________\  \   /  /_______

Congrats You Overloaded The great Zulton and saved The world!
"""
# Variable settings for difficulty
difficulty={
	"difficulty0":"Easy",
	"difficulty1":"Moderate",
	"difficulty2":"Hard",
	"range0":"1 - 10",
	"range1":"1 - 100",
	"range2":"1 - 1000",
	"guess0":5,
	"guess1":8,
	"guess2":10
}
#easy = range of 1 to 10, limit tries to 5.1
#moderate = range of 1 to 100, limit tries to 8.
#hard = range of 1 to 1000, limit tries to 10.
difficultyTable = f"""
+------------+------------+------------|
|           Difficulty Stats           |
+------------+------------+------------+
|{"Difficulty":^12}|{"Range":^12}|{"Gusses":^12}|
+------------+------------+------------+
|{difficulty["difficulty0"]:^12}|  {difficulty["range0"]:<10}|{difficulty["guess0"]:^12}|
|{difficulty["difficulty1"]:^12}|  {difficulty["range1"]:<10}|{difficulty["guess1"]:^12}|
|{difficulty["difficulty2"]:^12}|  {difficulty["range2"]:<10}|{difficulty["guess2"]:^12}| 
|------------+------------+------------|

"""
#Inside this function, keep track of the wins and losses for the player (using global variables), displaying the score before asking if they would like to play again.

gamestats={
	"gamer":"gayer",
	"wins":0,
	"losses":0,
	"difficulity":"",
	"round":0,
	"guesses":0,
	"range":range(1, 2),
	"trange":""
}
def round():
	gamestats["round"]+= 1
	number = random.randint(*gamestats["range"])
	print(guessmaster)
	for i in range(1, gamestats['guesses'] + 1):
		print(f"{gamestats['gamer']}: Round#{gamestats['round']} Guess: {i} of {gamestats['guesses']} Wins:{gamestats['wins']} Looses:{gamestats['losses']}")
		while True:
			try:
				guess = int(input(f"{gamestats['gamer']}, What number from {gamestats['trange']} is the Great Zulton Thinking of? "))
				break
			except ValueError:
				print("Not a valid number")
				continue
		if guess == number:
			gamestats['wins'] += 1
			print("Correct! The Great Zulton Knew you could do it!")
			return
		else:
			print("Wrong!")
	gamestats['losses'] += 1
	print(f"Game over {gamestats['gamer']}!") #If the player doesn't guess the number in the required amount of tries, they lose the game.
	return

	

#Define a function that can be reused later. 
def main():
	print("Welcome to the totally new and orginal hit game.")
	print("Guess The Number!")
	gamestats["gamer"] = input("Enter your gamer tag: ")#Inside this function, ask for the player's name. Output their name at least once.

	while True:
			print(difficultyTable)
			#Inside this function, ask players if they would like to play an EASY, MODERATE, or HARD game.
			print(f"{gamestats['gamer']}, select your difficulity!")
			while True:
				choice = input("Enter: Easy, Moderate, or Hard: ").lower()
				if choice in ("easy", "e"):
					gamestats.update({"difficulity": "Easy", "guesses": 5, "range":(1,10),"trange":"1 to 10"})
					round()
					break
				elif choice in ("moderate", "m"):
					gamestats.update({"difficulity": "Moderate", "guesses": 8, "range":(1,100),"trange":"1 to 100"})
					round()
					break
				elif choice in ("hard", "h"):
					gamestats.update({"difficulity": "Hard", "guesses": 10, "range":(1,1000),"trange":"1 to 1000"})
					round()
					break		
				else:
					print("Sorry that's not a valid choice")
			print(f"{gamestats['gamer']}: Round#{gamestats['round']} Wins:{gamestats['wins']} Looses:{gamestats['losses']}" )
			if gamestats['wins'] >= 1000: print(victory); break 
			while True:
				choice = input("Would you Like to try your luck again? Yes or No: ").lower()
				if choice in ("yes", "y"):
					break
				elif choice in ("no", "n"):
					print("Goodbye!")
					exit()
				else:
					print("Sorry that's not a valid choice")
	return

if __name__ == "__main__":
	while True:
		main()


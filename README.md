# blackjack
Developed by: Tony Rahman
Site: http://flyingsalmon.net/?tag=stem
Purpose: STEM - educational purpose

Overview:
 This is a one-player Blackjack game (playing against a non-human Dealer) simulating common rules of Casino Blackjack in the USA.
 The code is shared under the licensing term as listed. This is all Python 3.x code and has been tested on Windows although it should work on other platforms.
 It can also be made into a self-executable (and tested on Windows). 
 The code is written for a terminal/shell playable text-based application with Unicode symbols support, but it can be easily modified to be made into a GUI application using this core game logic.

 All blackjack tables will have minimum and maximum betting limits. 
 100 coins start.
 20 coins each bet.
 When a player (you) wins: you get +20 coins. If player loses, 20 coins are deducted.
 Game is over when there less than coins required for a bet (20 for example).
 
Blackjack basic rules:
 The aim of blackjack is to get as close as possible to 21 points without exceeding 21.
 The points are the same as the numbers on the cards with picture cards (Jack, Queen, King) being worth 10 points each and the Ace counting as either 1 or 11. In reality, this is decided by the player, but in this version, it's already decided for the player by the code by drawing an Ace of cards of two kinds (worth 1 point or 11 points).
 
 Each player gets 2 cards initially (face up). And the dealer gets 1 card (face up). The player decides on Hit/Stand. Hit means, player will be dealt one more random card from the deck. At which point player will have to decide again if s/he wantso Hit or Stand...unless the player goes BUST...meaning the total points of the player's hand is greater than 21 points, or the dealer's hand is exactly 21 (Blackjack!). 
 Once the player decides to Stand, meaning, "don't give me any more cards...I'm good with what I have. Let's see yours!", the dealer (computer) will keep drawing cards for itself until the points are AT LEAST worth 17 points. Which means dealer can get 17 or higher points before the round is decided. At which point, the scores are compared between dealer and player.
 
 One deck or two decks can be used for the game. In this game, you can imagine more than 1 deck as the same card suit and number may pop up in the same round.
 
 Win Conditions (for each round):
 If Player points are:
	Greater than 21 -> player is BUST! (dealer wins)
	Exactly =21 player wins. BLACKJACK!
	Less than 21 give Option: Hit or Stand
 		If Hit: pick 1 more rand card and add its points to current total points for player
		If Stand: Dealer gets additional cards for itself (until total points for itself is >=17 points) and then compare player's and dealer's points

	Less than Dealer's points AND Player points is less than 21 OR greater than 21) then Dealer wins.
	Greater than Dealer's points AND Player points is less than or equal to 21 then Player wins.


 If Dealer's points are:
	Greater than 21 -> dealer is BUST (you win)
      	Exactly =21 AND Player points is less than 21 OR greater than 21, Dealer wins! BLACKJACK!


 Tie Condition (for each round):
	If Player's point is same as Dealer's AND Player's score is less than 21, it's a tie, or called a PUSH. A PUSH means the player doesn't win or lose the betted coins for that round and continues to next round.
 
 GAME OVER Condition: How many rounds total?
 	Each round is over after checking the above Win conditions, and if there are chips left to bet for the next round for the player, the game continues. User can also Quit ('Q' key) anytime.
 
 Other notes:
 Because it's a text-based keyboard UI game, the code also verifies if correct command was given (H or S or Q keys on keyboard) and if not, it'll continue to ask for a valid input.
 It's worth noting and critical in coding that there are multiple loop conditions within each round depending on user commands (Hit or Stand) and Blackjack, and also the rule for drawing cards WITHIN each round is different from rules for drawing cars for a new round! 
 
Game Audio:
 Audio effects are used (WAV format). You may not reuse the audio or other assets without getting explicit permissions from the sources.

Game Visual:
 Some Unicode (UTF-8) characters are used for cards suit depiction and other prompts. Most of them work fine although in Windows CMD shell, Python apparently gets confused with certain symbols and therefore may appear as a '?' in a box, however, this will not affect the playability as the suit symbols and points still show correctly. The game is console based.


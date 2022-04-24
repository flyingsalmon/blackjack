def PromptUserForAction():
    # Called from: main
    # Calls: none
    # Returns: user input as a string to main
    
    inp=""
    while (inp not in "SHQ" or len(inp)<1):
        inp = input("\nYOUR TURN! Give a command: Stand (S), Hit or Deal (H), Quit (Q)> ").upper()
    
    return inp
    

def GetTwoCardsForPlayer():
    # Called by: main
    # Calls: none
    # Returns: nothing (updates global vars)
    # Updates global vars: player cards array, player suits array, player score, displays cards drawn.
    
    global g_player_score, g_player_cards, g_player_suits, g_deck, g_suits

    # For each NEW round: Always pick 2 cards for player:
    winsound.PlaySound(g_WAVcardsdraw, winsound.SND_FILENAME)
    while len(g_player_cards) <2:
        card=random.choice(g_deck)
        g_player_cards.append(card)
        suit=random.choice(g_suits)
        g_player_suits.append(suit)
        if (card ==1 or card==11):
            cardfullname="Ace of " + suit
            print("\t> You got:", cardfullname)   
        else:
            cardfullname=str(card) + " of " + suit
            print("\t> You got:", cardfullname)
    

    g_player_score=sum(g_player_cards)


def GetOneCardForDealer():
    # Called by: main
    # Calls: none
    # Returns: nothing (updates global vars)
    # Updates global vars: dealer cards array, dealer score, displays card drawn for dealer
    
    global g_dealer_score, g_dealer_cards, g_dealer_suits, g_deck, g_suits

    winsound.PlaySound(g_WAVcardsdraw, winsound.SND_FILENAME)
    card=random.choice(g_deck) 
    g_dealer_cards.append(card)
    suit=random.choice(g_suits)
    g_dealer_suits.append(suit)
    if (card ==1 or card==11):
        cardfullname="Ace of " + suit
        print("\t< Dealer got:", cardfullname)
    else:
        cardfullname=str(card) + " of " + suit
        print("\t< Dealer got: ", cardfullname)
    
    g_dealer_score=sum(g_dealer_cards)


def GetRemainingDealerCards():
    # Called by: main
    # Calls: none
    # Returns: nothing (updates global vars)

    global g_dealer_score, g_dealer_cards, g_deck, g_suits, g_dealer_suits
    
    winsound.PlaySound(g_WAVcardsdraw, winsound.SND_FILENAME) #SND
    
    while g_dealer_score <=17:
        card=random.choice(g_deck) 
        g_dealer_cards.append(card)
        suit=random.choice(g_suits)
        g_dealer_suits.append(suit)
        if (card !=1):            
            print("\t<< Dealer got", card, "of", suit)
            if (DEBUG): print("GDs():")            
        else:
            print("\t<< Dealer got Ace of", suit)
            if (DEBUG): print("GDs():")
            
        g_dealer_score=sum(g_dealer_cards) 
        


def CheckForBlackjack():
    # Called by: main after each draw of card (but during the round is ongoing...e.g. player has NOT done Stand yet but Hitting).
    # Calls: RoundOver()
    # Returns: nothing (updates global vars)
    
    global g_dealer_score, g_player_score, g_available_chips, g_MINIMUMBET
    
    if (DEBUG): print("CBJ() ROUND", g_roundnumber, "RUNNING SCORE", g_THINARROW, "PLAYER:", g_player_score, "| DEALER:", g_dealer_score, "| CHIPS LEFT:", g_available_chips)
    else: print("ROUND", g_roundnumber, "RUNNING SCORE", g_THINARROW, "PLAYER:", g_player_score, "| DEALER:", g_dealer_score, "| CHIPS LEFT:", g_available_chips)
           
    if (g_dealer_score > 21):
        g_available_chips= g_available_chips + g_MINIMUMBET
        winsound.PlaySound(g_WAVwinround, winsound.SND_FILENAME)
        RoundOver('Player!', "Dealer went BUST!")
    elif (g_dealer_score == 21 and g_player_score!= 21):
        g_available_chips= g_available_chips - g_MINIMUMBET
        winsound.PlaySound(g_WAVgameover, winsound.SND_FILENAME)
        RoundOver('Dealer', "Dealer has BlackJack!")

    elif (g_player_score >21):
        g_available_chips= g_available_chips - g_MINIMUMBET 
        winsound.PlaySound(g_WAVgameover, winsound.SND_FILENAME) 
        RoundOver('Dealer', "You are BUST!")

    elif (g_player_score ==21):
        g_available_chips= g_available_chips + g_MINIMUMBET 
        winsound.PlaySound(g_WAVwinround, winsound.SND_FILENAME) 
        RoundOver('Player', "You got BlackJack!")        

    else: 
        return

   

def CheckWinner():
    # Called from: main ONLY after player Stands (S) so dealer draws the remaining cards to decide the winner of the round.
    # Calls: RoundOver()
    # Returns: nothing (updates global vars)    
    # Checks who won the round or draw, and updates available chips, and round number.
    # This does not calculate or update scores.
    # This should be called only when ending the round with a decision.
    
    global g_dealer_score, g_player_score, g_available_chips, g_MINIMUMBET
    
    if (DEBUG): print("CW() ROUND:", g_roundnumber, "RUNNING SCORE", g_THINARROW, "PLAYER:", g_player_score, "| DEALER:", g_dealer_score, "| CHIPS LEFT:", g_available_chips)
    else: print("ROUND:", g_roundnumber, "RUNNING SCORE", g_THINARROW, "PLAYER:", g_player_score, "| DEALER:", g_dealer_score, "| CHIPS LEFT:", g_available_chips)
           
    
    if (g_dealer_score > 21):
        g_available_chips= g_available_chips + g_MINIMUMBET
        winsound.PlaySound(g_WAVwinround, winsound.SND_FILENAME) 
        RoundOver('Player!', "Dealer went BUST!")
    elif (g_dealer_score == 21 and g_player_score!= 21): 
        g_available_chips= g_available_chips - g_MINIMUMBET 
        winsound.PlaySound(g_WAVgameover, winsound.SND_FILENAME)
        RoundOver('Dealer', "Dealer has BlackJack!")
    elif (g_dealer_score==g_player_score): 
        winsound.PlaySound(g_WAVnotification, winsound.SND_FILENAME) 
        RoundOver('X', "It's a PUSH (tie)!") 
    elif (g_dealer_score > g_player_score): 
        g_available_chips= g_available_chips - g_MINIMUMBET 
        winsound.PlaySound(g_WAVgameover, winsound.SND_FILENAME) 
        RoundOver('Dealer', "Dealer scored higher.")        
    elif (g_player_score ==21):
        g_available_chips= g_available_chips + g_MINIMUMBET 
        winsound.PlaySound(g_WAVwinround, winsound.SND_FILENAME)
        RoundOver('Player', "You got BlackJack!")        
    elif (g_player_score >21):
        g_available_chips= g_available_chips - g_MINIMUMBET 
        winsound.PlaySound(g_WAVgameover, winsound.SND_FILENAME) 
        RoundOver('Dealer', "You are BUST!")
    elif (g_player_score > g_dealer_score): 
        g_available_chips= g_available_chips + g_MINIMUMBET 
        winsound.PlaySound(g_WAVwinround, winsound.SND_FILENAME) 
        RoundOver('Player', "You scored higher.")                
    else: 
        return


def RoundOver(winner, reason=""):
    # Called by: CheckWinner()...this simply prints the results passed to it by CheckWinner().
    # Calls: none
    # Returns: nothing (updates global vars)
    global g_player_score, g_dealer_score, g_player_cards, g_dealer_cards, g_player_suits, g_dealer_suits, g_available_chips
    global g_BIGARROW, g_THINARROW, g_roundnumber, g_roundover
    
    winsound.PlaySound(g_WAVroundover, winsound.SND_FILENAME)
    
    g_roundnumber = g_roundnumber +1
    
    if (DEBUG): print("RO() *** ROUND OVER!***")
    else:print("*** ROUND OVER!***")
        
    g_roundover=True 

    if (winner.upper()=='X'):
        print('\t', g_BIGARROW, 'Draw!', reason)        
    else: 
        print("\t", g_BIGARROW, "Winner:", winner, "Dealer score:", g_dealer_score, "Your score:", g_player_score, "REASON:", reason)
        print('\t', g_THINARROW, 'Chips available:', g_available_chips)        
    
    g_player_score=0 
    g_dealer_score=0
    g_player_cards.clear() 
    g_dealer_cards.clear()
    g_player_suits.clear()
    g_dealer_suits.clear()
        
# end RoundOver

def GameOver(winner, reason=""):
    # Called by: main
    # Calls: none
    # Returns: nothing (updates global vars)
        
    global g_roundnumber    
    winsound.PlaySound(g_WAVgameover, winsound.SND_FILENAME) 
        
    if (winner.upper()=='Q'):
        print("GAME OVER! REASON:", reason)        
    elif (winner.upper()=='Z'):
        print("GAME OVER! REASON:", reason)
    else: # should not get here
        print("Unexpected event! REASON:", reason)

    print("\tYou played", g_roundnumber, "rounds.")
    g_roundnumber=1 
    
    exit()
    
# =====main driver=====
import random
import os  
os.system("") 
import winsound 
from sys import exit

# global vars
DEBUG=False
g_deck=[1,2,3,4,5,6,7,8,9,10,10,10,10,11] # Ace is either 1 or 11. J,Q,K are 10 + there's a number 10 card
g_suits=['\u2665 [Hearts]', '\u2666 [Diamonds]', '\u2660 [Spades]', '\u2663 [Clubs]']
g_available_chips=g_STARTINGCHIPS=100
g_MINIMUMBET=20 # each bet/round is 20 chips
g_dealer_score=0
g_player_score=0
g_roundnumber=1 # start at 1
g_roundover=False

g_BIGARROW ='\u1405' # unicode for ᐅ symbol. May or may not show properly when running as an EXE on Windows.
g_THINARROW ='\u21FE' # # unicode for ⇾ symbol. May or may not show properly when running as an EXE on Windows.

g_player_cards=[]
g_player_suits=[]
g_dealer_cards=[]
g_dealer_suits=[]

# all audio files are in audio subdir
g_WAVnotification = "audio\\game-notification.wav"
g_WAVcardsdraw = "audio\\cardsdraw.wav"
g_WAVroundover = "audio\\roundover.wav"
g_WAVgameover = "audio\\gameover.wav"
g_WAVwinround = "audio\\coin-prize.wav"

# ---- code logic ----
random.shuffle(g_deck)
random.shuffle(g_suits)
if (DEBUG): print(deck)
if (DEBUG): print(suits)

print("THIS IS BLACKJACK! You are playing against a dealer (House).\nEach round costs 20 chips. \
You have", g_available_chips, "chips to start. \nEach win earns you 20 chips. Each loss costs you 20.")
print("Every round, you get 2 cards. Dealer gets 1 card. After which you are in control and must decide your next move.")
print("\nWhoever goes over 21 points, loses. Otherwise, the highest scorer within 21 points wins at each round.")
print("A player scores BLACKJACK when a player scores (you or the dealer) exactly 21 points resulting in an instant win for the round.")
print("There's no time limit or round limit--- the game ends when you do not have adequate chips to bet for the next round.")

winsound.PlaySound(g_WAVnotification, winsound.SND_FILENAME) #SND

while (g_available_chips>= g_MINIMUMBET):
    
    g_roundover=False 
    
    if (DEBUG): print("\nmain()*** NEW ROUND ***\n")
    else: print("\n*** NEW ROUND ***\n")

    # For each NEW round: Always pick 2 cards for player:
    GetTwoCardsForPlayer()
    # For each NEW round: also pick just 1 card for dealer (and 2 for player as done above).
    GetOneCardForDealer()    
    # Next, check if player got a blackjack on first set of cards (2 cards for player: possible blackjack)
    CheckForBlackjack() 
        
    user_input=""
    while (g_player_score <21 or g_dealer_score <21):                
        if (g_roundover==True):
            break 
        
        user_input=PromptUserForAction()
        if (user_input=='Q'):
            g_roundover=True
            GameOver('Q', "You quit.")
            print("LAST SCORE", g_THINARROW, "PLAYER:", g_player_score, "| DEALER:", g_dealer_score, "| CHIPS LEFT:", g_available_chips)
        
        elif (user_input=='H'):
            winsound.PlaySound(g_WAVcardsdraw, winsound.SND_FILENAME)
            suit=random.choice(g_suits)
            g_player_suits.append(suit) 
            card=random.choice(g_deck) 
            g_player_cards.append(card) 
            if (card !=1):
                print(">> You got", card, "of", suit)
            else:
                print(">> You got Ace of", suit)
            
            g_player_score=sum(g_player_cards) 
            CheckForBlackjack()

        elif (user_input=='S'):
            GetRemainingDealerCards() 
            g_player_score=sum(g_player_cards) 
            CheckWinner()
                    
        else:
            CheckForBlackjack()
            continue 
    

if (g_available_chips < g_MINIMUMBET):
        GameOver('Z', "You ran out of chips!")


#=====end main driver=====



import time
import pyautogui
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class Card:
    def __init__(self, card_name, card_value):
        self.card_name = card_name
        self.card_value = card_value
    used_ace = False



def blackjack_decision(player_cards, dealer_upcard, can_double):

    total_value = player_cards



    if(total_value == 21 and can_double):
        return "WE GOT A BLACKJACK BABY WOOOHOOO"


    if(total_value == 11 and can_double):
        return"Double Down"
    elif(total_value == 10):
        if(dealer_upcard != 11 & dealer_upcard != 10):
            return "Double Down"
        else:
            return "Hit"
    elif(17<=total_value<=20):
        print("stand because we hve 17 - 20")
        return 'Stand'
    elif( 12<= total_value ):
        if(dealer_upcard <=7):
            return "Hit"
        else:
            return "Stand"



    return "Hit"




def get_start_hand(existing_hand):
    # Get input for player's cards and dealer's upcard from the user through the command prompt
    player_card1 = input("Enter your first card (A, K, Q, J, or a number): ").upper()
    player_card2 = input("Enter your second card (A, K, Q, J, or a number): ").upper()




    player_cards = []
    player_cards += existing_hand

    if player_card1 == 'A':
        Ace_card = Card('A', 11)
        player_cards.append(Ace_card)
    elif player_card1 == 'K':
        King_card = Card('K', 10)
        player_cards.append(King_card)
    elif player_card1 == 'Q':
        Queen_card = Card('Q', 10)
        player_cards.append(Queen_card)
    elif player_card1 == 'J':
        Jack_card = Card('J', 10)
        player_cards.append(Jack_card)
    else:
        Any_card = Card(player_card1.__str__(), int(player_card1))
        player_cards.append(Any_card)

    if player_card2 == 'A':
        Ace_card = Card('A', 11)
        player_cards.append(Ace_card)
    elif player_card2 == 'K':
        King_card = Card('K', 10)
        player_cards.append(King_card)
    elif player_card2 == 'Q':
        Queen_card = Card('Q', 10)
        player_cards.append(Queen_card)
    elif player_card2 == 'J':
        Jack_card = Card('J', 10)
        player_cards.append(Jack_card)
    else:
        Any_card = Card(player_card2.__str__(), int(player_card2))
        player_cards.append(Any_card)

    return player_cards

def read_hand():

    # Take a screenshot using pyautogui
    left = 925  # X-coordinate of the left edge
    top = 675  # Y-coordinate of the top edge
    width = 50  # Width of the region
    height = 50  # Height of the region
    time.sleep(2)
    # Capture the screenshot of the specified region
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    screenshot.save('player hand.png')
    # Convert the PIL image to an OpenCV image (NumPy array)
    screenshot_np = np.array(screenshot)

    custom_config = r'--oem 3 --psm 6 outputbase digits'
    text = pytesseract.image_to_string(screenshot_np, config=custom_config)



    numeric_part = ''.join(filter(str.isdigit, text))

    # Convert the extracted numeric part to an integer
    result = int(numeric_part)
    print("our hand is a: ", result)
    return int(result)








def any_blackjacks( ):
    return False
    #code to check if anyone got a blackjack. we can do this by getting some pixel at the bottom, and checking if it has turned black. after each bet there is a
    #short period of time where there are emotes at the bottom, in a rectangle of black background. if this background turns black after we made our bet, someone
    #must have gotten a blackjack!  for now though, we'll return false, assuming theres no blackjacks.


def hit():

    return 0
def stand():
    #a function to stand
    return 0
def double_down():
    #a function to double down
    return 0


while True:
    print("we start heere!")
    player_cards = []

    game_in_progress = True

    time.sleep(2)

    #code to start a game, aka make a bet.


    can_double = True
    #check for blackjacks.

    if any_blackjacks():
        game_in_progress = False
        time.sleep(2)
    else:
        can_split = True

        def dealercard():

            #heights and widths u need for the screenshots are 50 and 50
            time.sleep(2)
            # Take a screenshot using pyautogui
            left = 925  # X-coordinate of the left edge
            top = 275  # Y-coordinate of the top edge
            width = 50  # Width of the region
            height = 50  # Height of the region
            time.sleep(2)
            # Capture the screenshot of the specified region
            screenshot = pyautogui.screenshot(region=(left, top, width, height))

            screenshot.save('dealer card.png')

            # Convert the PIL image to an OpenCV image (NumPy array)
            screenshot_np = np.array(screenshot)

            custom_config = r'--oem 3 --psm 6 outputbase digits'
            text = pytesseract.image_to_string(screenshot_np, config=custom_config)

            print("dealer cart is a: ", text)
            numeric_part = ''.join(filter(str.isdigit, text))

            # Convert the extracted numeric part to an integer
            result = int(numeric_part)
            return Card(text, (result))


        #player_cards = get_start_hand([])
        dealer_value = dealercard().card_value

        while game_in_progress:

            player_cards = read_hand()
            if(player_cards >21):
                game_in_progress = False

            decision = blackjack_decision(player_cards, dealer_value, can_double)


            print("decision: " , decision)

            if(decision == 'Hit'):
               #some shit to double down. then we update the players cards and do it all over again.
                can_double = False
                can_split = False
               #this hitting also gets the new card and appends it.

            elif(decision =='Stand'):
                game_in_progress = False
            elif(decision =='Double Down'):
                #some shit to double down
                game_in_progress = False
            else:
                game_in_progress = False
                print(decision)




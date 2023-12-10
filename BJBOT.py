import time
import pyautogui
import numpy as np
import pytesseract

##for it to work, u need to have the gop3 site, on 67% zoom. u also need  to have f11 on.

# these coords are perfect to give u an indication of how to adjust the screenshot coords:
# left = 840  # X-coordinate of the left edge
# top = 500    # Y-coordinate of the top edge
# width = 200  # Width of the region
# height = 200 # Height of the region

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=1023456789AJKQ'

class Card:
    def __init__(self, card_name, card_value):
        self.card_name = card_name
        self.card_value = card_value
    used_ace = False


def total_value2(player_cards):
    total_value = 0
    for card in player_cards:
        if(card.card_name == 'A' and not card.used_ace):
            if(total_value + 11 > 21):
                total_value += 1
            else:
                total_value += 11
        else:
            total_value += card.card_value
    return total_value




def blackjack_decision(player_cards, dealer_upcard, can_double):



    # Calculate total value of player's cards




    total_value = total_value2(player_cards)



    if(total_value == 21 and can_double):
        return "WE GOT A BLACKJACK BABY WOOOHOOO"




    for card in player_cards:

        if(card.card_name == 'A' and not card.used_ace):

            # Soft hands involving an Ace
            #we might have to implement to see if an ace in our hand is already count as a 1.
            #if total_value == 21:
            #   return "Blackjack!"

            if total_value == 20:
                print("we hebben een aas, en totaal value is 20, dus we staan")
                return "Stand"
            elif total_value == 19:
                print("we hebben een aas, en totaal value is 19, dus we staan")
                return "Stand"
            elif total_value == 18:
                if (2 <= dealer_upcard <= 6 and can_double):
                    return "Double Down"
                else:
                    return "Stand"
            elif total_value == 17:
                if(3<=dealer_upcard<=6 and can_double):
                    return "Double Down"
                else:
                    return "Hit"
            else:
                return "Hit"


        else:
            # Hard hands (no Ace or Ace counts as 1)
            if total_value <= 8:
                return "Hit"
            elif total_value >= 17:
                return "Stand"
            elif total_value == 9:
                if(3<= dealer_upcard <=6 and can_double):
                    return "Double Down"
                else:
                    return "Hit"
            elif total_value == 10:
                if(2<=dealer_upcard<=9 and can_double):
                    return "Double Down"
                else:
                    return "Hit"
            elif total_value == 11:
                if(can_double):
                    return "Double Down"
                else:
                    return "Hit"
            elif(total_value > 11 and dealer_upcard > 6):
                return "Hit"
            else:
                return "Stand"



def what_card_is_this(text):
    if text == 'A':
        Ace_card = Card('A', 11)
        return Ace_card
    elif text == 'K':
        King_card = Card('K', 10)
        return King_card
    elif text == 'Q':
        Queen_card = Card('Q', 10)
        return Queen_card
    elif text == 'J':
        Jack_card = Card('J', 10)
        return Jack_card
    elif text == '1':
        print("we have a 1, which is not possible, unless we have a 10. so this has to be a 10")
        Ten_card = Card('T', 10)
        return Ten_card
    else:
        Any_card = Card(text, int(text))
        return Any_card



def read_hand(amount_of_cards):
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=1023456789AJKQ'
    player_cards = []

    #card 1:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    if(amount_of_cards==2):
        # Take a screenshot using pyautogui
        left = 900  # X-coordinate of the left edge
        top = 590  # Y-coordinate of the top edge
        width = 35  # Width of the region
        height = 38  # Height of the region

        # Capture the screenshot of the specified region
        screenshot = pyautogui.screenshot(region=(left, top, width, height))

        screenshot.save("card 1.png")




        text = pytesseract.image_to_string(screenshot, config=custom_config).strip()  # Remove leading/trailing whitespace
        print("card 1 text found:", text)
        text = text.replace('\n', '')
        player_cards.append(what_card_is_this(text))

        #card 2:


        # Take a screenshot using pyautogui
        left = 935  # X-coordinate of the left edge
        top = 590  # Y-coordinate of the top edge
        width = 35  # Width of the region
        height = 38  # Height of the region


        # Capture the screenshot of the specified region
        screenshot = pyautogui.screenshot(region=(left, top, width, height))

        screenshot.save("card 2.png")


        text = pytesseract.image_to_string(screenshot, config=custom_config).strip()  # Remove leading/trailing whitespace
        text = text.replace('\n', '')
        print("card 2 text found: ", text )
        player_cards.append(what_card_is_this(text))

    elif(amount_of_cards == 3):
        print("we got a third card!")
        left = 955  # X-coordinate of the left edge
        top = 590  # Y-coordinate of the top edge
        width = 35  # Width of the region
        height = 38  # Height of the region

        # Capture the screenshot of the specified region
        screenshot = pyautogui.screenshot(region=(left, top, width, height))

        screenshot.save("card 3.png")

        text = pytesseract.image_to_string(screenshot, config=custom_config).strip()  # Remove leading/trailing whitespace
        text = text.replace('\n', '')
        print("card 3 text found: ", text)
        player_cards.append(what_card_is_this(text))



    return player_cards










def any_blackjacks( ):
    return False
    #code to check if anyone got a blackjack. we can do this by getting some pixel at the bottom, and checking if it has turned black. after each bet there is a
    #short period of time where there are emotes at the bottom, in a rectangle of black background. if this background turns black after we made our bet, someone
    #must have gotten a blackjack!  for now though, we'll return false, assuming theres no blackjacks.


def hit():
    x_coord = 702
    y_coord = 939

    time.sleep(1)
    pyautogui.click(x=x_coord, y=y_coord)


    #then sleep while dealer deals cards
    time.sleep(2)


def stand():
    #a function to stand
    x_coord=971
    y_coord=918

    time.sleep(1)
    pyautogui.click(x=x_coord, y=y_coord)


    return 0
def double_down():
    #a function to double down
    x_coord = 1007
    y_coord = 730
    time.sleep(1)
    pyautogui.click(x=x_coord, y=y_coord)

    time.sleep(2)
    return 0

def make_bet():
    x_coord = 702
    y_coord = 939

    time.sleep(1)
    pyautogui.click(x=x_coord, y=y_coord)


    #then sleep while dealer deals cards
    time.sleep(2)


while True:
    print("we start heere!")
    time.sleep(3)
    player_cards = []

    game_in_progress = True
    can_double = True
    can_split = True
    make_bet()
    time.sleep(2)


    #code to start a game, aka make a bet.


    can_double = True
    #check for blackjacks.

    if any_blackjacks():
        game_in_progress = False
        time.sleep(2)
    else:

        def dealercard():

            time.sleep(2)
            # Take a screenshot using pyautogui
            left = 902  # X-coordinate of the left edge
            top = 308  # Y-coordinate of the top edge
            width = 30  # Width of the region
            height = 35  # Height of the region

            # Capture the screenshot of the specified region
            screenshot = pyautogui.screenshot(region=(left, top, width, height))

            screenshot.save("dealer card.png")

            custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=1023456789AJKQ'
            text = pytesseract.image_to_string(screenshot,config=custom_config).strip()  # Remove leading/trailing whitespace
            text = text.replace('\n', '')
            print("dealer card found: ", text)
            return what_card_is_this(text)




        #player_cards = get_start_hand([])
        dealer_value = dealercard().card_value

        amount_of_cards = 2

        while game_in_progress:
            if(amount_of_cards==2):
                player_cards = read_hand(amount_of_cards)
            else:
                player_cards2  = read_hand(amount_of_cards)
                player_cards.extend(player_cards2)

            if(total_value2(player_cards) >21):
                game_in_progress = False
            else:

                decision = blackjack_decision(player_cards, dealer_value, can_double)


                print("decision: " , decision)

                if(decision == 'Hit'):
                   #some shit to double down. then we update the players cards and do it all over again.
                    can_double = False
                    can_split = False
                   #this hitting also gets the new card and appends it.
                    hit()
                    amount_of_cards = amount_of_cards + 1
                    time.sleep(2)
                elif(decision =='Stand'):
                    print("were standing! the game is over! next one please!")
                    stand()
                    time.sleep(5)
                    game_in_progress = False
                elif(decision =='Double Down'):
                    #some shit to double down
                    double_down()
                    time.sleep(5)
                    game_in_progress = False
                else:
                    game_in_progress = False
                    time.sleep(5)
                    print(decision)












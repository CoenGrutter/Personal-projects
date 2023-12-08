import time


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






def any_blackjacks( ):
    return False
    #code to check if anyone got a blackjack. we can do this by getting some pixel at the bottom, and checking if it has turned black. after each bet there is a
    #short period of time where there are emotes at the bottom, in a rectangle of black background. if this background turns black after we made our bet, someone
    #must have gotten a blackjack!  for now though, we'll return false, assuming theres no blackjacks.


def hit():
    #a function to hit. for now, we'l return a 7. we'll have to return the card  we got though.
    return Card('7', 7)


while True:
    print("we start heere motherfuckersss")
    player_cards = []

    game_in_progress = True

    time.sleep(2)

    #code to start a game, aka make a bet.


    #check for blackjacks.

    if any_blackjacks():
        game_in_progress = False
        time.sleep(2)
    else:
        can_double = True

        def dealercard():
            dealer_upcard = input("enter the dealers upcard here:   ").upper()
            if dealer_upcard== 'A':
               return  Card('A', 11)
            elif dealer_upcard == 'K':
                return  Card('K', 10)
            elif dealer_upcard== 'Q':
                return Card('Q', 10)
            elif dealer_upcard == 'J':
                return  Card('J', 10)
            else:
                return Card(dealer_upcard.__str__(), int(dealer_upcard))


        player_cards = get_start_hand([])

        while game_in_progress:

            dealer_value = dealercard().card_value

            if(can_double):
                decision = blackjack_decision(player_cards, dealer_value, can_double)
            else:
                decision = blackjack_decision(player_cards, dealer_value, can_double)


            print("decision: " , decision)

            if(decision == 'Hit'):
               #some shit to double down. then we update the players cards and do it all over again.
                can_double = False
               #this hitting also gets the new card and appends it.
                player_cards.append(hit())

            elif(decision =='Stand'):
                print("WE stood, the game ends. we stood at: ", total_value2(player_cards))
                game_in_progress = False
            elif(decision =='Double Down'):
                #some shit to double down
                player_cards.append(hit())
                print("we doubled down, we get one more card, then the game ends! we ended up at: ",    total_value2(player_cards))
                game_in_progress = False
            else:
                game_in_progress = False
                print(decision)




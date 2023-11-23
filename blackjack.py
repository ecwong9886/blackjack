import random

deck = []
hands = {}

for pip in range(1, 14):
    for suit in ("Diamond", "Club", "Heart", "Spade"):
        if pip > 1 and pip <= 10:
            deck.append((str(pip), suit, pip))
        elif pip == 1:
            deck.append(("Ace", suit, 1))
        elif pip == 11:
            deck.append(("Jack", suit, 10))
        elif pip == 12:
            deck.append(("Queen", suit, 10))
        elif pip == 13:
            deck.append(("King", suit, 10))

hands["dealer"] = []
hands["player"] = [(10, 'Club'), ('Ace', 'Diamond')]


def deal_card(person):
    dealing_card = random.choice(deck)
    deck.remove(dealing_card)
    hands[person].append(dealing_card)
    print(f"{dealing_card} was dealt to {person}.")

def print_hands():
    print(f"Dealer's hand: {hands['dealer']}")
    print(f"Player's hand: {hands['player']}")

def start_game():
    deal_card("player")
    deal_card("dealer")
    deal_card("player")
    deal_card("dealer")
    print_hands()

def check_naturals():
    for card_i in hands["player"]:
        if card_i[2] == 1:
            for card_j in hands["player"]:
                if card_j[2] == 10:
                    return True
        else:
            return False
        
def get_total(person):
    total = 0
    for card in hands[person]:
        total += card[2]
        if card[2] == 1:
            if total + 10 <= 21:
                return total + 10
            else:
                return total

def player_turn():
    while True:
        menu = input("1. Stand\n2. Hit\n")
        if menu == "1":
            break
        elif menu == "2":
            deal_card("player")
            print_hands()

def dealer_turn():
    while True:
        if get_total("dealer") < 17:
            deal_card("dealer")
        elif get_total("dealer") > 21:
            print("Dealer busted!")
            break
        else:
            print("Dealer stands.")
            break
        

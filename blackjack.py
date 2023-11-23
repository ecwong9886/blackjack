import random

deck = []
hands = {}
hands["dealer"] = []
hands["player"] = []


def generate_deck():
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

def deal_card(person):
    dealing_card = random.choice(deck)
    deck.remove(dealing_card)
    hands[person].append(dealing_card)
    print(f"{dealing_card} was dealt to {person}.")

def print_hands():
    print()
    print(f"Dealer's hand: {hands['dealer']}")
    print(f"Player's hand: {hands['player']}")

def start_game():
    deck.clear()
    hands["dealer"].clear()
    hands["player"].clear()
    generate_deck()
    print("* * *B L A C K J A C K * * *\n")
    deal_card("player")
    deal_card("dealer")
    deal_card("player")
    deal_card("dealer")
    print_hands()

def check_naturals(person):
    for card_i in hands[person]:
        if card_i[2] == 1:
            for card_j in hands[person]:
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
    print("\nPlayer's turn:")
    while get_total("player") <= 21:
        menu = input("1. Stand\n2. Hit\n")
        if menu == "1":
            break
        elif menu == "2":
            deal_card("player")
            print_hands()

def dealer_turn():
    while get_total("dealer") < 17:
        print("Dealer hits.")
        deal_card("dealer")


while True:
    input("Press ENTER to start a new game")
    start_game()

    if check_naturals("player"):
        if check_naturals("dealer"):
            print("Tie.")
        else:
            print("Player won.")
        continue

    player_turn()
    player_total = get_total("player")
    if player_total > 21:
        print("Player busted!")
        continue

    dealer_turn()
    dealer_total = get_total("dealer")
    if dealer_total > 21:
        print("Dealer busted!")
    else:
        print("Dealer stands.")
        print(f"Player total: {player_total}")
        print(f"Dealer total: {dealer_total}")
        if player_total > dealer_total:
            print("Player won.")
        elif dealer_total > player_total:
            print("Dealer won.")
        else:
            print("Tie.")
    continue

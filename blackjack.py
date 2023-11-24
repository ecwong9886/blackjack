import random, time, os 

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

def print_hand(person='both'):
    if person == 'both':
        print(f"\nDealer's hand: {hands['dealer']}")
        print(f"Player's hand: {hands['player']}\n")
    else:
        print((f"\nPlayer's hand: {hands[person]}\n"))

def start_game():
    os.system('cls')
    deck.clear()
    hands["dealer"].clear()
    hands["player"].clear()
    generate_deck()
    print("* * *B L A C K J A C K * * *\n")
    time.sleep(1)
    deal_card("player")
    time.sleep(1)
    deal_card("dealer")
    time.sleep(1)
    deal_card("player")
    time.sleep(1)
    deal_card("dealer")
    time.sleep(1)
    print_hand()

def check_blackjack(person):
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
    time.sleep(1)
    print("===== Player's turn =====\n")
    while get_total("player") <= 21:
        menu = input("1. Stand\n2. Hit\n")
        print()
        if menu == "1":
            time.sleep(1)
            print("Player stands.")
            time.sleep(1)
            break
        elif menu == "2":
            time.sleep(1)
            deal_card("player")
            time.sleep(1)
            print_hand("player")
            time.sleep(1)

def dealer_turn():
    print("\n===== Dealer's turn =====\n")
    while get_total("dealer") < 17:
        time.sleep(1)
        print("Dealer hits.\n")
        time.sleep(1)
        deal_card("dealer")
        time.sleep(1)
        print_hand("dealer")
    time.sleep(1)


print("* * * B L A C K J A C K * * *\n")
input("Press Enter to start")

while True:

    start_game()

    if check_blackjack("player"):
        if check_blackjack("dealer"):
            print("Blackjacks for both player and dealer! Tie.")
        else:
            print("Blackjack for player! Player won.")
        input("\nPress Enter to start a new game...")
        continue
    elif check_blackjack("dealer"):
        print("Blackjack for dealer. Dealer won.")
        input("\nPress Enter to start a new game...")
        continue

    player_turn()

    player_total = get_total("player")
    if player_total > 21:
        print("Player busted! Dealer won.")
        time.sleep(1)
        input("\nPress Enter to start a new game...")
        continue

    dealer_turn()

    dealer_total = get_total("dealer")
    if dealer_total > 21:
        print("Dealer busted! Player won.")
    else:
        print("Dealer stands.")
        time.sleep(1)
        print("\n===== Final results =====")
        print_hand()
        time.sleep(1)
        print(f"Player total: {player_total}")
        print(f"Dealer total: {dealer_total}\n")
        time.sleep(1)
        if player_total > dealer_total:
            print("Player won.")
        elif dealer_total > player_total:
            print("Dealer won.")
        else:
            print("Tie.")
    time.sleep(1)
    input("\nPress Enter to start a new game...")
    continue

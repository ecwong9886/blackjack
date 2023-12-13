import random, time, os 

deck = []
hands = {"dealer": [], "player": []}

def generate_deck():
    for pip in range(1, 14):
        for suit in ("♦", "♣", "♥", "♠"):
            if pip > 1 and pip <= 10:
                deck.append((str(pip), suit, pip))
            elif pip == 1:
                deck.append(("A", suit, 1))
            elif pip == 11:
                deck.append(("J", suit, 10))
            elif pip == 12:
                deck.append(("Q", suit, 10))
            elif pip == 13:
                deck.append(("K", suit, 10))

def deal_card(person, start_deal = False):
    dealing_card = random.choice(deck)
    deck.remove(dealing_card)
    hands[person].append(dealing_card)
    if not start_deal:
        print(f"{dealing_card[0]}{dealing_card[1]} was dealt to {person}")

def print_hand(person, hide_first = False):

    hand = hands[person]
    header = " " + person.capitalize() + " "
    lines = [[] for i in range(7)]
    for index, card in enumerate(hand):
        header = f">>>>{header}<<<<"

        if hide_first and index == 0:
            suit_symbol = "*"
            pip_symbol = "  "
        else:
            suit_symbol = card[1]
            pip_symbol = card[0] if card[0] == "10" else card[0] + " "

        lines[0].append('┌───────┐')
        lines[1].append('│ {}    │'.format(pip_symbol))
        lines[2].append('│       │')
        lines[3].append('│   {}   │'.format(suit_symbol))
        lines[4].append('│       │')
        lines[5].append('│     {}│'.format(pip_symbol))
        lines[6].append('└───────┘')

    print()
    print(header)
    for line in lines:
        print(" ".join(line))
    time.sleep(1)

def start_game():
    os.system('cls')
    deck.clear()
    hands["dealer"].clear()
    hands["player"].clear()
    generate_deck()
    print("* * * * B L A C K J A C K * * * *\n")
    time.sleep(1)
    print("Dealing...")
    deal_card("player", True)
    deal_card("dealer", True)
    deal_card("player", True)
    deal_card("dealer", True)
    time.sleep(1)
    print_hand("dealer", True)
    print_hand("player")

def check_blackjack(person):
    for card_i in hands[person]:
        if card_i[2] == 1:
            for card_j in hands[person]:
                if card_j[2] == 10:
                    return True
        
    return False
        
def get_total(person):
    total = 0
    has_ace = False
    for card in hands[person]:
        total += card[2]
        if card[2] == 1:
            has_ace = True

    if has_ace:     
        if total + 10 <= 21:
            return total + 10
    
    return total

def player_turn():
    while get_total("player") <= 21:
        menu = input("1. Stand\n2. Hit\n")
        print()
        if menu == "1":
            print("Player stands.")
            break
        elif menu == "2":
            deal_card("player")
            time.sleep(1)
            print_hand("player")

def dealer_turn():
    time.sleep(1)
    print_hand("dealer")
    while get_total("dealer") < 17:
        print("Dealer hits.\n")
        time.sleep(1)
        deal_card("dealer")
        time.sleep(1)
        print_hand("dealer")


input("""

______ _            _    _            _    
| ___ \ |          | |  (_)          | |   
| |_/ / | __ _  ___| | ___  __ _  ___| | __
| ___ \ |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_/ / | (_| | (__|   <| | (_| | (__|   < 
\____/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\.
                       _/ |                
                      |__/                 


            Press Enter to start""")

while True:

    start_game()

    if check_blackjack("player"):
        if check_blackjack("dealer"):
            print("Blackjacks for both player and dealer! Tie.")
        else:
            print("Blackjack for player! Player won.")
        time.sleep(1)
        input("\nPress Enter to start a new game...")
        continue
    elif check_blackjack("dealer"):
        print("Blackjack for dealer. Dealer won.")
        time.sleep(1)
        input("\nPress Enter to start a new game...")
        continue

    player_turn()

    player_total = get_total("player")
    if player_total > 21:
        print("\nPlayer busted! Dealer won.")
        time.sleep(1)
        input("\nPress Enter to start a new game...")
        continue

    dealer_turn()

    dealer_total = get_total("dealer")
    if dealer_total > 21:
        print("\nDealer busted! Player won.")
    else:
        print("Dealer stands.")
        time.sleep(1)
        print("\n====== Final results ======")
        print(f"\nDealer total: {dealer_total}")
        time.sleep(1)
        print(f"Player total: {player_total}\n")
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

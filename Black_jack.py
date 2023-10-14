from random import shuffle

def create_deck():
    suits = ["spades", "clubs", "diamonds", "hearts"]
    values = list(range(2, 11)) + ["J", "Q", "K", "A"]
    deck = []
    for suit in suits:
        for val in values:
            deck.append(Card(val, suit))
    return deck

def deck_sum(deck):
    summ = 0
    alt_sum = 0
    spec = ("J", "Q", "K")
    for card in deck:
        if (card.value in spec):
            summ += 10
            alt_sum += 10
        elif card.value == "A":
            summ += 11
            alt_sum += 1
        else:
            summ += card.value
            alt_sum += card.value
    return (summ, alt_sum)


def overdraw_check(deck):
    summ, alt_sum = deck_sum(deck)
    if (summ > 21 and alt_sum > 21):
        return True
    else:
        return False

def draw_process(player, dealer, deck):
    draw_confirm = input("Would you like to draw? (y/n)")
    if (draw_confirm == "y"):
        player.append(deck.pop())
        print(f"DEALER_HAND: {dealer}")
        print(f"YOUR_HAND: {player}")
        if (overdraw_check(player) == True):
            print("Overdraw.")
            return 0
        else:
            draw_process(player, dealer, deck)
    elif (draw_confirm == "n"):
        return 0
    else:
        print("Please, enter valid answer")
        draw_process(player, dealer, deck)
    return 0

def black_jack():
    print("Welcome to Black Jack table, padre. Let's play.")
    deck = create_deck()
    shuffle(deck)
    dealer = []
    player = []
    dealer.append(deck.pop())
    player.append(deck.pop())
    player.append(deck.pop())
    hidden_card = deck.pop()
    print(f"DEALER_HAND: {dealer}")
    print(f"YOUR_HAND: {player}")
    if (deck_sum(player)[0] == 21):
        print("BLACKJACK!!!")
        return 0
    a = draw_process(player, dealer, deck)

    dealer.append(hidden_card)
    print(f"DEALER_HAND: {dealer}")
    print(f"YOUR_HAND: {player}")
    sum_d, alt_sum_d = deck_sum(dealer)
    while (sum_d < 17 or alt_sum_d < 17):
        dealer.append(deck.pop())
        print(f"DEALER_HAND: {dealer}")
        print(f"YOUR_HAND: {player}")
        sum_d, alt_sum_d = deck_sum(dealer)
        if (sum_d > 16 and sum_d < 22):
            break
    if (sum_d > 21):
        sum_d = alt_sum_d
    sum_p, alt_sum_p = deck_sum(player)
    if (sum_p > 21):
        sum_p = alt_sum_p
    if ((sum_p > sum_d and sum_p < 22) or (sum_d > 21 and sum_p < 22) ):
        print("YOU WIN!")
    elif (sum_d > sum_p and sum_d < 22 or (sum_p > 21 and sum_d < 22 )):
        print("You lose.")
    elif (sum_p == sum_d or (sum_d > 21 and sum_p > 21)):
        print("Tie.")
    return 0



class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return (f"{self.value} of {self.suit}")


if (__name__ == "__main__"):
    black_jack()
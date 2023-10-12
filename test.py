import random

cards = ["jack" , "queen", "king"]

card_pick = random.randint(9, 13)

if card_pick == 10:
    random_cards = random.choice(cards)
    print(random_cards)
else:
    print(card_pick)



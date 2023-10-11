import random

cards = ["jack" , "queen", "king", 10]

card_pick = random.randint(9, 10)

if card_pick == 10:
    random_cards = random.choice(cards)
    print(random_cards)
else:
    print(card_pick)



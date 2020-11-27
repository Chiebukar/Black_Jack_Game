class Card(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite

    def __str__(self):
        rep = self.rank + self.suite
        return rep


class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        rep = ""
        if self.cards:
            for card in self.cards:
                rep += str(card) + " "
            return rep
        else:
            return "<Empty>"

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

    def clear(self):
        self.cards.clear()


def main():

    # Creating object instances of Card
    card1 = Card("A", "c")
    card2 = Card("2", "c")
    card3 = Card("3", "c")
    card4 = Card("4", "c")
    card5 = Card("5", "c")
    print("Printing the 5 generated cards")
    print(card1, card2, card3, card4, card5)

# Creating my_hand object instance of Hand class
    my_hand = Hand()
    print("printing cards in my_hand")
    print("my_hand: ", my_hand)
# Adding generated cards to the my_hand object
    my_hand.add(card1)
    my_hand.add(card2)
    my_hand.add(card3)
    my_hand.add(card4)
    my_hand.add(card5)
    print("printing cards in my hand after adding generated cards")
    print("my_hand: ", my_hand)
#   creating other_hand object of Hand class
    other_hand = Hand()
# Giving card1 and card2 to other_hand from my_hand
    my_hand.give(card1, other_hand)
    my_hand.give(card2, other_hand)
    print("printing cards in  my_hand after giving away card1 and card2")
    print("my_hand: ", my_hand)
    print("printing cards in other_hand after getting two cards from my_hand")
    print("other_hand: ", other_hand)


main()








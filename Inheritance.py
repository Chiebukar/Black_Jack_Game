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
            print("<Empty>")

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

    def clear(self):
        self.cards.clear()


class Deck(Hand):
    def populate(self):
        for suite in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suite))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand):
        for rounds in range(per_hand):
            for hand in hands:
                top_card = self.cards[0]
                self.give(top_card, hand)


def main():
    deck1 = Deck()
    print("Populating deck")
    deck1.populate()
    print(deck1)
    print("Shuffling deck")
    deck1.shuffle()
    print(deck1)
    my_hand = Hand()
    your_hand = Hand()
    hands = [my_hand, your_hand]
    print("Sharing cards to hands")
    deck1.deal(hands, 5)
    print(my_hand)
    print(your_hand)
    print("After sharing cards to hand, deck becomes")
    print(deck1)


main()





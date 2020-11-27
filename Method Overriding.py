class Cards(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite

    def __str__(self):
        rep = self.rank + self.suite
        return rep

# New sub class of Cards  with a  __str__ method
# Method to overrides Card's __str__() method by the using same name


class Unprintable(Cards):
    def __str__(self):
        return "Unprintable"

# New sub class of Cards  with __init__ and   __str__ methods
# Method to overrides Card's  __init__ and   __str__ methods
# By modifying their functionality


class PositionalCard(Cards):
    def __init__(self, rank, suite, face_up=True):
        super(PositionalCard, self).__init__(rank, suite)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(PositionalCard, self).__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


def main():
    card1 = Cards("A", "c")
    card2 = Unprintable("A", "c")
    card3 = PositionalCard("A", "c")

    print("Printing Cards' object")
    print(card1)
    print("Printing Unprintable's object")
    print(card2)
    print("printing Positional card's object")
    print(card3)
    print("Flipping card 3")
    card3.flip()
    print(card3)


main()
input("\n\n press the enter key to exit")




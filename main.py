import random


def main():
    class Card( object) :
        def __init__(self, face, value, suit):
            self.face = face
            self.value = value
            self.suit = suit
        def __repr__(self):
            return str(self.face) + " of " + self.suit 

    class Deck( list ):
        def __init__(self):
            suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
            values = {
                "Two"   : 2,
                "Three" : 3,
                "Four"  : 4,
                "Five"  : 5,
                "Six"   : 6,
                "Seven" : 7,
                "Eight" : 8,
                "Nine"  : 9,
                "Ten"   : 10,
                "Jack"  : 11,
                "Queen" : 12,
                "King"  : 13,
                "Ace"   : 14
            }

            for suit in suits:
                for faceValue in values:
                    self.append(Card(faceValue, values[faceValue], suit))
            print("Taking the deck out of the box...")
        
        def shuffle(self, times=1):
            random.shuffle(self)
            print("Shuffling the deck...")

        def deal(self):
            return self.pop()
    
    class Player(object):
        def __init__(self, name):
            self.hand = []
            self.name = name
        
        def draw(self, deck):
            self.hand.append(deck.deal())
            print("Dealing to player " + self.name + "...")

        def showHand(self):
            print(self.name + "'s hand is:")
            for card in self.hand:
                print(card)

    
    deck = Deck()
    deck.shuffle()
    stanislav = Player("Stasyan")
    stanislav.draw(deck)
    stanislav.draw(deck)
    stanislav.showHand()
    
    




if __name__ == "__main__":
    main()
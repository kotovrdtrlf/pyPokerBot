import random


def main():
    class Card(object) :
        def __init__(self, face, value, suit):
            self.face = face
            self.value = value
            self.suit = suit
        def __repr__(self):
            return str(self.face) + " of " + self.suit 

    class Deck(list):
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

        def burn(self):
            self.pop()
    
    class Player(object):
        def __init__(self, name):
            self.hand = []
            self.name = name
        
        def draw(self, deck):
            self.hand.append(deck.deal())
            print("Dealing to player " + self.name + "...")

        def showHand(self):
            if len(self.hand) != 0:
                print(self.name + "'s hand is: " + str(self.hand[0]) + " and " + str(self.hand[1]))
            else:
                print(self.name + "'s hand is empty")

    class Table(object):
        def __init__(self, players):
            self.tableCards = []
            self.players = players
            print("Players " + self.showPlayers() + "sat at the table")

        def showTable(self):
            tableStr = ""
            for card in self.tableCards:
                tableStr += str(card) + ", "
            print(tableStr)

        def showPlayers(self):
            playersStr = ""
            for player in self.players:
                playersStr += player.name + ", "
            return playersStr

        def flop(self, deck):
            print("Burning the first card...")
            deck.burn()
            print("Flopping three cards...")
            for i in range(3):
                self.tableCards.append(deck.deal())
            self.showTable()

        def turn(self, deck):
            print("Burning the first card...")
            deck.burn()
            print("Drawing turn...")
            self.tableCards.append(deck.deal())
            self.showTable()

        def river(self, deck):
            print("Burning the first card...")
            deck.burn()
            print("Drawing river...")
            self.tableCards.append(deck.deal())
            self.showTable()

        def dealer(self, deck):
            print("Dealing out to players at the table...")
            for counter in range(2):
                for player in self.players:
                    player.draw(deck)
            print("All players were dealt to")
            
    class handAsessor(object):
        def __init__(self, cards):
            self.hand = cards
            self.handValues = sorted([card.value for card in self.hand])
            self.handUniqueValues = list(set(self.handValues))
            self.handSuits = [card.suit for card in self.hand]
            self.handUniqueSuits = list(set(self.handSuits))

        def royalFlush(self):
            if len(self.hand) == 5:
                if self.handValues[0] == 10 and self.straight() and self.flush():
                    return True
                return False
            elif len(self.hand) == 7:
                numOfCardsInARow = 0
                cardIndex = 0
                isStraight = False
                straightHand = []
                straightHandSuits = []
                while (cardIndex < len(self.hand) - 1) and not isStraight:
                    if self.handValues[cardIndex + 1] - self.handValues[cardIndex] == 1:
                        straightHand.append(self.handValues[cardIndex])
                        straightHandSuits.append(self.handSuits[cardIndex])
                        numOfCardsInARow += 1
                        if numOfCardsInARow == 4:
                            straightHand.append(self.handValues[cardIndex+1])
                            straightHandSuits.append(self.handSuits[cardIndex+1])
                            isStraight = True
                        else:
                            cardIndex += 1
                    else:
                        numOfCardsInARow = 0
                        straightHand = []
                        straightHandSuits = []
                        cardIndex += 1
                if isStraight:
                    if straightHand[0] == 10:
                        if len(straightHand) == 5 and len(list(set(straightHandSuits))):
                            return True
                        return False
                    return False
                return False
            else:
                print("Something went horribly wrong in hand size (royal flush)!")
                

        def straightFlush(self):
            if len(self.hand) == 5:
                if self.straight() and self.flush():
                    return True
                return False
            elif len(self.hand) == 7:
                numOfCardsInARow = 0
                cardIndex = 0
                isStraight = False
                straightHand = []
                straightHandSuits = []
                while (cardIndex < len(self.hand) - 1) and not isStraight:
                    if self.handValues[cardIndex + 1] - self.handValues[cardIndex] == 1:
                        straightHand.append(self.handValues[cardIndex])
                        straightHandSuits.append(self.handSuits[cardIndex])
                        numOfCardsInARow += 1
                        if numOfCardsInARow == 4:
                            straightHand.append(self.handValues[cardIndex+1])
                            straightHandSuits.append(self.handSuits[cardIndex+1])
                            isStraight = True
                        else:
                            cardIndex += 1
                    else:
                        numOfCardsInARow = 0
                        straightHand = []
                        straightHandSuits = []
                        cardIndex += 1
                if isStraight:
                    if len(straightHand) == 5 and len(list(set(straightHandSuits))):
                        return True
                    return False
                return False
            else:
                print("Something went horribly wrong in hand size (straight flush)!")
            
        def fourOfAKind(self):
            for value in self.handUniqueValues:
                if self.handValues.count(value) == 4:
                    return True
                return False

        def fullHouse(self):
            hasSet = False
            hasPair = False
            for value in self.handUniqueValues:
                if self.handValues.count(value) >= 3:
                    hasSet = True
                elif self.handValues.count(value) >= 2:
                    hasPair = True
            return hasSet and hasPair


        def flush(self):
            if len(self.hand) == 5 and len(self.handUniqueSuits) == 1:
                return True
            elif len(self.hand) == 7:
                for suit in self.handUniqueSuits:
                    if self.handSuits.count(suit) == 5:
                        return True
                return False
            else:
                print("Something went horribly wrong in hand size (flush)!")

        def straight(self):
            if len(self.hand) == 5:
                if self.handValues[4] == 14 and self.handValues[0] == 2:
                    for cardIndex in range(2):
                        if self.handValues[cardIndex+1] != self.handValues[cardIndex] + 1:
                            return False
                    return True
                else:   
                    for cardIndex in range(3):
                        if self.handValues[cardIndex+1] != self.handValues[cardIndex] + 1:
                            return False
                    return True
            elif len(self.hand) == 7:
                numOfCardsInARow = 0
                cardIndex = 0
                isStraight = False
                while (cardIndex < len(self.hand) - 1) and not isStraight:
                    if self.handValues[cardIndex + 1] - self.handValues[cardIndex] == 1:
                        numOfCardsInARow += 1
                        if numOfCardsInARow == 4:
                            isStraight = True
                        else:
                            cardIndex += 1
                    else:
                        numOfCardsInARow = 0
                        cardIndex += 1
                return isStraight
            else:
                print("Something went terribly wrong in hand size (straight)!")


        def threeOfAKind(self):
            for value in self.handUniqueValues:
                if self.handValues.count(value) == 3:
                    return True
            return False
            
        def twoPairs(self):
            pass                                #needs thinking, subject - count will count same element 

        def pair(self):
            for value in self.handUniqueValues:
                if self.handValues.count(value) == 2:
                    return True
            return False

        def highCard(self):
            return self.handValues[len(self.hand)-1] #review this is wrong
        
    #TESTING WHATS READY, JUST RUN AND CHECK CONSOLE---------------------------------
    deck = Deck()
    deck.shuffle()
    player1 = Player("Stas")
    player2 = Player("Dan")
    player3 = Player("Max")
    player2.showHand()
    someplayers = [player1, player2, player3]
    table = Table(someplayers)
    table.dealer(deck)
    player1.showHand()
    player2.showHand()
    player3.showHand()
    table.flop(deck)
    table.turn(deck)
    table.river(deck)
    handToAssess = table.tableCards + player2.hand
    somehand = handAsessor(handToAssess)
    print("--------------------")
    print(handToAssess)
    print("--------------------")
    print("Royal flush -", somehand.royalFlush())
    print("Straight flush -", somehand.straightFlush())
    print("4 of a Kind -", somehand.fourOfAKind())
    print("Full House -", somehand.fullHouse())
    print("Flush -", somehand.flush())
    print("Straight -", somehand.straight())
    print("Set -", somehand.threeOfAKind())
    print("Pair -", somehand.pair())
    print("Kicker -", somehand.highCard())










if __name__ == "__main__":
    main()
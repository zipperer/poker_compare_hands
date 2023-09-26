class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def cardRank(self):
        return self.rank

    def cardSuit(self):
        return self.suit

    def toString(self):
        return '{rank} of {suit}s'.format(rank=self.rank, suit=self.suit)

    def printCard(self, indent=0):
        print((' ' * indent) + self.toString())

ace_of_spades     = Card('ace','spade')
king_of_spades    = Card('king','spade')
queen_of_spades   = Card('queen','spade')
jack_of_spades    = Card('jack','spade')
ten_of_spades     = Card('ten','spade')
nine_of_spades    = Card('nine','spade')
eight_of_spades   = Card('eight','spade')
seven_of_spades   = Card('seven','spade')
six_of_spades     = Card('six','spade')
five_of_spades    = Card('five','spade')
four_of_spades    = Card('four','spade')
three_of_spades   = Card('three','spade')
two_of_spades     = Card('two','spade')
ace_of_hearts     = Card('ace','heart')
king_of_hearts    = Card('king','heart')
queen_of_hearts   = Card('queen','heart')
jack_of_hearts    = Card('jack','heart')
ten_of_hearts     = Card('ten','heart')
nine_of_hearts    = Card('nine','heart')
eight_of_hearts   = Card('eight','heart')
seven_of_hearts   = Card('seven','heart')
six_of_hearts     = Card('six','heart')
five_of_hearts    = Card('five','heart')
four_of_hearts    = Card('four','heart')
three_of_hearts   = Card('three','heart')
two_of_hearts     = Card('two','heart')
ace_of_diamonds   = Card('ace','diamond')
king_of_diamonds  = Card('king','diamond')
queen_of_diamonds = Card('queen','diamond')
jack_of_diamonds  = Card('jack','diamond')
ten_of_diamonds   = Card('ten','diamond')
nine_of_diamonds  = Card('nine','diamond')
eight_of_diamonds = Card('eight','diamond')
seven_of_diamonds = Card('seven','diamond')
six_of_diamonds   = Card('six','diamond')
five_of_diamonds  = Card('five','diamond')
four_of_diamonds  = Card('four','diamond')
three_of_diamonds = Card('three','diamond')
two_of_diamonds   = Card('two','diamond')
ace_of_clubs      = Card('ace','club')
king_of_clubs     = Card('king','club')
queen_of_clubs    = Card('queen','club')
jack_of_clubs     = Card('jack','club')
ten_of_clubs      = Card('ten','club')
nine_of_clubs     = Card('nine','club')
eight_of_clubs    = Card('eight','club')
seven_of_clubs    = Card('seven','club')
six_of_clubs      = Card('six','club')
five_of_clubs     = Card('five','club')
four_of_clubs     = Card('four','club')
three_of_clubs    = Card('three','club')
two_of_clubs      = Card('two','club')

ranksLowToHigh = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']

def rankHigherThanRank(rankA, rankB):
    rankAIndexInRanksLowToHigh = rankIndexInRanksLowToHigh(rankA)
    rankBIndexInRanksLowToHigh = rankIndexInRanksLowToHigh(rankB)
    rankAIndexHigherThanRankBIndex = (rankAIndexInRanksLowToHigh > rankBIndexInRanksLowToHigh)
    return rankAIndexHigherThanRankBIndex

def cardRankHigherThanCardRank(cardA, cardB):
    cardARank = cardA.cardRank()
    cardBRank = cardB.cardRank()
    cardARankHigherThanCardBRank = rankHigherThanRank(cardARank, cardBRank)
    return cardARankHigherThanCardBRank

def rankIndexInRanksLowToHigh(rank):
    return ranksLowToHigh.index(rank)

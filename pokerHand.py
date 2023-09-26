from card import *

class PokerHand:

    def printPokerHand(self):
        print('hand:')
        cards_indent = 2
        cards_left_padding = ' ' * cards_indent
        print(cards_left_padding + 'cards:')
        for card in self.cards:
            card.printCard(indent=4)
        labels_indent = 2
        labels_left_padding = ' ' * labels_indent
        pokerHandDictCopy = self.__dict__.copy()
        del pokerHandDictCopy['cards']
        print(labels_left_padding + 'labels:')
        for label, card in pokerHandDictCopy.items():
            print(labels_left_padding * 2, label, ': ', card.toString())

    def handType(self):
        return type(self)
        
class PokerHandHighCard(PokerHand):

    def __init__(self, cards, highestRank, secondHighestRank, thirdHighestRank, fourthHighestRank, fifthHighestRank):
        self.cards = cards
        self.highestRank = highestRank
        self.secondHighestRank = secondHighestRank
        self.thirdHighestRank = thirdHighestRank
        self.fourthHighestRank = fourthHighestRank
        self.fifthHighestRank = fifthHighestRank    

    def highCardHighestRank(self):
        return self.highestRank

    def highCardSecondHighestRank(self):
        return self.secondHighestRank 

    def highCardThirdHighestRank(self):
        return self.thirdHighestRank

    def highCardFourthHighestRank(self):
        return self.fourthHighestRank

    def highCardFifthHighestRank(self):
        return self.fifthHighestRank 

class PokerHandOnePair(PokerHand):

    def __init__(self, cards, rankWithOnePair, highestRankUnpaired, secondHighestRankUnpaired, thirdHighestRankUnpaired):
        self.cards = cards
        self.rankWithOnePair = rankWithOnePair
        self.highestRankUnpaired = highestRankUnpaired
        self.secondHighestRankUnpaired = secondHighestRankUnpaired
        self.thirdHighestRankUnpaired = thirdHighestRankUnpaired

    def onePairRankWithOnePair(self):
        return self.rankWithOnePair

    def onePairHighestRankUnpaired(self):
        return self.highestRankUnpaired

    def onePairSecondHighestRankUnpaired(self):
        return self.secondHighestRankUnpaired

    def onePairThirdHighestRankUnpaired(self):
        return self.thirdHighestRankUnpaired

class PokerHandTwoPair(PokerHand):

    def __init__(self, cards, rankWithPairHigh, rankWithPairLow, otherRankUnpaired):
        self.cards = cards
        self.rankWithPairHigh = rankWithPairHigh
        self.rankWithPairLow = rankWithPairLow
        self.otherRankUnpaired = otherRankUnpaired

    def twoPairRankWithPairHigh(self):
        return self.rankWithPairHigh

    def twoPairRankWithPairLow(self):
        return self.rankWithPairLow

    def twoPairOtherRankUnpaired(self):
        return self.otherRankUnpaired

class PokerHandThreeOfAKind(PokerHand):

    def __init__(self, cards, rankWithThreeOfAKind, highRankUnpaired, lowRankUnpaired):
        self.cards = cards
        self.rankWithThreeOfAKind = rankWithThreeOfAKind
        self.highRankUnpaired = highRankUnpaired
        self.lowRankUnpaired = lowRankUnpaired

    def threeOfAKindRankWithThreeOfAKind(self):
        return self.rankWithThreeOfAKind

    def threeOfAKindHighRankUnpaired(self):
        return self.highRankUnpaired

    def threeOfAKindLowRankUnpaired(self):
        return self.lowRankUnpaired

class PokerHandStraight(PokerHand):

    def __init__(self, cards, rankWithHighEndOfStraight, rankWithLowEndOfStraight):
        self.cards = cards
        self.rankWithHighEndOfStraight = rankWithHighEndOfStraight
        self.rankWithLowEndOfStraight = rankWithLowEndOfStraight

    def straightRankWithHighEndOfStraight(self):
        return self.rankWithHighEndOfStraight

    def straightRankWithLowEndOfStraight(self):
        return self.rankWithLowEndOfStraight

class PokerHandFlush(PokerHand):

    def __init__(self, cards, highestRank, secondHighestRank, thirdHighestRank, fourthHighestRank, lowestRank, suitOfFlush):
        self.cards = cards
        self.highestRank = highestRank
        self.secondHighestRank = secondHighestRank
        self.thirdHighestRank = thirdHighestRank
        self.fourthHighestRank = fourthHighestRank
        self.lowestRank = lowestRank
        self.suitOfFlush = suitOfFlush

    def flushHighestRank(self):
        return self.highestRank

    def flushSecondHighestRank(self):
        return self.secondHighestRank

    def flushThirdHighestRank(self):
        return self.thirdHighestRank

    def flushFourthHighestRank(self):
        return self.fourthHighestRank

    def flushLowestRank(self):
        return self.lowestRank

class PokerHandFullHouse(PokerHand):

    def __init__(self, cards, rankWithThreeOfAKind, rankWithPair):
        self.cards = cards
        self.rankWithThreeOfAKind = rankWithThreeOfAKind
        self.rankWithPair = rankWithPair

    def fullHouseRankWithThreeOfAKind(self):
        return self.rankWithThreeOfAKind

    def fullHouseRankWithPair(self):
        return self.rankWithPair    

class PokerHandFourOfAKind(PokerHand):

    def __init__(self, cards, rankWithFourOfAKind, otherRankUnpaired):
        self.cards = cards
        self.rankWithFourOfAKind = rankWithFourOfAKind
        self.otherRankUnpaired = otherRankUnpaired

    def fourOfAKindRankWithFourOfAKind(self):
        return self.rankWithFourOfAKind

    def fourOfAKindOtherRankUnpaired(self):
        return self.otherRankUnpaired

class PokerHandStraightFlush(PokerHandStraight):

    def __init__(self, cards, rankWithHighEndOfStraight, rankWithLowEndOfStraight, suitOfFlush):
        self.cards = cards
        self.rankWithHighEndOfStraight = rankWithHighEndOfStraight
        self.rankWithLowEndOfStraight = rankWithLowEndOfStraight
        self.suitOfFlush = suitOfFlush

pokerHandTypes = [PokerHandHighCard, PokerHandOnePair, PokerHandTwoPair, PokerHandThreeOfAKind, PokerHandStraight, PokerHandFlush, PokerHandFullHouse, PokerHandFourOfAKind, PokerHandStraightFlush]

def pokerHandTypeBetter(pokerHandTypeA, pokerHandTypeB):
    pokerHandTypeAIndexInPokerHandTypes = pokerHandTypes.index(pokerHandTypeA)
    pokerHandTypeBIndexInPokerHandTypes = pokerHandTypes.index(pokerHandTypeB)
    pokerHandTypeABetterThanPokerHandTypeB = (pokerHandTypeAIndexInPokerHandTypes > pokerHandTypeBIndexInPokerHandTypes)
    return pokerHandTypeABetterThanPokerHandTypeB

def testPokerHandTypeBetter():
    pokerHandTypeA = PokerHandOnePair
    pokerHandTypeB = PokerHandHighCard
    assert pokerHandTypeBetter(pokerHandTypeA, pokerHandTypeB) == True

    pokerHandTypeA = PokerHandHighCard
    pokerHandTypeB = PokerHandHighCard
    assert pokerHandTypeBetter(pokerHandTypeA, pokerHandTypeB) == False

    pokerHandTypeA = PokerHandHighCard
    pokerHandTypeB = PokerHandOnePair
    assert pokerHandTypeBetter(pokerHandTypeA, pokerHandTypeB) == False

    pokerHandTypeA = PokerHandHighCard
    pokerHandTypeB = PokerHandTwoPair
    assert pokerHandTypeBetter(pokerHandTypeA, pokerHandTypeB) == False
    assert pokerHandTypeBetter(pokerHandTypeB, pokerHandTypeA) == True

    pokerHandTypeA = PokerHandOnePair
    pokerHandTypeB = PokerHandTwoPair
    assert pokerHandTypeBetter(pokerHandTypeA, pokerHandTypeB) == False
    assert pokerHandTypeBetter(pokerHandTypeB, pokerHandTypeA) == True

    pokerHandTypeA = PokerHandTwoPair
    pokerHandTypeB = PokerHandTwoPair
    assert pokerHandTypeBetter(pokerHandTypeA, pokerHandTypeB) == False
    assert pokerHandTypeBetter(pokerHandTypeB, pokerHandTypeA) == False

    # todo: add more comparisons here

def pokerHandBetter(pokerHandA, pokerHandB):
    if pokerHandBetterDueToHandType(pokerHandA, pokerHandB):
        return True, "{pokerHandAHandType} better than {pokerHandBHandType}".format(pokerHandAHandType=pokerHandA.handType(), pokerHandBHandType=pokerHandB.handType())
    elif pokerHandBetterDueToHandType(pokerHandB, pokerHandA):
        return False, "{pokerHandBHandType} better than {pokerHandAHandType}".format(pokerHandAHandType=pokerHandA.handType(), pokerHandBHandType=pokerHandB.handType())
    # so same hand type
    else:
        pokerHandABetterThanPokerHandBSameHandType, explanation = pokerHandBetterSameHandType(pokerHandA, pokerHandB)
        if pokerHandABetterThanPokerHandBSameHandType:
            return True, explanation
        # this repeats the same calculation. pokerHandBetterSameHandType should return the better of the two hands rather than a boolean
        if explanation != 'the hands are the same':
            pokerHandBBetterThanPokerHandASameHandType, explanation = pokerHandBetterSameHandType(pokerHandB, pokerHandA)
            if pokerHandBBetterThanPokerHandASameHandType:
                return False, explanation
        return False, explanation

def pokerHandBetterSameHandType(pokerHandA, pokerHandB):
    pokerHandAHandType = pokerHandA.handType()
    # pokerHandBHandType = pokerHandB.handType()
    if pokerHandAHandType == PokerHandHighCard:
        betterBoolean, explanation = pokerHandBetterSameHandTypeHighCard(pokerHandA, pokerHandB)
    elif pokerHandAHandType == PokerHandOnePair:
        betterBoolean, explanation = pokerHandBetterSameHandTypeOnePair(pokerHandA, pokerHandB)
    elif pokerHandAHandType == PokerHandTwoPair:
        betterBoolean, explanation = pokerHandBetterSameHandTypeTwoPair(pokerHandA, pokerHandB)
    elif pokerHandAHandType == PokerHandThreeOfAKind:
        betterBoolean, explanation = pokerHandBetterSameHandTypeThreeOfAKind(pokerHandA, pokerHandB)
    elif pokerHandAHandType == PokerHandStraight:
        betterBoolean, explanation = pokerHandBetterSameHandTypeStraight(pokerHandA, pokerHandB)
    elif pokerHandAHandType == PokerHandFlush:
        betterBoolean, explanation = pokerHandBetterSameHandTypeFlush(pokerHandA, pokerHandB)
    elif pokerHandAHandType == PokerHandFullHouse:
        betterBoolean, explanation = pokerHandBetterSameHandTypeFullHouse(pokerHandA, pokerHandB)
    elif pokerHandAHandType == PokerHandFourOfAKind:
        betterBoolean, explanation = pokerHandBetterSameHandTypeFourOfAKind(pokerHandA, pokerHandB)
    elif pokerHandAHandType == PokerHandStraightFlush:
        betterBoolean, explanation = pokerHandBetterSameHandTypeStraightFlush(pokerHandA, pokerHandB)
    else:
        raise ValueError("unknown hand type: {pokerHandAType}".format(pokerHandAType=pokerHandAType))
    return betterBoolean, explanation
    
def pokerHandBetterDueToHandType(pokerHandA, pokerHandB):
    pokerHandAHandType = pokerHandA.handType()
    pokerHandBHandType = pokerHandB.handType()
    pokerHandTypeBetterBoolean = pokerHandTypeBetter(pokerHandAHandType, pokerHandBHandType)
    return pokerHandTypeBetterBoolean

def pokerHandBetterSameHandTypeHighCard(pokerHandAHighCard, pokerHandBHighCard):
    # highest rank card has higher rank
    pokerHandAHighestRank = pokerHandAHighCard.highCardHighestRank()
    pokerHandBHighestRank = pokerHandBHighCard.highCardHighestRank()
    aHighestRankHigherRankThanBHighestRank = rankHigherThanRank(pokerHandAHighestRank, pokerHandBHighestRank)
    explanationSoFar = "both high card"
    explanationSuffixButCardHasHigherRankThanCard = ", but {oneCardRank} has higher rank than {otherCardRank}"
    if aHighestRankHigherRankThanBHighestRank:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandAHighestRank, otherCardRank=pokerHandBHighestRank)
        return True, explanation
    else:
        bHighestRankHigherRankThanAHighestRank = rankHigherThanRank(pokerHandBHighestRank, pokerHandAHighestRank)
        if bHighestRankHigherRankThanAHighestRank:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBHighestRank, otherCardRank=pokerHandAHighestRank)
            return False, explanation

    # second highest rank card has higher rank
    pokerHandASecondHighestRank = pokerHandAHighCard.highCardSecondHighestRank()
    pokerHandBSecondHighestRank = pokerHandBHighCard.highCardSecondHighestRank()
    aSecondHighestRankHigherRankThanBSecondHighestRank = rankHigherThanRank(pokerHandASecondHighestRank, pokerHandBSecondHighestRank)
    explanationSoFar += ", and highest card is same rank"
    if aSecondHighestRankHigherRankThanBSecondHighestRank:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandASecondHighestRank, otherCardRank=pokerHandBSecondHighestRank)
        return True, explanation
    else:
        bSecondHighestRankHigherRankThanASecondHighestRank = rankHigherThanRank(pokerHandBSecondHighestRank, pokerHandASecondHighestRank)
        if bSecondHighestRankHigherRankThanASecondHighestRank:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBSecondHighestRank, otherCardRank=pokerHandASecondHighestRank)
            return False, explanation

    # third highest rank card has higher rank
    pokerHandAThirdHighestRank = pokerHandAHighCard.highCardThirdHighestRank()
    pokerHandBThirdHighestRank = pokerHandBHighCard.highCardThirdHighestRank()
    aThirdHighestRankHigherRankThanBThirdHighestRank = rankHigherThanRank(pokerHandAThirdHighestRank, pokerHandBThirdHighestRank)
    explanationSoFar += ", and second highest card is same rank"
    if aThirdHighestRankHigherRankThanBThirdHighestRank:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandAThirdHighestRank, otherCardRank=pokerHandBThirdHighestRank)
        return True, explanation
    else:
        bThirdHighestRankHigherRankThanAThirdHighestRank = rankHigherThanRank(pokerHandBThirdHighestRank, pokerHandAThirdHighestRank)
        if bThirdHighestRankHigherRankThanAThirdHighestRank:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBThirdHighestRank, otherCardRank=pokerHandAThirdHighestRank)
            return False, explanation

    # fourth highest rank card has higher rank
    pokerHandAFourthHighestRank = pokerHandAHighCard.highCardFourthHighestRank()
    pokerHandBFourthHighestRank = pokerHandBHighCard.highCardFourthHighestRank()
    aFourthHighestRankHigherRankThanBFourthHighestRank = rankHigherThanRank(pokerHandAFourthHighestRank, pokerHandBFourthHighestRank)
    explanationSoFar += ", and third highest card is same rank"
    if aFourthHighestRankHigherRankThanBFourthHighestRank:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandAFourthHighestRank, otherCardRank=pokerHandBFourthHighestRank)
        return True, explanation
    else:
        bFourthHighestRankHigherRankThanAFourthHighestRank = rankHigherThanRank(pokerHandBFourthHighestRank, pokerHandAFourthHighestRank)
        if bFourthHighestRankHigherRankThanAFourthHighestRank:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBFourthHighestRank, otherCardRank=pokerHandAFourthHighestRank)
            return False, explanation

    # fifth highest rank card has higher rank
    pokerHandAFifthHighestRank = pokerHandAHighCard.highCardFifthHighestRank()
    pokerHandBFifthHighestRank = pokerHandBHighCard.highCardFifthHighestRank()
    aFifthHighestRankHigherRankThanBFifthHighestRank = rankHigherThanRank(pokerHandAFifthHighestRank, pokerHandBFifthHighestRank)
    explanationSoFar += ", and fourth highest card is same rank"
    if aFifthHighestRankHigherRankThanBFifthHighestRank:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandAFifthHighestRank, otherCardRank=pokerHandBFifthHighestRank)
        return True, explanation
    else:
        bFifthHighestRankHigherRankThanAFifthHighestRank = rankHigherThanRank(pokerHandBFifthHighestRank, pokerHandAFifthHighestRank)
        if bFifthHighestRankHigherRankThanAFifthHighestRank:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBFifthHighestRank, otherCardRank=pokerHandAFifthHighestRank)
            return False, explanation

    return False, "the hands are the same"
#    raise ValueError('have compared (1) highest rank cards, (2) second highest rank cards, (3) third highest rank cards, (4) fourth highest rank cards, (5) fifth highest rank cards, and did not get a result')

def pokerHandBetterSameHandTypeOnePair(pokerHandAOnePair, pokerHandBOnePair):
    # rank with one pair is higher
    pokerHandARankWithOnePair = pokerHandAOnePair.onePairRankWithOnePair()
    pokerHandBRankWithOnePair = pokerHandBOnePair.onePairRankWithOnePair()
    aRankWithOnePairHigherRankThanBRankWithOnePair = rankHigherThanRank(pokerHandARankWithOnePair, pokerHandBRankWithOnePair)
    explanationSoFar = "both one pair"
    explanationSuffixButCardHasHigherRankThanCard = ", but {oneCardRank} has higher rank than {otherCardRank}"
    if aRankWithOnePairHigherRankThanBRankWithOnePair:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandARankWithOnePair, otherCardRank=pokerHandBRankWithOnePair)
        return True, explanation
    else:
        bRankWithOnePairHigherRankThanARankWithOnePair = rankHigherThanRank(pokerHandBRankWithOnePair, pokerHandARankWithOnePair)
        if bRankWithOnePairHigherRankThanARankWithOnePair:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBRankWithOnePair, otherCardRank=pokerHandARankWithOnePair)
            return False, explanation

    # rank with one pair is same, and differ on highest card rank without pair
    pokerHandAHighestRankUnpaired = pokerHandAOnePair.onePairHighestRankUnpaired()
    pokerHandBHighestRankUnpaired = pokerHandBOnePair.onePairHighestRankUnpaired()
    explanationSoFar += ", and the rank of the pair is the same"
    aHighestRankUnpairedHigherRankThanBHighestRankUnpaired = rankHigherThanRank(pokerHandAHighestRankUnpaired, pokerHandBHighestRankUnpaired)
    if aHighestRankUnpairedHigherRankThanBHighestRankUnpaired:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandAHighestRankUnpaired, otherCardRank=pokerHandBHighestRankUnpaired)
        return True, explanation
    else:
        bHighestRankUnpairedHigherRankThanAHighestRankUnpaired = rankHigherThanRank(pokerHandBHighestRankUnpaired, pokerHandAHighestRankUnpaired)
        if bHighestRankUnpairedHigherRankThanAHighestRankUnpaired:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBHighestRankUnpaired, otherCardRank=pokerHandAHighestRankUnpaired)
            return False, explanation

    # rank with one pair is same, and highest card rank without pair is same, but differ on second highest card rank without pair
    pokerHandASecondHighestRankUnpaired = pokerHandAOnePair.onePairSecondHighestRankUnpaired()
    pokerHandBSecondHighestRankUnpaired = pokerHandBOnePair.onePairSecondHighestRankUnpaired()
    explanationSoFar += ", and the highest card rank without a pair is the same"
    aSecondHighestRankUnpairedHigherRankThanBSecondHighestRankUnpaired = rankHigherThanRank(pokerHandASecondHighestRankUnpaired, pokerHandBSecondHighestRankUnpaired)
    if aSecondHighestRankUnpairedHigherRankThanBSecondHighestRankUnpaired:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandASecondHighestRankUnpaired, otherCardRank=pokerHandBSecondHighestRankUnpaired)
        return True, explanation
    else:
        bSecondHighestRankUnpairedHigherRankThanASecondHighestRankUnpaired = rankHigherThanRank(pokerHandBSecondHighestRankUnpaired, pokerHandASecondHighestRankUnpaired)
        if bSecondHighestRankUnpairedHigherRankThanASecondHighestRankUnpaired:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBSecondHighestRankUnpaired, otherCardRank=pokerHandASecondHighestRankUnpaired)
            return False, explanation

    # rank with one pair is same, and highest card rank without pair is same, and second highest card rank without pair is same, but differ on third highest card rank without pair
    pokerHandAThirdHighestRankUnpaired = pokerHandAOnePair.onePairThirdHighestRankUnpaired()
    pokerHandBThirdHighestRankUnpaired = pokerHandBOnePair.onePairThirdHighestRankUnpaired()
    explanationSoFar += ", and the second highest card rank without a pair is the same"
    aThirdHighestRankUnpairedHigherRankThanBThirdHighestRankUnpaired = rankHigherThanRank(pokerHandAThirdHighestRankUnpaired, pokerHandBThirdHighestRankUnpaired)
    if aThirdHighestRankUnpairedHigherRankThanBThirdHighestRankUnpaired:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandAThirdHighestRankUnpaired, otherCardRank=pokerHandBThirdHighestRankUnpaired)
        return True, explanation
    else:
        bThirdHighestRankUnpairedHigherRankThanAThirdHighestRankUnpaired = rankHigherThanRank(pokerHandBThirdHighestRankUnpaired, pokerHandAThirdHighestRankUnpaired)
        if bThirdHighestRankUnpairedHigherRankThanAThirdHighestRankUnpaired:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBThirdHighestRankUnpaired, otherCardRank=pokerHandAThirdHighestRankUnpaired)
            return False, explanation

    return False, "the hands are the same"

def pokerHandBetterSameHandTypeTwoPair(pokerHandATwoPair, pokerHandBTwoPair):
    # pair of high rank is higher
    pokerHandARankWithPairHigh = pokerHandATwoPair.twoPairRankWithPairHigh()
    pokerHandBRankWithPairHigh = pokerHandBTwoPair.twoPairRankWithPairHigh()
    aRankWithPairHighHigherRankThanBRankWithPairHigh = rankHigherThanRank(pokerHandARankWithPairHigh, pokerHandBRankWithPairHigh)
    explanationSoFar = "both two pair"
    explanationSuffixButCardHasHigherRankThanCard = ", but {oneCardRank} has higher rank than {otherCardRank}"
    if aRankWithPairHighHigherRankThanBRankWithPairHigh:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandARankWithPairHigh, otherCardRank=pokerHandBRankWithPairHigh)
        return True, explanation
    else:
        bRankWithPairHighHigherRankThanARankWithPairHigh = rankHigherThanRank(pokerHandBRankWithPairHigh, pokerHandARankWithPairHigh)
        if bRankWithPairHighHigherRankThanARankWithPairHigh:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBRankWithPairHigh, otherCardRank=pokerHandARankWithPairHigh)
            return False, explanation

    # pair of high rank is same and pair of low rank is higher
    pokerHandARankWithPairLow = pokerHandATwoPair.twoPairRankWithPairLow()
    pokerHandBRankWithPairLow = pokerHandBTwoPair.twoPairRankWithPairLow()
    aRankWithPairLowHigherRankThanBRankWithPairLow = rankHigherThanRank(pokerHandARankWithPairLow, pokerHandBRankWithPairLow)
    explanationSoFar += ", and rank of high pair is the same"
    explanationSuffixButCardHasHigherRankThanCard = ", but {oneCardRank} has higher rank than {otherCardRank}"
    if aRankWithPairLowHigherRankThanBRankWithPairLow:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandARankWithPairLow, otherCardRank=pokerHandBRankWithPairLow)
        return True, explanation
    else:
        bRankWithPairLowHigherRankThanARankWithPairLow = rankHigherThanRank(pokerHandBRankWithPairLow, pokerHandARankWithPairLow)
        if bRankWithPairLowHigherRankThanARankWithPairLow:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBRankWithPairLow, otherCardRank=pokerHandARankWithPairLow)
            return False, explanation
    
    # rank with high pair is same, and rank with low pair is same, and differ on highest card rank without pair
    pokerHandAOtherRankUnpaired = pokerHandATwoPair.twoPairOtherRankUnpaired()
    pokerHandBOtherRankUnpaired = pokerHandBTwoPair.twoPairOtherRankUnpaired()
    explanationSoFar += ", and the rank of the low pair is the same"
    aOtherRankUnpairedHigherRankThanBOtherRankUnpaired = rankHigherThanRank(pokerHandAOtherRankUnpaired, pokerHandBOtherRankUnpaired)
    if aOtherRankUnpairedHigherRankThanBOtherRankUnpaired:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandAOtherRankUnpaired, otherCardRank=pokerHandBOtherRankUnpaired)
        return True, explanation
    else:
        bOtherRankUnpairedHigherRankThanAOtherRankUnpaired = rankHigherThanRank(pokerHandBOtherRankUnpaired, pokerHandAOtherRankUnpaired)
        if bOtherRankUnpairedHigherRankThanAOtherRankUnpaired:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBOtherRankUnpaired, otherCardRank=pokerHandAOtherRankUnpaired)
            return False, explanation

    return False, "the hands are the same"

def pokerHandBetterSameHandTypeThreeOfAKind(pokerHandAThreeOfAKind, pokerHandBThreeOfAKind):
    # rank of three of a kind is higher
    pokerHandARankWithThreeOfAKind = pokerHandAThreeOfAKind.threeOfAKindRankWithThreeOfAKind()
    pokerHandBRankWithThreeOfAKind = pokerHandBThreeOfAKind.threeOfAKindRankWithThreeOfAKind()
    aRankWithThreeOfAKindHigherRankThanBRankWithThreeOfAKind = rankHigherThanRank(pokerHandARankWithThreeOfAKind, pokerHandBRankWithThreeOfAKind)
    explanationSoFar = "both three of a kind"
    explanationSuffixButCardHasHigherRankThanCard = ", but {oneCardRank} has higher rank than {otherCardRank}"
    if aRankWithThreeOfAKindHigherRankThanBRankWithThreeOfAKind:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandARankWithThreeOfAKind, otherCardRank=pokerHandBRankWithThreeOfAKind)
        return True, explanation
    else:
        bRankWithThreeOfAKindHigherRankThanARankWithThreeOfAKind = rankHigherThanRank(pokerHandBRankWithThreeOfAKind, pokerHandARankWithThreeOfAKind)
        if bRankWithThreeOfAKindHigherRankThanARankWithThreeOfAKind:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBRankWithThreeOfAKind, otherCardRank=pokerHandARankWithThreeOfAKind)
            return False, explanation

    # pair of three of a kind is same and high card rank unpaired is higher
    pokerHandAHighRankUnpaired = pokerHandAThreeOfAKind.threeOfAKindHighRankUnpaired()
    pokerHandBHighRankUnpaired = pokerHandBThreeOfAKind.threeOfAKindHighRankUnpaired()
    aHighRankUnpairedHigherRankThanBHighRankUnpaired = rankHigherThanRank(pokerHandAHighRankUnpaired, pokerHandBHighRankUnpaired)
    explanationSoFar += ", and rank of three of a kind is the same"
    explanationSuffixButCardHasHigherRankThanCard = ", but {oneCardRank} has higher rank than {otherCardRank}"
    if aHighRankUnpairedHigherRankThanBHighRankUnpaired:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandAHighRankUnpaired, otherCardRank=pokerHandBHighRankUnpaired)
        return True, explanation
    else:
        bHighRankUnpairedHigherRankThanAHighRankUnpaired = rankHigherThanRank(pokerHandBHighRankUnpaired, pokerHandAHighRankUnpaired)
        if bHighRankUnpairedHigherRankThanAHighRankUnpaired:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBHighRankUnpaired, otherCardRank=pokerHandAHighRankUnpaired)
            return False, explanation
    
    # pair of three of a kind is same and high card rank unpaired is same and low card rank unpaired is higher
    pokerHandALowRankUnpaired = pokerHandAThreeOfAKind.threeOfAKindLowRankUnpaired()
    pokerHandBLowRankUnpaired = pokerHandBThreeOfAKind.threeOfAKindLowRankUnpaired()
    aLowRankUnpairedHigherRankThanBLowRankUnpaired = rankHigherThanRank(pokerHandALowRankUnpaired, pokerHandBLowRankUnpaired)
    explanationSoFar += ", and rank of three of a kind is the same"
    explanationSuffixButCardHasHigherRankThanCard = ", but {oneCardRank} has higher rank than {otherCardRank}"
    if aLowRankUnpairedHigherRankThanBLowRankUnpaired:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandALowRankUnpaired, otherCardRank=pokerHandBLowRankUnpaired)
        return True, explanation
    else:
        bLowRankUnpairedHigherRankThanALowRankUnpaired = rankHigherThanRank(pokerHandBLowRankUnpaired, pokerHandALowRankUnpaired)
        if aLowRankUnpairedHigherRankThanBLowRankUnpaired:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBLowRankUnpaired, otherCardRank=pokerHandALowRankUnpaired)
            return False, explanation

    return False, "the hands are the same"

def pokerHandBetterSameHandTypeStraight(pokerHandAStraight, pokerHandBStraight):
    pokerHandAStraightRankWithHighEndOfStraight = pokerHandAStraight.straightRankWithHighEndOfStraight()
    pokerHandBStraightRankWithHighEndOfStraight = pokerHandBStraight.straightRankWithHighEndOfStraight()
    aRankWithHighEndOfStraightHigherRankThanBRankWithHighEndOfStraight = rankHigherThanRank(pokerHandAStraightRankWithHighEndOfStraight, pokerHandBStraightRankWithHighEndOfStraight)
    explanationSoFar = "both straight"
    explanationSuffixButCardHasHigherRankThanCard = ", but {oneCardRank} has higher rank than {otherCardRank}"
    if aRankWithHighEndOfStraightHigherRankThanBRankWithHighEndOfStraight:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandAStraightRankWithHighEndOfStraight, otherCardRank=pokerHandBStraightRankWithHighEndOfStraight)
        return True, explanation
    else:
        bRankWithHighEndOfStraightHigherRankThanARankWithHighEndOfStraight = rankHigherThanRank(pokerHandBStraightRankWithHighEndOfStraight, pokerHandAStraightRankWithHighEndOfStraight)
        if bRankWithHighEndOfStraightHigherRankThanARankWithHighEndOfStraight:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBStraightRankWithHighEndOfStraight, otherCardRank=pokerHandAStraightRankWithHighEndOfStraight)
            return False, explanation

    return False, "the hands are the same"

def pokerHandBetterSameHandTypeFlush(pokerHandAFlush, pokerHandBFlush):
    pokerHandAHighestRank = pokerHandAFlush.flushHighestRank()
    pokerHandBHighestRank = pokerHandBFlush.flushHighestRank()
    aHighestRankHigherRankThanBHighestRank = rankHigherThanRank(pokerHandAHighestRank, pokerHandBHighestRank)
    explanationSoFar = "both flush"
    explanationSuffixButCardHasHigherRankThanCard = ", but {oneCardRank} has higher rank than {otherCardRank}"
    if aHighestRankHigherRankThanBHighestRank:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandAHighestRank, otherCardRank=pokerHandBHighestRank)
        return True, explanation
    else:
        bHighestRankHigherRankThanAHighestRank = rankHigherThanRank(pokerHandBHighestRank, pokerHandAHighestRank)
        if bHighestRankHigherRankThanAHighestRank:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBHighestRank, otherCardRank=pokerHandAHighestRank)
            return False, explanation

    # second highest rank card has higher rank
    pokerHandASecondHighestRank = pokerHandAFlush.flushSecondHighestRank()
    pokerHandBSecondHighestRank = pokerHandBFlush.flushSecondHighestRank()
    aSecondHighestRankHigherRankThanBSecondHighestRank = rankHigherThanRank(pokerHandASecondHighestRank, pokerHandBSecondHighestRank)
    explanationSoFar += ", and highest card is same rank"
    if aSecondHighestRankHigherRankThanBSecondHighestRank:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandASecondHighestRank, otherCardRank=pokerHandBSecondHighestRank)
        return True, explanation
    else:
        bSecondHighestRankHigherRankThanASecondHighestRank = rankHigherThanRank(pokerHandBSecondHighestRank, pokerHandASecondHighestRank)
        if bSecondHighestRankHigherRankThanASecondHighestRank:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBSecondHighestRank, otherCardRank=pokerHandASecondHighestRank)
            return False, explanation

    # third highest rank card has higher rank
    pokerHandAThirdHighestRank = pokerHandAFlush.flushThirdHighestRank()
    pokerHandBThirdHighestRank = pokerHandBFlush.flushThirdHighestRank()
    aThirdHighestRankHigherRankThanBThirdHighestRank = rankHigherThanRank(pokerHandAThirdHighestRank, pokerHandBThirdHighestRank)
    explanationSoFar += ", and second highest card is same rank"
    if aThirdHighestRankHigherRankThanBThirdHighestRank:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandAThirdHighestRank, otherCardRank=pokerHandBThirdHighestRank)
        return True, explanation
    else:
        bThirdHighestRankHigherRankThanAThirdHighestRank = rankHigherThanRank(pokerHandBThirdHighestRank, pokerHandAThirdHighestRank)
        if bThirdHighestRankHigherRankThanAThirdHighestRank:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBThirdHighestRank, otherCardRank=pokerHandAThirdHighestRank)
            return False, explanation

    # fourth highest rank card has higher rank
    pokerHandAFourthHighestRank = pokerHandAFlush.flushFourthHighestRank()
    pokerHandBFourthHighestRank = pokerHandBFlush.flushFourthHighestRank()
    aFourthHighestRankHigherRankThanBFourthHighestRank = rankHigherThanRank(pokerHandAFourthHighestRank, pokerHandBFourthHighestRank)
    explanationSoFar += ", and third highest card is same rank"
    if aFourthHighestRankHigherRankThanBFourthHighestRank:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandAFourthHighestRank, otherCardRank=pokerHandBFourthHighestRank)
        return True, explanation
    else:
        bFourthHighestRankHigherRankThanAFourthHighestRank = rankHigherThanRank(pokerHandBFourthHighestRank, pokerHandAFourthHighestRank)
        if bFourthHighestRankHigherRankThanAFourthHighestRank:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBFourthHighestRank, otherCardRank=pokerHandAFourthHighestRank)
            return False, explanation

    # fifth highest rank card has higher rank
    pokerHandALowestRank = pokerHandAFlush.flushLowestRank()
    pokerHandBLowestRank = pokerHandBFlush.flushLowestRank()
    aLowestRankHigherRankThanBLowestRank = rankHigherThanRank(pokerHandALowestRank, pokerHandBLowestRank)
    explanationSoFar += ", and fourth highest card is same rank"
    if aLowestRankHigherRankThanBLowestRank:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandALowestRank, otherCardRank=pokerHandBLowestRank)
        return True, explanation
    else:
        bLowestRankHigherRankThanALowestRank = rankHigherThanRank(pokerHandBLowestRank, pokerHandALowestRank)
        if bLowestRankHigherRankThanALowestRank:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBLowestRank, otherCardRank=pokerHandALowestRank)
            return False, explanation

    return False, "the hands are the same"
    
def pokerHandBetterSameHandTypeFullHouse(pokerHandAFullHouse, pokerHandBFullHouse):
    # rank with three of a kind higher than rank with three of a kind
    pokerHandARankWithThreeOfAKind = pokerHandAFullHouse.fullHouseRankWithThreeOfAKind()
    pokerHandBRankWithThreeOfAKind = pokerHandBFullHouse.fullHouseRankWithThreeOfAKind()
    aRankWithThreeOfAKindHigherRankThanBRankWithThreeOfAKind = rankHigherThanRank(pokerHandARankWithThreeOfAKind, pokerHandBRankWithThreeOfAKind)
    explanationSoFar = "both full house"
    explanationSuffixButCardHasHigherRankThanCard = ", but {oneCardRank} has higher rank than {otherCardRank}"
    if aRankWithThreeOfAKindHigherRankThanBRankWithThreeOfAKind:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandARankWithThreeOfAKind, otherCardRank=pokerHandBRankWithThreeOfAKind)
        return True, explanation
    else:
        bRankWithThreeOfAKindHigherRankThanARankWithThreeOfAKind = rankHigherThanRank(pokerHandBRankWithThreeOfAKind, pokerHandARankWithThreeOfAKind)
        if bRankWithThreeOfAKindHigherRankThanARankWithThreeOfAKind:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBRankWithThreeOfAKind, otherCardRank=pokerHandARankWithThreeOfAKind)
            return False, explanation

    # rank with three of a kind same, but rank with pair higher than rank with pair
    pokerHandARankWithPair = pokerHandAFullHouse.fullHouseRankWithPair()
    pokerHandBRankWithPair = pokerHandBFullHouse.fullHouseRankWithPair()
    aRankWithPairHigherRankThanBRankWithPair = rankHigherThanRank(pokerHandARankWithPair, pokerHandBRankWithPair)
    explanationSoFar += ", and rank with three of a kind is the same"
    if aRankWithPairHigherRankThanBRankWithPair:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandARankWithPair, otherCardRank=pokerHandBRankWithPair)
        return True, explanation
    else:
        bRankWithPairHigherRankThanARankWithPair = rankHigherThanRank(pokerHandBRankWithPair, pokerHandARankWithPair)
        if bRankWithPairHigherRankThanARankWithPair:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBRankWithPair, otherCardRank=pokerHandARankWithPair)
            return False, explanation

    return False, "the hands are the same"

def pokerHandBetterSameHandTypeFourOfAKind(pokerHandAFourOfAKind, pokerHandBFourOfAKind):
    # rank with four of a kind is higher
    pokerHandARankWithFourOfAKind = pokerHandAFourOfAKind.fourOfAKindRankWithFourOfAKind()
    pokerHandBRankWithFourOfAKind = pokerHandBFourOfAKind.fourOfAKindRankWithFourOfAKind()
    aRankWithFourOfAKindHigherRankThanBRankWithFourOfAKind = rankHigherThanRank(pokerHandARankWithFourOfAKind, pokerHandBRankWithFourOfAKind)
    explanationSoFar = "both four of a kind"
    explanationSuffixButCardHasHigherRankThanCard = ", but {oneCardRank} has higher rank than {otherCardRank}"
    if aRankWithFourOfAKindHigherRankThanBRankWithFourOfAKind:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandARankWithFourOfAKind, otherCardRank=pokerHandBRankWithFourOfAKind)
        return True, explanation
    else:
        bRankWithFourOfAKindHigherRankThanARankWithFourOfAKind = rankHigherThanRank(pokerHandBRankWithFourOfAKind, pokerHandARankWithFourOfAKind)
        if bRankWithFourOfAKindHigherRankThanARankWithFourOfAKind:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBRankWithFourOfAKind, otherCardRank=pokerHandARankWithFourOfAKind)
            return False, explanation

    # rank with four of a kind is same and high card rank unpaired is higher
    pokerHandAOtherRankUnpaired = pokerHandAFourOfAKind.fourOfAKindOtherRankUnpaired()
    pokerHandBOtherRankUnpaired = pokerHandBFourOfAKind.fourOfAKindOtherRankUnpaired()
    aOtherRankUnpairedHigherRankThanBOtherRankUnpaired = rankHigherThanRank(pokerHandAOtherRankUnpaired, pokerHandBOtherRankUnpaired)
    explanationSoFar += ", and rank of four of a kind is the same"
    explanationSuffixButCardHasHigherRankThanCard = ", but {oneCardRank} has higher rank than {otherCardRank}"
    if aOtherRankUnpairedHigherRankThanBOtherRankUnpaired:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandAOtherRankUnpaired, otherCardRank=pokerHandBOtherRankUnpaired)
        return True, explanation
    else:
        aOtherRankUnpairedHigherRankThanBOtherRankUnpaired = rankHigherThanRank(pokerHandBOtherRankUnpaired, pokerHandAOtherRankUnpaired)
        if aOtherRankUnpairedHigherRankThanBOtherRankUnpaired:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBOtherRankUnpaired, otherCardRank=pokerHandAOtherRankUnpaired)
            return False, explanation
        
    return False, "the hands are the same"

def pokerHandBetterSameHandTypeStraightFlush(pokerHandAStraightFlush, pokerHandBStraightFlush):
#    could, do but explanation would have "straight" rather than "straight flush".
#    to resolve that, could make a field for the hand type and get that string rather than hard-coding the string in explanationSoFar
#    better, explanation = pokerHandBetterSameHandTypeStraight(pokerHandAStraightFlush, pokerHandBStraightFlush)
#    return better, explanation
    pokerHandAStraightFlushRankWithHighEndOfStraightFlush = pokerHandAStraightFlush.straightRankWithHighEndOfStraight()
    pokerHandBStraightFlushRankWithHighEndOfStraightFlush = pokerHandBStraightFlush.straightRankWithHighEndOfStraight()
    aRankWithHighEndOfStraightFlushHigherRankThanBRankWithHighEndOfStraightFlush = rankHigherThanRank(pokerHandAStraightFlushRankWithHighEndOfStraightFlush, pokerHandBStraightFlushRankWithHighEndOfStraightFlush)
    explanationSoFar = "both straight flush"
    explanationSuffixButCardHasHigherRankThanCard = ", but {oneCardRank} has higher rank than {otherCardRank}"
    if aRankWithHighEndOfStraightFlushHigherRankThanBRankWithHighEndOfStraightFlush:
        explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandAStraightFlushRankWithHighEndOfStraightFlush, otherCardRank=pokerHandBStraightFlushRankWithHighEndOfStraightFlush)
        return True, explanation
    else:
        bRankWithHighEndOfStraightFlushHigherRankThanARankWithHighEndOfStraightFlush = rankHigherThanRank(pokerHandBStraightFlushRankWithHighEndOfStraightFlush, pokerHandAStraightFlushRankWithHighEndOfStraightFlush)
        if bRankWithHighEndOfStraightFlushHigherRankThanARankWithHighEndOfStraightFlush:
            explanation = explanationSoFar + explanationSuffixButCardHasHigherRankThanCard.format(oneCardRank=pokerHandBStraightFlushRankWithHighEndOfStraightFlush, otherCardRank=pokerHandAStraightFlushRankWithHighEndOfStraightFlush)
            return False, explanation

    return False, "the hands are the same"

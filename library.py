from tests import *

def runTests():
    testPokerHandTypeBetter()
    testPokerHandBetterDueToHandType()
    testPokerHandBetterSameHandTypeHighCard()
    testPokerHandBetterSameHandTypeOnePair()
    testPokerHandBetterSameHandTypeTwoPair()
    testPokerHandBetterSameHandTypeThreeOfAKind()
    testPokerHandBetterSameHandTypeStraight()
    testPokerHandBetterSameHandTypeFlush()
    testPokerHandBetterSameHandTypeFullHouse()
    testPokerHandBetterSameHandTypeFourOfAKind()
    testPokerHandBetterSameHandTypeStraightFlush()
    testPokerHandBetter()
    print('success')

if __name__ == '__main__':
    import sys
    firstArg = None
    if len(sys.argv) > 1:
        firstArg = sys.argv[1]
    if firstArg == 'test':
        runTests()
    else:
        print('hello')

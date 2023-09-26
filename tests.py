from findPokerHand import *

#import pdb     # https://docs.python.org/3/library/pdb.html
#pdb.set_trace()

def testPokerHandBetterDueToHandType():
    pokerHandACard1 = two_of_hearts
    pokerHandACard2 = two_of_clubs
    pokerHandACard3 = jack_of_diamonds
    pokerHandACard4 = ten_of_clubs
    pokerHandACard5 = four_of_hearts
    pokerHandACards = [pokerHandACard1, pokerHandACard2, pokerHandACard3, pokerHandACard4, pokerHandACard5]
    pokerHandBCard1 = two_of_spades
    pokerHandBCard2 = three_of_spades
    pokerHandBCard3 = five_of_diamonds
    pokerHandBCard4 = six_of_diamonds
    pokerHandBCard5 = eight_of_hearts
    pokerHandBCards = [pokerHandBCard1, pokerHandBCard2, pokerHandBCard3, pokerHandBCard4, pokerHandBCard5]
    pokerHandA = PokerHandOnePair(pokerHandACards, "two", pokerHandACard3, pokerHandACard4, pokerHandACard5)
    pokerHandOnePair = pokerHandA
    pokerHandB = PokerHandHighCard(pokerHandBCards, pokerHandBCard5, pokerHandBCard4, pokerHandBCard3, pokerHandBCard2, pokerHandBCard1)
    pokerHandHighCard = pokerHandB
    assert pokerHandBetterDueToHandType(pokerHandOnePair, pokerHandHighCard) == True

    assert pokerHandBetterDueToHandType(pokerHandHighCard, pokerHandOnePair) == False
    
    assert type(findBestPokerHand(pokerHandACards)) == PokerHandOnePair

    assert type(findBestPokerHand(pokerHandBCards)) == PokerHandHighCard
    
def testPokerHandBetterSameHandTypeHighCard():
    pokerHandACard1 = two_of_hearts
    pokerHandACard2 = three_of_clubs
    pokerHandACard3 = jack_of_diamonds
    pokerHandACard4 = ten_of_clubs
    pokerHandACard5 = four_of_hearts
    pokerHandACards = [pokerHandACard1, pokerHandACard2, pokerHandACard3, pokerHandACard4, pokerHandACard5]
    pokerHandBCard1 = two_of_spades
    pokerHandBCard2 = three_of_spades
    pokerHandBCard3 = five_of_diamonds
    pokerHandBCard4 = six_of_diamonds
    pokerHandBCard5 = eight_of_hearts
    pokerHandBCards = [pokerHandBCard1, pokerHandBCard2, pokerHandBCard3, pokerHandBCard4, pokerHandBCard5]
    pokerHandA = PokerHandHighCard(pokerHandACards, pokerHandACard3.cardRank(), pokerHandACard4.cardRank(), pokerHandACard5.cardRank(), pokerHandACard2.cardRank(), pokerHandACard1.cardRank())
    pokerHandAHighCard = pokerHandA
    pokerHandB = PokerHandHighCard(pokerHandBCards, pokerHandBCard5.cardRank(), pokerHandBCard4.cardRank(), pokerHandBCard3.cardRank(), pokerHandBCard2.cardRank(), pokerHandBCard1.cardRank())
    pokerHandBHighCard = pokerHandB

    assert pokerHandBetterSameHandTypeHighCard(pokerHandAHighCard, pokerHandBHighCard) == (True, "both high card, but jack has higher rank than eight")

    assert pokerHandBetterSameHandTypeHighCard(pokerHandBHighCard, pokerHandAHighCard) == (False, "both high card, but jack has higher rank than eight")

    assert pokerHandBetterSameHandTypeHighCard(pokerHandAHighCard, pokerHandAHighCard) == (False, "the hands are the same")

    assert type(findBestPokerHand(pokerHandACards)) == PokerHandHighCard

    assert type(findBestPokerHand(pokerHandBCards)) == PokerHandHighCard


def testPokerHandBetterSameHandTypeOnePair():
    pokerHandACard1 = two_of_hearts
    pokerHandACard2 = two_of_clubs
    pokerHandACard3 = jack_of_diamonds
    pokerHandACard4 = ten_of_clubs
    pokerHandACard5 = four_of_hearts
    pokerHandACards = [pokerHandACard1, pokerHandACard2, pokerHandACard3, pokerHandACard4, pokerHandACard5]
    pokerHandBCard1 = two_of_spades
    pokerHandBCard2 = two_of_diamonds
    pokerHandBCard3 = five_of_diamonds
    pokerHandBCard4 = six_of_diamonds
    pokerHandBCard5 = eight_of_hearts
    pokerHandBCards = [pokerHandBCard1, pokerHandBCard2, pokerHandBCard3, pokerHandBCard4, pokerHandBCard5]
    pokerHandA = PokerHandOnePair(pokerHandACards, "two", pokerHandACard3.cardRank(), pokerHandACard4.cardRank(), pokerHandACard5.cardRank())
    pokerHandAOnePair = pokerHandA
    pokerHandB = PokerHandOnePair(pokerHandBCards, "two", pokerHandBCard5.cardRank(), pokerHandBCard4.cardRank(), pokerHandBCard3.cardRank())
    pokerHandBOnePair = pokerHandB
    assert pokerHandBetterSameHandTypeOnePair(pokerHandAOnePair, pokerHandBOnePair) == (True, "both one pair, and the rank of the pair is the same, but jack has higher rank than eight")

    assert pokerHandBetterSameHandTypeOnePair(pokerHandBOnePair, pokerHandAOnePair) == (False, "both one pair, and the rank of the pair is the same, but jack has higher rank than eight")

    assert pokerHandBetterSameHandTypeOnePair(pokerHandAOnePair, pokerHandAOnePair) == (False, "the hands are the same")

    assert type(findBestPokerHand(pokerHandACards)) == PokerHandOnePair

    assert type(findBestPokerHand(pokerHandBCards)) == PokerHandOnePair

def testPokerHandBetterSameHandTypeTwoPair():
    pokerHandACard1 = two_of_hearts
    pokerHandACard2 = two_of_clubs
    pokerHandACard3 = jack_of_diamonds
    pokerHandACard4 = jack_of_clubs
    pokerHandACard5 = four_of_hearts
    pokerHandACards = [pokerHandACard1, pokerHandACard2, pokerHandACard3, pokerHandACard4, pokerHandACard5]
    pokerHandBCard1 = two_of_spades
    pokerHandBCard2 = two_of_diamonds
    pokerHandBCard3 = five_of_diamonds
    pokerHandBCard4 = five_of_spades
    pokerHandBCard5 = eight_of_hearts
    pokerHandBCards = [pokerHandBCard1, pokerHandBCard2, pokerHandBCard3, pokerHandBCard4, pokerHandBCard5]
    pokerHandA = PokerHandTwoPair(pokerHandACards, "jack", "two", pokerHandACard5.cardRank())
    pokerHandATwoPair = pokerHandA
    pokerHandB = PokerHandTwoPair(pokerHandBCards, "five", "two", pokerHandBCard5.cardRank())
    pokerHandBTwoPair = pokerHandB
    assert pokerHandBetterSameHandTypeTwoPair(pokerHandATwoPair, pokerHandBTwoPair) == (True, "both two pair, but jack has higher rank than five")

    assert pokerHandBetterSameHandTypeTwoPair(pokerHandBTwoPair, pokerHandATwoPair) == (False, "both two pair, but jack has higher rank than five")

    assert pokerHandBetterSameHandTypeTwoPair(pokerHandATwoPair, pokerHandATwoPair) == (False, "the hands are the same")

    # add tests for: 
    # - both two pair, and high rank is same, and low rank differs
    # - both two pair, and both ranks are same, and high card differs

    assert type(findBestPokerHand(pokerHandACards)) == PokerHandTwoPair

    assert type(findBestPokerHand(pokerHandBCards)) == PokerHandTwoPair

def testPokerHandBetterSameHandTypeThreeOfAKind():
    # these hands can share cards because both hands may be using one of the cards from the board
    pokerHandACard1 = two_of_hearts
    pokerHandACard2 = two_of_clubs
    pokerHandACard3 = two_of_spades
    pokerHandACard4 = jack_of_clubs
    pokerHandACard5 = four_of_hearts
    pokerHandACards = [pokerHandACard1, pokerHandACard2, pokerHandACard3, pokerHandACard4, pokerHandACard5]
    pokerHandBCard1 = two_of_spades
    pokerHandBCard2 = two_of_diamonds
    pokerHandBCard3 = two_of_hearts
    pokerHandBCard4 = five_of_spades
    pokerHandBCard5 = eight_of_hearts
    pokerHandBCards = [pokerHandBCard1, pokerHandBCard2, pokerHandBCard3, pokerHandBCard4, pokerHandBCard5]
    pokerHandA = PokerHandThreeOfAKind(pokerHandACards, "two", pokerHandACard4.cardRank(), pokerHandACard5.cardRank())
    pokerHandAThreeOfAKind = pokerHandA
    pokerHandB = PokerHandThreeOfAKind(pokerHandBCards, "two", pokerHandBCard5.cardRank(), pokerHandBCard4.cardRank())
    pokerHandBThreeOfAKind = pokerHandB

    assert pokerHandBetterSameHandTypeThreeOfAKind(pokerHandAThreeOfAKind, pokerHandBThreeOfAKind) == (True, "both three of a kind, and rank of three of a kind is the same, but jack has higher rank than eight")

    assert pokerHandBetterSameHandTypeThreeOfAKind(pokerHandBThreeOfAKind, pokerHandAThreeOfAKind) == (False, "both three of a kind, and rank of three of a kind is the same, but jack has higher rank than eight")

    assert pokerHandBetterSameHandTypeThreeOfAKind(pokerHandAThreeOfAKind, pokerHandAThreeOfAKind) == (False, "the hands are the same")

    # add tests for:
    # - three of a kind rank differs
    # - three of a kind rank same, and high card same, but low card differs

    #print(findBestPokerHand(pokerHandACards))

    assert type(findBestPokerHand(pokerHandACards)) == PokerHandThreeOfAKind

    assert type(findBestPokerHand(pokerHandBCards)) == PokerHandThreeOfAKind


def testPokerHandBetterSameHandTypeStraight():
    pokerHandACard1 = two_of_hearts
    pokerHandACard2 = three_of_clubs
    pokerHandACard3 = four_of_spades
    pokerHandACard4 = five_of_clubs
    pokerHandACard5 = six_of_hearts
    pokerHandACards = [pokerHandACard1, pokerHandACard2, pokerHandACard3, pokerHandACard4, pokerHandACard5]
    pokerHandBCard1 = four_of_clubs
    pokerHandBCard2 = five_of_spades
    pokerHandBCard3 = six_of_diamonds
    pokerHandBCard4 = seven_of_spades
    pokerHandBCard5 = eight_of_hearts
    pokerHandBCards = [pokerHandBCard1, pokerHandBCard2, pokerHandBCard3, pokerHandBCard4, pokerHandBCard5]
    pokerHandA = PokerHandStraight(pokerHandACards, "six", "two")
    pokerHandAStraight = pokerHandA
    pokerHandB = PokerHandStraight(pokerHandBCards, "eight", "four")
    pokerHandBStraight = pokerHandB

    assert pokerHandBetterSameHandTypeStraight(pokerHandAStraight, pokerHandBStraight) == (False, "both straight, but eight has higher rank than six")

    assert pokerHandBetterSameHandTypeStraight(pokerHandBStraight, pokerHandAStraight) == (True, "both straight, but eight has higher rank than six")

    assert pokerHandBetterSameHandTypeStraight(pokerHandAStraight, pokerHandAStraight) == (False, "the hands are the same")    

    assert type(findBestPokerHand(pokerHandACards)) == PokerHandStraight

    assert type(findBestPokerHand(pokerHandBCards)) == PokerHandStraight


def testPokerHandBetterSameHandTypeFlush():
    pokerHandACard1 = two_of_hearts
    pokerHandACard2 = four_of_hearts
    pokerHandACard3 = six_of_hearts
    pokerHandACard4 = eight_of_hearts
    pokerHandACard5 = ten_of_hearts
    pokerHandACards = [pokerHandACard1, pokerHandACard2, pokerHandACard3, pokerHandACard4, pokerHandACard5]
    pokerHandBCard1 = two_of_hearts
    pokerHandBCard2 = four_of_hearts
    pokerHandBCard3 = six_of_hearts
    pokerHandBCard4 = ten_of_hearts
    pokerHandBCard5 = jack_of_hearts
    pokerHandBCards = [pokerHandBCard1, pokerHandBCard2, pokerHandBCard3, pokerHandBCard4, pokerHandBCard5]
    pokerHandA = PokerHandFlush(pokerHandACards, pokerHandACard5.cardRank(), pokerHandACard4.cardRank(), pokerHandACard3.cardRank(), pokerHandACard2.cardRank(), pokerHandACard1.cardRank(), pokerHandACard5.cardSuit())
    pokerHandAFlush = pokerHandA
    pokerHandB = PokerHandFlush(pokerHandBCards, pokerHandBCard5.cardRank(), pokerHandBCard4.cardRank(), pokerHandBCard3.cardRank(), pokerHandBCard2.cardRank(), pokerHandBCard1.cardRank(), pokerHandBCard5.cardSuit())
    pokerHandBFlush = pokerHandB

    assert pokerHandBetterSameHandTypeFlush(pokerHandAFlush, pokerHandBFlush) == (False, "both flush, but jack has higher rank than ten")

    assert pokerHandBetterSameHandTypeFlush(pokerHandBFlush, pokerHandAFlush) == (True, "both flush, but jack has higher rank than ten")

    assert pokerHandBetterSameHandTypeFlush(pokerHandAFlush, pokerHandAFlush) == (False, "the hands are the same")

    # todo: add test that compare two hands where (i) both are flush, (ii) both share highest rank (and maybe second high, third high, fourth high), and (iii) differ on a lower rank

    assert type(findBestPokerHand(pokerHandACards)) == PokerHandFlush

    assert type(findBestPokerHand(pokerHandBCards)) == PokerHandFlush

def testPokerHandBetterSameHandTypeFullHouse():
    pokerHandACard1 = two_of_hearts
    pokerHandACard2 = two_of_clubs
    pokerHandACard3 = two_of_spades
    pokerHandACard4 = jack_of_clubs
    pokerHandACard5 = jack_of_hearts
    pokerHandACards = [pokerHandACard1, pokerHandACard2, pokerHandACard3, pokerHandACard4, pokerHandACard5]
    pokerHandBCard1 = two_of_spades
    pokerHandBCard2 = two_of_diamonds
    pokerHandBCard3 = two_of_hearts
    pokerHandBCard4 = ten_of_spades
    pokerHandBCard5 = ten_of_hearts
    pokerHandBCards = [pokerHandBCard1, pokerHandBCard2, pokerHandBCard3, pokerHandBCard4, pokerHandBCard5]
    pokerHandA = PokerHandFullHouse(pokerHandACards, "two", "jack")
    pokerHandAFullHouse = pokerHandA
    pokerHandB = PokerHandFullHouse(pokerHandBCards, "two", "ten")
    pokerHandBFullHouse = pokerHandB

    assert pokerHandBetterSameHandTypeFullHouse(pokerHandAFullHouse, pokerHandBFullHouse) == (True, "both full house, and rank with three of a kind is the same, but jack has higher rank than ten")

    assert pokerHandBetterSameHandTypeFullHouse(pokerHandBFullHouse, pokerHandAFullHouse) == (False, "both full house, and rank with three of a kind is the same, but jack has higher rank than ten")

    assert pokerHandBetterSameHandTypeFullHouse(pokerHandAFullHouse, pokerHandAFullHouse) == (False, "the hands are the same")

    # add tests for:
    # - three of a kind rank differs
    # - three of a kind rank same, and rank with pair differs

    assert type(findBestPokerHand(pokerHandACards)) == PokerHandFullHouse

    assert type(findBestPokerHand(pokerHandBCards)) == PokerHandFullHouse


def testPokerHandBetterSameHandTypeFourOfAKind():
    pokerHandACard1 = two_of_hearts
    pokerHandACard2 = two_of_clubs
    pokerHandACard3 = two_of_spades
    pokerHandACard4 = two_of_diamonds
    pokerHandACard5 = four_of_hearts
    pokerHandACards = [pokerHandACard1, pokerHandACard2, pokerHandACard3, pokerHandACard4, pokerHandACard5]
    pokerHandBCard1 = two_of_spades
    pokerHandBCard2 = two_of_diamonds
    pokerHandBCard3 = two_of_hearts
    pokerHandBCard4 = two_of_clubs
    pokerHandBCard5 = eight_of_hearts
    pokerHandBCards = [pokerHandBCard1, pokerHandBCard2, pokerHandBCard3, pokerHandBCard4, pokerHandBCard5]
    pokerHandA = PokerHandFourOfAKind(pokerHandACards, "two", pokerHandACard5.cardRank())
    pokerHandAFourOfAKind = pokerHandA
    pokerHandB = PokerHandFourOfAKind(pokerHandBCards, "two", pokerHandBCard5.cardRank())
    pokerHandBFourOfAKind = pokerHandB

    assert pokerHandBetterSameHandTypeFourOfAKind(pokerHandAFourOfAKind, pokerHandBFourOfAKind) == (False, "both four of a kind, and rank of four of a kind is the same, but eight has higher rank than four")

    assert pokerHandBetterSameHandTypeFourOfAKind(pokerHandBFourOfAKind, pokerHandAFourOfAKind) == (True, "both four of a kind, and rank of four of a kind is the same, but eight has higher rank than four")

    assert pokerHandBetterSameHandTypeFourOfAKind(pokerHandAFourOfAKind, pokerHandAFourOfAKind) == (False, "the hands are the same")

    # add tests for:
    # - three of a kind rank differs
    # - three of a kind rank same, and high card same, but low card differs

    assert type(findBestPokerHand(pokerHandACards)) == PokerHandFourOfAKind

    assert type(findBestPokerHand(pokerHandBCards)) == PokerHandFourOfAKind

def testPokerHandBetterSameHandTypeStraightFlush():
    pokerHandACard1 = two_of_hearts
    pokerHandACard2 = three_of_hearts
    pokerHandACard3 = four_of_hearts
    pokerHandACard4 = five_of_hearts
    pokerHandACard5 = six_of_hearts
    pokerHandACards = [pokerHandACard1, pokerHandACard2, pokerHandACard3, pokerHandACard4, pokerHandACard5]
    pokerHandBCard1 = three_of_hearts
    pokerHandBCard2 = four_of_hearts
    pokerHandBCard3 = five_of_hearts
    pokerHandBCard4 = six_of_hearts
    pokerHandBCard5 = seven_of_hearts
    pokerHandBCards = [pokerHandBCard1, pokerHandBCard2, pokerHandBCard3, pokerHandBCard4, pokerHandBCard5]
    pokerHandA = PokerHandStraightFlush(pokerHandACards, "six", "two", "heart")
    pokerHandAStraightFlush = pokerHandA
    pokerHandB = PokerHandStraightFlush(pokerHandBCards, "eight", "four", "heart")
    pokerHandBStraightFlush = pokerHandB

    assert pokerHandBetterSameHandTypeStraightFlush(pokerHandAStraightFlush, pokerHandBStraightFlush) == (False, "both straight flush, but eight has higher rank than six")

    assert pokerHandBetterSameHandTypeStraightFlush(pokerHandBStraightFlush, pokerHandAStraightFlush) == (True, "both straight flush, but eight has higher rank than six")

    assert pokerHandBetterSameHandTypeStraightFlush(pokerHandAStraightFlush, pokerHandAStraightFlush) == (False, "the hands are the same")

    assert type(findBestPokerHand(pokerHandACards)) == PokerHandStraightFlush

    assert type(findBestPokerHand(pokerHandBCards)) == PokerHandStraightFlush

def testPokerHandBetter():
    pokerHandACard1 = two_of_hearts
    pokerHandACard2 = three_of_hearts
    pokerHandACard3 = four_of_hearts
    pokerHandACard4 = five_of_hearts
    pokerHandACard5 = six_of_hearts
    pokerHandACards = [pokerHandACard1, pokerHandACard2, pokerHandACard3, pokerHandACard4, pokerHandACard5]
    pokerHandBCard1 = three_of_hearts
    pokerHandBCard2 = four_of_hearts
    pokerHandBCard3 = five_of_hearts
    pokerHandBCard4 = six_of_hearts
    pokerHandBCard5 = seven_of_hearts
    pokerHandBCards = [pokerHandBCard1, pokerHandBCard2, pokerHandBCard3, pokerHandBCard4, pokerHandBCard5]
    pokerHandA = PokerHandStraightFlush(pokerHandACards, "six", "two", "heart")
    pokerHandAStraightFlush = pokerHandA
    pokerHandB = PokerHandStraightFlush(pokerHandBCards, "eight", "four", "heart")
    pokerHandBStraightFlush = pokerHandB

    assert pokerHandBetter(pokerHandAStraightFlush, pokerHandBStraightFlush) == (False, "both straight flush, but eight has higher rank than six")

    assert pokerHandBetter(pokerHandBStraightFlush, pokerHandAStraightFlush) == (True, "both straight flush, but eight has higher rank than six")

    assert pokerHandBetter(pokerHandAStraightFlush, pokerHandAStraightFlush) == (False, "the hands are the same")
    

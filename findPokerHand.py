from pokerHand import *

# needs unit tests -- copied directly from server.py
def findBestPokerHand(playerFiveCards): # renamed assessHand -> findPokerHand
    cardRankCardsMap, cardRankOccurrenceCountMap, cardRankOccurrenceCountRankMap, cardsAllSameSuit, flushSuit = cardCategories(playerFiveCards)
    if not cardsAllSameSuit: # if cards are all same suit, then cannot have multiple occurences of same rank
        handWithMultipleOccurrencesOfARankSpecification = bestHandTypeWithMultipleOccurrencesOfARank(cardRankCardsMap, cardRankOccurrenceCountMap, cardRankOccurrenceCountRankMap)
        if 'handType' in handWithMultipleOccurrencesOfARankSpecification:
            if handWithMultipleOccurrencesOfARankSpecification['handType'] == 'fourOfAKind':
                rankWithFourOfAKind = handWithMultipleOccurrencesOfARankSpecification['rankWithFourOfAKind']
                rankWithOtherCard = handWithMultipleOccurrencesOfARankSpecification['otherCardRank']
                return PokerHandFourOfAKind(playerFiveCards, rankWithFourOfAKind, rankWithOtherCard)
            elif handWithMultipleOccurrencesOfARankSpecification['handType'] == 'fullHouse':
                rankWithThreeOfAKind = handWithMultipleOccurrencesOfARankSpecification['rankWithThreeOfAKind']
                rankWithPair = handWithMultipleOccurrencesOfARankSpecification['rankWithPair']
                return PokerHandFullHouse(playerFiveCards, rankWithThreeOfAKind, rankWithPair)
            elif handWithMultipleOccurrencesOfARankSpecification['handType'] == 'threeOfAKind':
                rankWithThreeOfAKind = handWithMultipleOccurrencesOfARankSpecification['rankWithThreeOfAKind']
                firstKickerRank = handWithMultipleOccurrencesOfARankSpecification['threeOfAKindFirstKickerRank']
                secondKickerRank = handWithMultipleOccurrencesOfARankSpecification['threeOfAKindSecondKickerRank']
                return PokerHandThreeOfAKind(playerFiveCards, rankWithThreeOfAKind, firstKickerRank, secondKickerRank)
            elif handWithMultipleOccurrencesOfARankSpecification['handType'] == 'twoPair':
                twoPairHighRank = handWithMultipleOccurrencesOfARankSpecification['twoPairHighRank']
                twoPairLowRank = handWithMultipleOccurrencesOfARankSpecification['twoPairLowRank']
                twoPairKickerRank = handWithMultipleOccurrencesOfARankSpecification['twoPairKicker']
                return PokerHandTwoPair(playerFiveCards, twoPairHighRank, twoPairLowRank, twoPairKickerRank)
            elif handWithMultipleOccurrencesOfARankSpecification['handType'] == 'onePair':
                rankWithOnePair = handWithMultipleOccurrencesOfARankSpecification['rankWithOnePair']
                onePairFirstKickerRank = handWithMultipleOccurrencesOfARankSpecification['onePairFirstKickerRank']
                onePairSecondKickerRank = handWithMultipleOccurrencesOfARankSpecification['onePairSecondKickerRank']
                onePairThirdKickerRank = handWithMultipleOccurrencesOfARankSpecification['onePairThirdKickerRank']
                return PokerHandOnePair(playerFiveCards, rankWithOnePair, onePairFirstKickerRank, onePairSecondKickerRank, onePairThirdKickerRank)
    cardsAreEachADifferentRankAndTheRanksAreSequentialVar, highestCardRank, secondHighestCardRank, thirdHighestCardRank, fourthHighestCardRank, lowestCardRank = cardsAreEachADifferentRankAndTheRanksAreSequential(cardRankCardsMap, cardRankOccurrenceCountMap, cardRankOccurrenceCountRankMap) # why do I have to make the variable name cardsAreEachADifferentRankAndTheRanksAreSequentialVar rather than cardsAreEachADifferentRankAndTheRanksAreSequential ? I get a UnboundLocalError: local variable 'cardsAreEachADifferentRankAndTheRanksAreSequential' referenced before assignment
    if cardsAllSameSuit and cardsAreEachADifferentRankAndTheRanksAreSequentialVar:
        return PokerHandStraightFlush(playerFiveCards, highestCardRank, lowestCardRank, flushSuit)
    if cardsAllSameSuit:
        return PokerHandFlush(playerFiveCards, highestCardRank, secondHighestCardRank, thirdHighestCardRank, fourthHighestCardRank, lowestCardRank, flushSuit)
    if cardsAreEachADifferentRankAndTheRanksAreSequentialVar:
        return PokerHandStraight(playerFiveCards, highestCardRank, lowestCardRank)
    return PokerHandHighCard(playerFiveCards, highestCardRank, secondHighestCardRank, thirdHighestCardRank, fourthHighestCardRank, lowestCardRank)

# needs unit tests -- copied directly from server.py
def cardsAreEachADifferentRankAndTheRanksAreSequential(cardRankCardsMap, cardRankOccurrenceCountMap, cardRankOccurrenceCountRankMap):
    ranksWithOneCard = cardRankOccurrenceCountRankMap[1]
    numberOfRanksWithOneCard = len(ranksWithOneCard)
    cardsAreEachADifferentRank = (numberOfRanksWithOneCard == 5)
    if not cardsAreEachADifferentRank:
        return False, None, None, None, None, None
    ranksAreSequential = False
    ranksWithOneCard.sort(key=rankIndexInRanksLowToHigh)
    lowestRankInRanksWithOneCard = ranksWithOneCard[0]
    lowestCardRank = lowestRankInRanksWithOneCard
    indexOfLowestRankInRanksWithOneCard = rankIndexInRanksLowToHigh(lowestRankInRanksWithOneCard)
    secondRankInRanksWithOneCard = ranksWithOneCard[1]
    indexOfSecondRankInRanksWithOneCard = rankIndexInRanksLowToHigh(secondRankInRanksWithOneCard)
    thirdRankInRanksWithOneCard = ranksWithOneCard[2]
    indexOfThirdRankInRanksWithOneCard = rankIndexInRanksLowToHigh(thirdRankInRanksWithOneCard)
    fourthRankInRanksWithOneCard = ranksWithOneCard[3]
    indexOfFourthRankInRanksWithOneCard = rankIndexInRanksLowToHigh(fourthRankInRanksWithOneCard)
    fifthRankInRanksWithOneCard = ranksWithOneCard[4]
    indexOfFifthRankInRanksWithOneCard = rankIndexInRanksLowToHigh(fifthRankInRanksWithOneCard)
    highestCardRank = fifthRankInRanksWithOneCard
    secondHighestCardRank = fourthRankInRanksWithOneCard # 20220521 -- if highest is fifth, shouldn't second highest be fourth?
    thirdHighestCardRank = thirdRankInRanksWithOneCard
    fourthHighestCardRank = secondRankInRanksWithOneCard
    if ((indexOfSecondRankInRanksWithOneCard == 1 + indexOfLowestRankInRanksWithOneCard and # first-rank + 1 = second-rank
        indexOfThirdRankInRanksWithOneCard  == 1 + indexOfSecondRankInRanksWithOneCard and # second-rank + 1 == third-rank
        indexOfFourthRankInRanksWithOneCard == 1 + indexOfThirdRankInRanksWithOneCard # third-rank + 1 == fourth-rank
        ) and
        ((indexOfFifthRankInRanksWithOneCard  == 1 + indexOfFourthRankInRanksWithOneCard) or # normal case: fourth-rank + 1 == fifth-rank
         (indexOfFifthRankInRanksWithOneCard == 13 and # ace-is-low case: fifth-rank is ace
          indexOfLowestRankInRanksWithOneCard == 0))): #                  lowest-rank is two 
        ranksAreSequential = True
        if (indexOfFifthRankInRanksWithOneCard == 13 and # ace-is-low case
            indexOfLowestRankInRanksWithOneCard == 0):
            highestCardRank = fourthRankInRanksWithOneCard # make high card 5
            lowestCardRank = fifthRankInRanksWithOneCard   # make low card ace
    cardsAreEachADifferentRankAndTheRanksAreSequential = (cardsAreEachADifferentRank and ranksAreSequential)
    return cardsAreEachADifferentRankAndTheRanksAreSequential, highestCardRank, secondHighestCardRank, thirdHighestCardRank, fourthHighestCardRank, lowestCardRank

# needs unit tests -- copied directly from server.py
def cardCategories(playerFiveCards):
    flushSuit = None # assume no flush suit
    cardsAllSameSuit = True # assume true and provide ways to disconfirm
    firstCard = playerFiveCards[0]
    firstCardSuit = firstCard.suit
    cardRankCardsMap = {}
    for card in playerFiveCards:
        cardRank = card.rank
        if cardRank in cardRankCardsMap:
            cardRankCardsMap[cardRank].append(card)
        else:
            cardRankCardsMap[cardRank] = [card]
        if card.suit != firstCardSuit:
            cardsAllSameSuit = False
#        print(card.rank)
#        print(card.suit)
#        print(cardRankCardsMap)
    if cardsAllSameSuit:
        flushSuit = firstCardSuit
    cardRankOccurrenceCountMap = {}
    cardRankOccurrenceCountRankMap = {}
    for rank, cards in cardRankCardsMap.items():
        rankOccurrenceCount = len(cards)
        cardRankOccurrenceCountMap[rank] = rankOccurrenceCount
        if rankOccurrenceCount in cardRankOccurrenceCountRankMap:
            cardRankOccurrenceCountRankMap[rankOccurrenceCount].append(rank)
        else:
            cardRankOccurrenceCountRankMap[rankOccurrenceCount] = [rank]
    return cardRankCardsMap, cardRankOccurrenceCountMap, cardRankOccurrenceCountRankMap, cardsAllSameSuit, flushSuit

# needs unit tests -- copied directly from server.py
def bestHandTypeWithMultipleOccurrencesOfARank(cardRankCardsMap, cardRankOccurrenceCountMap, cardRankOccurrenceCountRankMap):
    """return map"""
    handWithMultipleOccurrencesOfARankSpecification = {}
    if 4 in cardRankOccurrenceCountRankMap:
        handWithMultipleOccurrencesOfARankSpecification['handType'] = 'fourOfAKind'
        ranksWithFourOfAKind = cardRankOccurrenceCountRankMap[4]
        rankWithFourOfAKind = ranksWithFourOfAKind[0]
        handWithMultipleOccurrencesOfARankSpecification['rankWithFourOfAKind'] = rankWithFourOfAKind
        otherCardRanks = cardRankOccurrenceCountRankMap[1]
        otherCardRank = otherCardRanks[0]
        # otherCards = cardRankCardsMap[otherCardRank]
        # otherCard = otherCards[0]
        handWithMultipleOccurrencesOfARankSpecification['otherCardRank'] = otherCardRank
    elif 3 in cardRankOccurrenceCountRankMap:
        ranksWithThreeOfAKind = cardRankOccurrenceCountRankMap[3]
        rankWithThreeOfAKind = ranksWithThreeOfAKind[0]
        handWithMultipleOccurrencesOfARankSpecification['rankWithThreeOfAKind'] = rankWithThreeOfAKind
        if 2 in cardRankOccurrenceCountRankMap:
            handWithMultipleOccurrencesOfARankSpecification['handType'] = 'fullHouse'
            ranksWithPair = cardRankOccurrenceCountRankMap[2]
            rankWithPair = ranksWithPair[0]
            handWithMultipleOccurrencesOfARankSpecification['rankWithPair'] = rankWithPair
        else:
            handWithMultipleOccurrencesOfARankSpecification['handType'] = 'threeOfAKind'
            ranksWithSingleOccurrenceOfRank = cardRankOccurrenceCountRankMap[1]
            ranksWithSingleOccurrenceOfRank.sort(key=rankIndexInRanksLowToHigh, reverse=True)
            threeOfAKindFirstKickerRank = ranksWithSingleOccurrenceOfRank[0]
            threeOfAKindSecondKickerRank = ranksWithSingleOccurrenceOfRank[1]
            handWithMultipleOccurrencesOfARankSpecification['threeOfAKindFirstKickerRank'] = threeOfAKindFirstKickerRank
            handWithMultipleOccurrencesOfARankSpecification['threeOfAKindSecondKickerRank'] = threeOfAKindSecondKickerRank
    elif 2 in cardRankOccurrenceCountRankMap:
        ranksWithPair = cardRankOccurrenceCountRankMap[2]
        twoRanksWithPair = (len(ranksWithPair) == 2)
        if twoRanksWithPair:
            handWithMultipleOccurrencesOfARankSpecification['handType'] = 'twoPair'
            oneRankWithPair = ranksWithPair[0]
            otherRankWithPair = ranksWithPair[1]
            ranksOfKicker = cardRankOccurrenceCountRankMap[1]
            rankOfKicker = ranksOfKicker[0]
            if rankHigherThanRank(oneRankWithPair, otherRankWithPair):
                handWithMultipleOccurrencesOfARankSpecification['twoPairHighRank'] = oneRankWithPair
                handWithMultipleOccurrencesOfARankSpecification['twoPairLowRank'] = otherRankWithPair
            else:
                handWithMultipleOccurrencesOfARankSpecification['twoPairHighRank'] = otherRankWithPair
                handWithMultipleOccurrencesOfARankSpecification['twoPairLowRank'] = oneRankWithPair
            handWithMultipleOccurrencesOfARankSpecification['twoPairKicker'] = rankOfKicker    
        else:
            handWithMultipleOccurrencesOfARankSpecification['handType'] = 'onePair'
            rankWithPair = ranksWithPair[0]
            handWithMultipleOccurrencesOfARankSpecification['rankWithOnePair'] = rankWithPair
            ranksWithSingleOccurrenceOfRank = cardRankOccurrenceCountRankMap[1]
            ranksWithSingleOccurrenceOfRank.sort(key=rankIndexInRanksLowToHigh, reverse=True)
            onePairFirstKickerRank = ranksWithSingleOccurrenceOfRank[0]
            onePairSecondKickerRank = ranksWithSingleOccurrenceOfRank[1]
            onePairThirdKickerRank = ranksWithSingleOccurrenceOfRank[2]
            handWithMultipleOccurrencesOfARankSpecification['onePairFirstKickerRank'] = onePairFirstKickerRank
            handWithMultipleOccurrencesOfARankSpecification['onePairSecondKickerRank'] = onePairSecondKickerRank
            handWithMultipleOccurrencesOfARankSpecification['onePairThirdKickerRank'] = onePairThirdKickerRank
#    print(handWithMultipleOccurrencesOfARankSpecification)
    return handWithMultipleOccurrencesOfARankSpecification
#    for cardRank, occurrenceCount in cardRankOccurrenceCountsMap.items():
#        if occurrenceCount == 4:

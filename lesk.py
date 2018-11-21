"""
Author - Romi Padam
"""

import sys
from nltk.corpus import wordnet

def lesk(sentence, word):
    context = sentence.split()
    wordsenses = wordnet.synsets(word)
    maxOverlap = -sys.maxsize -1
    if wordsenses[0].name().__contains__('.' + 'n' + '.'):
        bestSense = wordsenses[0].definition()

    for wordsense in wordsenses:
        if wordsense.name().__contains__('.' + 'n' + '.'):
            #signature <- set of words in the gloss and examples of sense
            signature = str(wordsense.definition())
            signature += ' '
            for example in wordsense.examples():
                signature += str(example)
            signature = signature.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})

            #Number of words common between signature and context, ignoring function words
            overlap = computeOverlap(signature.split(), context, word)

            if overlap > maxOverlap:
                maxOverlap = overlap
                bestSense = str(wordsense.definition())
                sense = wordsense.name()

            print('----------------------------------------------------------------')
            print('Sense: ' + str(wordsense.name()) + '\nDefinition: ' + str(wordsense.definition()) + '\nExample: ' + str(wordsense.examples()) + '\nOverlap:' + str(overlap))

    return sense, bestSense, maxOverlap

def computeOverlap(signature, context, word):
    overlap = list((set(context) & set(signature)))
    if word in overlap:
        overlap.remove(word)
    return(len(overlap))

if __name__ == '__main__':
    #sentence = 'The bank can guarantee deposits will eventually cover future tuition costs because it invests in adjustable-rate mortgage securities.'
    #word = 'bank'
    sentence = sys.argv[1]
    word = sys.argv[2]

    sense, bestSense, maxOverlap = lesk(sentence, word)

    print('\n****************************************************************')
    print("Final Chosen Sense - ")
    print('Sense: ' + str(sense) + '\nBest Sense: ' + str(bestSense) + '\nMax Overlap:' + str(maxOverlap))
    print('****************************************************************')

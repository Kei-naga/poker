from pcard import *


class Hand(Deck):
    """definition of Deck"""
    def __init__(self):
        super().__init__()
        self.clear()

    def score(self):
        s = 0
        ace = 0
        for card in self:
            if card.number > 10:
                s += 10
            elif card.number == 1:
                ace += 1
                s += 11
            else:
                s += card.number
        for i in range(ace):
            if s > 21:
                s -= 10
            else:
                break
        return s

    def sort(self):
        super().sort(key=lambda x: (x.number, x.suit))
        '''
        super().sort(key=lambda x:
                     (x.number, PlayingCard.SUIT_LIST.index(x.suit)))
        '''

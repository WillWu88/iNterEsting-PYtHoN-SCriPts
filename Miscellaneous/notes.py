# some example codes and notes for review


def ask_ok(prompt, retries=4, reminder='Please try again!'):
while True:
        # pattern matching in an array if....in
    ok = input(prompt)
    if ok in ('y', 'ye', 'yes'):
        return True
    if ok in ('n', 'no', 'nop', 'nope'):
        return False
    retries = retries - 1
    if retries < 0:
        raise ValueError('invalid user response')
    print(reminder)

#######################################################


# French Desk Example

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()  # constructor

print(deck[0])

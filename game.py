import os
from random import choice

from util import get_match_list, get_accept_list


class Wordle:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    GRAY = '\033[90m'
    ENDC = '\033[0m'
    clear = lambda self: os.system('cls' if os.name == 'nt' else 'clear')
    KEYBOARD = 'qwertyuiop\nasdfghjkl\nzxcvbnm'

    def __init__(self, word_index=None, max_guess=6):
        self.match_list = get_match_list()
        self.accept_list = self.match_list + get_accept_list()
        self.word = choice(self.match_list) if word_index is None else self.match_list[word_index]
        self.max_guess = max_guess
        self.history = [self.ENDC + chr(ord('a')+i) for i in range(26)]

    def reload(self, word_index=None):
        self.word = choice(self.match_list) if word_index is None else self.match_list[word_index]
        self.history = [self.ENDC + chr(ord('a') + i) for i in range(26)]

    def format_guess_word(self, w, guess_count):
        """
        makes
        |a|b|c|d|e|
        +-+-+-+-+-+

        :param w: string of 5 letter word
        :return:
        """
        # print(w)
        res = '+-+-+-+-+-+\n|' if guess_count == 0 else '|'
        for i, c in enumerate(w):
            if c == self.word[i]:
                res += self.GREEN + c
                self.history[ord(c) - ord('a')] = self.GRAY + c
            elif c in self.word:
                res += self.YELLOW + c
                self.history[ord(c) - ord('a')] = self.GRAY + c
            else:
                res += self.GRAY + c
                self.history[ord(c) - ord('a')] = self.GRAY + c
            res += self.ENDC + '|'
            # print(res)

        return res + '\n+-+-+-+-+-+'

    def print_keyboard(self):
        res = ''
        for c in self.KEYBOARD:
            if c.isalpha():
                res += self.history[ord(c) - ord('a')]
            else:
                res += '\n'

        print(res + self.ENDC)

    def run(self):
        session = 'W-O-R-D-L-E'
        for i in range(self.max_guess):
            self.clear()
            # print(self.word)
            print(session)
            self.print_keyboard()

            w = input('>')
            while w not in self.accept_list:
                print('Your entry is not an accepted word. Try again.')
                w = input('>')

            session += '\n' + self.format_guess_word(w, i)
            if w == self.word:
                self.clear()
                print(session)
                print('You guessed right! Good job!')
                return

        self.clear()
        print(session)
        print('You used up all of your guess. The word is')
        print(self.word)

#
# wordle = Wordle(6)
# wordle.run()

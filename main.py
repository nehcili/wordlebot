import random

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_MAP = {ALPHABET[i]: i for i in range(26)}


class MatchCharacteristics:
    def __init__(self, exact_match, partial_match, does_not_contain):
        """

        :param exact_match: dict: position [0, 5): char
        :param partial_match: set
        :param does_not_contain: set
        """
        self.exact_match = exact_match
        self.partial_match = partial_match
        self.does_not_contain = does_not_contain

    @classmethod
    def from_words(cls, guess, truth):
        exact_match = {}
        partial_match = {}
        does_not_contain = set()

        for i, c in enumerate(guess):
            if c == truth[i]:
                exact_match[i] = c
            elif c in truth:
                partial_match[i] = c
            else:
                does_not_contain.add(c)

        return cls(exact_match, partial_match, does_not_contain)

    def match(self, w):
        for i, c in self.exact_match.items():
            if w[i] != c:
                return False
        for i, c in self.partial_match.items():
            if c not in w or w[i] == c:
                return False
        for c in self.does_not_contain:
            if c in w:
                return False
        return True

    def get_matching_subspace_size(self, sample_space):
        res = 0
        for w in sample_space:
            res += self.match(w)

        return res

    def get_matching_subspace(self, sample_space):
        res = []
        for w in sample_space:
            if self.match(w):
                res.append(w)

        return res


class WordleBot:
    # roate is the best
    def __init__(self, match_file_name, accept_file_name, sample_limit=100, accept_limit=1000):
        self.match_file_name = match_file_name
        self.accept_file_name = accept_file_name
        self.sample_space = self.get_word_list(match_file_name)
        self.accept_list = self.get_word_list(accept_file_name)
        self.sample_limit = sample_limit
        self.accept_limit = accept_limit

        self.green = set()
        self.yellow = set()

    @staticmethod
    def get_word_list(filename):
        with open(filename, 'r') as f:
            match_list = f.read()
        return [x for x in match_list.lower().split('\n') if len(x) == 5]

    def reload(self):
        self.sample_space = self.get_word_list(self.match_file_name)
        self.accept_list = self.get_word_list(self.accept_file_name)

        self.green = set()
        self.yellow = set()

    def condition(self, exact_match, partial_match, does_not_match):
        mchar = MatchCharacteristics(exact_match, partial_match, does_not_match)
        self.sample_space = mchar.get_matching_subspace(self.sample_space)

    @staticmethod
    def get_expected_matching_subspace_size(guess, sample_space):
        total_size = 0.
        for truth in sample_space:
            mchar = MatchCharacteristics.from_words(guess, truth)
            total_size += mchar.get_matching_subspace_size(sample_space)

        return total_size / len(sample_space)

    def get_best_guess(self):
        min_expected_matching_subspace_size = float('inf')
        res = None

        sample_space = self.sample_space if self.sample_limit is None \
            else random.sample(self.sample_space, min(self.sample_limit, len(self.sample_space)))
        accept_list = self.accept_list if self.accept_limit is None \
            else random.sample(self.accept_list, min(self.accept_limit, len(self.accept_list)))

        n = len(sample_space) + len(accept_list)
        for i, guess in enumerate(sample_space + accept_list):
            expected_matching_subspace_size = self.get_expected_matching_subspace_size(guess, sample_space)
            if expected_matching_subspace_size < min_expected_matching_subspace_size:
                min_expected_matching_subspace_size = expected_matching_subspace_size
                res = guess

        return res

    def run(self):
        print('best guess: raise')
        while True:
            green = input('green: ')
            self.green.update(set(green))
            green = {i: c for i, c in enumerate(green) if c != ' '}
            if not green:
                green = {}

            yellow = input('yellow: ')
            self.yellow.update(set(yellow))
            yellow = {i: c for i, c in enumerate(yellow) if c != ' '}
            if not yellow:
                yellow = {}

            gray = input('gray: ')
            gray = {x for x in gray if x not in self.green and x not in self.yellow}
            self.condition(green, yellow, gray)
            print('best guess:', self.get_best_guess())



def main():
    wb = WordleBot('steve_match.txt', 'steve_accept.txt', 100, 1000)
    wb.run()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# word_index:
# 1313
# 83
# 2000
# 1433
# 100
#
#
#
# Muffin+Smartie:
# 1313: 4
# 83: 7 FAIL
# 2000: 6
# 1433: 5
# 100: 3
#
# Computer
# 1313: 5
# 83: 3
# 2000: 4
# 1433: 4
# 100: 3

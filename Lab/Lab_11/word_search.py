
from collections import defaultdict


class WordSearch:
    '''
    Records the contents of a file that contains n lines with m letters for some n and m,
    possibly with spaces between the letters and possibly with blank lines.
    Such a contents is intended to be the grid of a word search game: words are given that
    have to be found in the grid, being read horizontally, vertically or diagonally, in
    either direction.
    '''
    def __init__(self, filename):
        self.grid = self._get_grid(filename)

    def _get_grid(self,filename):
        grid = [[None for _ in range(14)] for _ in range(14)]
        with open(filename) as file:
            i = -1
            for line in file:
                line = line.rstrip()
                if not line:
                    continue
                i += 1
                j = -1
                for x in line:
                    if not x.isalpha():
                        continue
                    j += 1
                    grid[i][j] = x
        return grid


    def __str__(self):
        return '\n'.join(' '.join(_ for _ in line) for line in self.grid)

    def locate_word_in_grid(self, word):
        '''
        Returns None if word cannot be read in the grid.
        Otherwise, returns the x and y coordinates of an occurrence
        of the first letter of word, and the direction to follow
        (N, NE, E, SE, S, SW, W or NW) to read the whole word from
        that point onwards.
        '''
        pass
        # Replace pass above with your code

    def locate_words_in_grid(self, *words):
        pass
        # Replace pass above with your code

    def display_word_in_grid(self, word):
        '''
        In case word can indeed be read from the grid,
        prints out the grid with all characters being displayed in lowercase,
        except for those that make up word, displayed in uppercase.
        '''
        pass
        # Replace pass above with your code

        # Possibly define helper functions

if __name__ == '__main__':
    import pprint
    ws = WordSearch('word_search_1.txt')
    print('Testing with grid for metals')
    print()
    print(ws)
    # print()
    # metal = 'PLATINUM'
    # print(f'{metal}: {ws.locate_word_in_grid(metal)}')
    # metal = 'SODIUM'
    # print(f'{metal}: {ws.locate_word_in_grid(metal)}')
    # metals = ('PLATINUM', 'COPPER', 'MERCURY', 'TUNGSTEN', 'MAGNESIUM', 'ZINC', 'MANGANESE',
    #           'TITANIUM', 'TIN', 'IRON', 'LITHIUM', 'CADMIUM', 'GOLD', 'COBALT', 'SILVER',
    #           'NICKEL', 'LEAD', 'IRIDIUM', 'URANIUM', 'SODIUM')
    # located_metals = ws.locate_words_in_grid(*metals)
    # pprint.pprint(located_metals)
    # print()
    # for metal in metals:
    #     print(metal, end = ':\n')
    #     ws.display_word_in_grid(metal)
    #     print()
    # print()
    #
    # ws = WordSearch('word_search_2.txt')
    # print('Testing with grid for fruits')
    # print()
    # print(ws)
    # print()
    # fruit = 'RASPBERRY'
    # print(f'{fruit}: {ws.locate_word_in_grid(fruit)}')
    # fruit = 'PEAR'
    # print(f'{fruit}: {ws.locate_word_in_grid(fruit)}')
    # fruits = ('RASPBERRY', 'LIME', 'BLACKBERRY', 'BLUEBERRY', 'WATERMELON', 'ORANGE',
    #           'BANANA', 'PAPAYA', 'LEMON', 'KIWI', 'GRAPE', 'APPLE', 'PEAR', 'MANGOE')
    # located_fruits = ws.locate_words_in_grid(*fruits)
    # pprint.pprint(located_fruits)
    # print()
    # for fruit in fruits:
    #     print(fruit, end = ':\n')
    #     ws.display_word_in_grid(fruit)
    #     print()

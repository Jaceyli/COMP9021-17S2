
from collections import defaultdict, deque
import sys


'''
Computes all transformations from a word word_1 to a word word_2, consisting of
sequences of words of minimal length, starting with word_1, ending in word_2,
and such that two consecutive words in the sequence differ by at most one letter.
All words have to occur in a dictionary with name dictionary.txt, stored in the
working directory.
'''

# dictionary 存了每个basket可以生成的word  {'_AINWRIGHT': {'WAINWRIGHT'}, 'W_INWRIGHT': {'WAINWRIGHT'}....
#但是在遍历的时候，要先遍历 word1的basket然后找，会特别慢
#所以改进为dict的key是word，value是由这个word变化一个字母生成的word

dictionary_file = 'd.txt'
# dictionary_file = 'dictionary.txt'

def get_words_and_word_relationships():
    words = set()
    closest_words = defaultdict(set)
    try:
        with open(dictionary_file) as file:
            for line in file:
                words.add(line.rstrip())
            for word in words:
                for i in range(len(word)):
                    basket = word[:i]+'_'+word[i + 1:]
                    closest_words[basket].add(word)

    except FileExistsError:
        print('There is no such file...')
        sys.exit()
    return words,closest_words


def word_ladder(word_1, word_2):
    word_1 = word_1.upper()
    word_2 = word_2.upper()
    lexicon, closest_words = get_words_and_word_relationships()
    print(closest_words)
    if len(word_1) != len(word_2) or word_1 not in lexicon or word_2 not in lexicon:
        return []
    if word_1 == word_2:
        return [[word_1]]

    solutions = []
    queue = deque([[word_1]])
    while queue:
        current_sequence = queue.pop()
        current_word = current_sequence[-1]
        for i in range(len(current_word)):
            for j in closest_words[current_word[:i] + '_' + current_word[i+1:]]:
                if j in current_sequence:
                    continue
                if j == word_2 and (not solutions or len(solutions[-1]) > len(current_sequence)):
                    # current_sequence.append(word_2)
                    solutions.append(current_sequence + [word_2])
                else:
                    queue.appendleft(current_sequence+[j])
    return solutions


for ladder in word_ladder('cold', 'warm'): print(ladder)






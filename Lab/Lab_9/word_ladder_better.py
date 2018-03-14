
from collections import defaultdict, deque
import sys


'''
Computes all transformations from a word word_1 to a word word_2, consisting of
sequences of words of minimal length, starting with word_1, ending in word_2,
and such that two consecutive words in the sequence differ by at most one letter.
All words have to occur in a dictionary with name dictionary.txt, stored in the
working directory.
'''


dictionary_file = 'dictionary.txt'

def get_words_and_word_relationships():
    words = set()
    basket = defaultdict(list)
    closest_words = defaultdict(set)

    try:
        with open(dictionary_file) as file:
            for line in file:
                words.add(line.rstrip())

            for word in words:
                for i in range(len(word)):
                    slot = word[:i]+'_'+word[i + 1:]
                    basket[slot].append(word)
            # l = []
            # for key in basket:
            #     if len(basket[key]) == 1:
            #         l.append(key)
            # for i in l:
            #     basket.pop(i)
            # print(len(basket))

            # 这个算法效率太低了....
            # for word in words:
            #     for i in range(len(words)):
            #         for e in basket[word[:i]+'_'+word[i + 1:]]:
            #             if e != word and word not in closest_words.keys():
            #                 closest_words[word].add(e)
            for slot in basket:
                for i in range(len(basket[slot])):
                    for j in range(i+1, len(basket[slot])):
                        # print(basket[slot][i], basket[slot][j])
                        closest_words[basket[slot][i]].add(basket[slot][j])
                        closest_words[basket[slot][j]].add(basket[slot][i])
            # print(closest_words)
    except FileExistsError:
        print('There is no such file...')
        sys.exit()
    return words, closest_words


def word_ladder(word_1, word_2):
    word_1 = word_1.upper()
    word_2 = word_2.upper()
    lexicon, closest_words = get_words_and_word_relationships()
    if len(word_1) != len(word_2) or word_1 not in lexicon or word_2 not in lexicon:
        return []
    if word_1 == word_2:
        return [[word_1]]
    solutions = []
    queue = deque([[word_1]])
    while queue:
        current_sequence = queue.pop()
        current_word = current_sequence[-1]
        for e in closest_words[current_word]:
            # if e in current_sequence:
            #     continue
            if e == word_2:
                if not solutions or len(solutions[-1]) > len(current_sequence):
                    solutions.append(current_sequence + [e])
            if not solutions and e not in current_sequence:
                queue.appendleft(current_sequence+[e])
    return solutions


for ladder in word_ladder('cold', 'warm'): print(ladder)






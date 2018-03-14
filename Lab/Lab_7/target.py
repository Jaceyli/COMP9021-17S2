from random import choice, sample
from collections import defaultdict


class Target:
    def __init__(self, dictionary='dictionary.txt', target=None, minimal_length=4):
        self.dictionary = dictionary
        self.minimal_length = minimal_length
        with open(self.dictionary) as file:
            # 这句厉害了 d=====(￣▽￣*)b
            self.words = dict(filter(lambda x: len(x[0]) == len(x[1]), ((word, set(word))
                                                                        for word in (line.rstrip() for line in file)
                                                                        )
                                     )
                              )
        # print(self.words)
        self.letter = [self.words[word] for word in self.words if len(word) == 9]
        # print(self.letter)
        if target:
            self.target_letter = set(target)
            if len(self.target_letter) == 9 and \
                            self.target_letter in self.letter:
                self.target = target
            else:
                target = None
                print(f'{target} is not a valid target, a random one will be generated instead.')
        if not target:
            self.target_letter = choice(self.letter)
            # sample(X,n) 从有序的序列中取n个随机排序
            self.target = ''.join(sample(self.target_letter, 9))
        self.solutions = self._solve_target()

    def __repr__(self):
        return f'Target(dictionary = {self.dictionary}, minimal_length = {self.minimal_length})'

    def __str__(self):
        target_string = '\n       ___________\n'
        for i in range(1, 4):
            target_string += '\n      | '
            target_string += ' | '.join(str(e) for e in self.target[3 * i - 3: 3 * i])
            target_string += ' |\n       ___________\n'
        return target_string

    def _solve_target(self):
        solution = defaultdict(list)
        # print(self.target)
        for word in self.words:
            if self.minimal_length <= len(word) and \
                            self.target[4] in self.words[word] and \
                            self.words[word] <= self.target_letter:
                # len(word) == len([e for e in word if e in self.target]):
                # 直接用> < 比较  一个包含于另一个，不用这么麻烦
                solution[len(word)].append(word)
        return solution

    def number_of_solutions(self):
        max_number = max(self.solutions.keys())
        min_number = min(self.solutions.keys())
        print(f'In decreasing order of length between {max_number} and {min_number}:')
        solution = sorted(self.solutions.items(), key=lambda x: x[0], reverse=True)
        for e in solution:
            number_of_sol = len(e[1])
            if number_of_sol == 1:
                print(f'    1 solution of length {e[0]}')
            else:
                print(f'    {len(e[1])} solutions of length {e[0]}')

    def give_solutions(self, minimal_length=None):
        if minimal_length is None:
            minimal_length = self.minimal_length
        keys = sorted(self.solutions.keys(), reverse=True)
        for e in keys:
            if e < minimal_length:
                continue
            if e != 9:
                print()
            if len(self.solutions[e]) == 1:
                print(f'Solution of length {e}:')
                print('   ', self.solutions[e][0])
            else:
                print(f'Solutions of length {e}:')
                for i in self.solutions[e]:
                    print('   ', i)

    # 没看懂
    def change_target(self, to_be_replaced, to_replace):
        if to_be_replaced != to_replace and len(to_be_replaced) == len(to_replace):
            letters_to_be_replaced = set(to_be_replaced)
            if letters_to_be_replaced <= self.target_letter:
                new_target_letters = self.target_letter - letters_to_be_replaced | set(to_replace)
                if new_target_letters in self.letter:
                    old_target_letters = self.target_letter
                    old_letter_at_centre = self.target[4]
                    self.target_letter = new_target_letters
                    self.target = self.target.translate(str.maketrans(to_be_replaced, to_replace))
                    if self.target_letter != old_target_letters or \
                                    self.target[4] != old_letter_at_centre:
                        self.solutions = self._solve_target()
                    else:
                        print('The solutions are not changed.')
                    return
        print('The target was not changed.')

        # if len(to_be_replaced) == len(to_replace) and set(to_be_replaced) != set(to_replace):
        #     remain = [e for e in self.target_letter if e not in list(to_be_replaced)]
        #     self.target_letter = set(to_replace)
        #     for e in remain:
        #         self.target_letter.add(e)
        #     # self.target_letter.add(e for e in remain)
        #     if len(self.target_letter) == 9 and \
        #                     self.target_letter in self.letter:
        #         self.target = ''.join(e for e in self.target_letter)
        #         # print(self.target)
        #     else:
        #         print('The target was not changed.')
        #         return
        # else:
        #     print('The target was not changed.')
        #     return




# target = Target()
target = Target(target='IMRVOZATK', minimal_length=5)
##target.change_target('IVAKZRMO', 'DAFNEMRS')
print(target)
# target.number_of_solutions()
# target.give_solutions()

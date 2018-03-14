import os
import copy
from collections import defaultdict

defaultbegin = '\\documentclass[10pt]{article}\n' \
               '\\usepackage[left=0pt,right=0pt]{geometry}\n' \
               '\\usepackage{tikz}\n' \
               '\\usetikzlibrary{positioning}\n' \
               '\\usepackage{cancel}\n' \
               '\\pagestyle{empty}\n' \
               '\n' \
               '\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},' \
               '\n                               label=above right:{\\tiny #2},' \
               '\n                               label=below left:{\\tiny #3},' \
               '\n                               label=below right:{\\tiny #4}]{#5};}}\n' \
               '\n' \
               '\\begin{document}\n' \
               '\n' \
               '\\tikzset{every node/.style={minimum size=.5cm}}\n' \
               '\n' \
               '\\begin{center}\n' \
               '\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\hline\hline'
defaultend = '\\end{tabular}\n' \
             '\\end{center}\n' \
             '\n' \
             '\\end{document}'


class SudokuError(Exception):
    def __init__(self, message):
        self.message = message


class Sudoku:
    def __init__(self, filename):
        name = filename.split('.')
        self.filename = name[0]
        self._grid = self._get_grid()
        self._row_value = [[] for _ in range(9)]
        self._column_value = [[] for _ in range(9)]
        self._box_value = [[] for _ in range(9)]
        self._row_available = [list(range(1, 10)) for _ in range(9)]
        self._column_available = [list(range(1, 10)) for _ in range(9)]
        self._box_available = [list(range(1, 10)) for _ in range(9)]
        self._original_markup = dict()
        self._markup = dict()
        self._preemptive_set_box = dict()
        self._preemptive_set_row = dict()
        self._preemptive_set_column = dict()

    # read txt, init grid
    def _get_grid(self):
        grid = [[0 for _ in range(9)] for _ in range(9)]
        with open(self.filename + '.txt') as file:
            i = -1
            for line in file:
                line = line.rstrip()
                if not line:
                    continue
                i += 1
                j = -1
                for x in line:
                    if not x.isdigit():
                        continue
                    j += 1
                    try:
                        x = int(x)
                    except ValueError:
                        raise SudokuError('Incorrect input')
                    grid[i][j] = x
                if j < 8:
                    raise SudokuError('Incorrect input')
            if i < 8:
                raise SudokuError('Incorrect input')
        return grid

    def _init_params(self):
        # duplicate in row
        for i in range(9):
            for j in range(9):
                if self._grid[i][j]:
                    self._row_value[i].append(self._grid[i][j])
                    if len(set(self._row_value[i])) != len(self._row_value[i]):
                        return 0
        # duplicate in column
        for j in range(9):
            for i in range(9):
                if self._grid[i][j]:
                    self._column_value[j].append(self._grid[i][j])
                    if len(set(self._column_value[j])) != len(self._column_value[j]):
                        return 0
        # duplicate in box
        for j in range(9):
            for i in range(9):
                if self._grid[i][j]:
                    self._box_value[(i // 3) * 3 + j // 3].append(self._grid[i][j])
                    if len(set(self._box_value[(i // 3) * 3 + j // 3])) != len(self._box_value[(i // 3) * 3 + j // 3]):
                        return 0
        return 1

    # prints out to standard output
    def preassess(self):
        if self._init_params():
            print('There might be a solution.')
        else:
            print('There is clearly no solution.')

    # print grid to tex file
    def _tex_output(self, param):
        filename = self.filename + param
        with open(filename + '.tex', 'w') as tex_file:
            print(defaultbegin, file=tex_file)
            for i in range(9):
                print(f'% Line {i+1}\n', end='', file=tex_file)
                for j in range(9):
                    out = ''
                    l = [[] for _ in range(4)]
                    if self._grid[i][j] != 0:
                        out = self._grid[i][j]
                    if param == '_marked':
                        if (i, j) in self._original_markup:
                            for e in sorted(self._original_markup[(i, j)]):
                                if e < 7:
                                    l[int((e - 1) / 2)].append(str(e))
                                else:
                                    l[3].append(str(e))
                        for e in range(4):
                            if l[e]:
                                l[e] = ' '.join(_ for _ in l[e])
                            else:
                                l[e] = ''
                    elif param == '_worked':
                        if (i, j) in self._original_markup:
                            for e in sorted(self._original_markup[(i, j)]):
                                if e < 7:
                                    if (i, j) in self._markup and e in self._markup[(i, j)]:
                                        l[int((e - 1) / 2)].append(str(e))
                                    else:
                                        l[int((e - 1) / 2)].append('\cancel{'+str(e)+'}')
                                elif (i, j) in self._markup and e in self._markup[(i, j)]:
                                    l[3].append(str(e))
                                else:
                                    l[3].append('\cancel{'+str(e)+'}')
                        for e in range(4):
                            if l[e]:
                                l[e] = ' '.join(_ for _ in l[e])
                            else:
                                l[e] = ''
                    else:
                        for e in range(4):
                            l[e] = ''
                    if j in {3, 6}:
                        print('\n', end='', file=tex_file)
                    if j < 8:
                        print(f'\\N{{{l[0]}}}{{{l[1]}}}{{{l[2]}}}{{{l[3]}}}{{{out}}} &', end='', file=tex_file)
                    elif i in {2, 5}:
                        print(f'\\N{{{l[0]}}}{{{l[1]}}}{{{l[2]}}}{{{l[3]}}}{{{out}}} \\\ \hline\hline\n', file=tex_file)
                    elif i == 8:
                        print(f'\\N{{{l[0]}}}{{{l[1]}}}{{{l[2]}}}{{{l[3]}}}{{{out}}} \\\ \hline\hline', file=tex_file)
                    else:
                        print(f'\\N{{{l[0]}}}{{{l[1]}}}{{{l[2]}}}{{{l[3]}}}{{{out}}} \\\ \hline\n', file=tex_file)
                    if j in {0, 1, 3, 4, 6, 7}:
                        print(' ', end='', file=tex_file)
            print(defaultend, file=tex_file)

        os.system('pdflatex ' + filename)
        for file in (self.filename + param + ext for ext in ('.aux', '.log')):
            os.remove(file)

    # 原始题
    def bare_tex_output(self):
        # self.init_params()
        self._tex_output('_bare')

    def _get_markup(self):
        for i in range(9):
            self._row_available[i] = list(set(self._row_available[i]).difference(self._row_value[i]))
            self._column_available[i] = list(set(self._column_available[i]).difference(self._column_value[i]))
            self._box_available[i] = list(set(self._box_available[i]).difference(self._box_value[i]))
        for i in range(9):
            for j in range(9):
                if not self._grid[i][j]:
                    self._markup[(i, j)] = list(set(self._row_available[i]).intersection \
                        (set(self._column_available[j])).intersection(
                        set(self._box_available[(i // 3) * 3 + j // 3])))

    def _update_markup(self, row, column, number):
        for e in range(9):
            if not self._grid[row][e] and number in self._markup[(row, e)]:
                self._markup[(row, e)].remove(number)
        for e in range(9):
            if not self._grid[e][column] and number in self._markup[(e, column)]:
                self._markup[(e, column)].remove(number)
        box = (row // 3) * 3 + column // 3
        for i in range(3 * int(box / 3), 3 * int(box / 3) + 3):
            for j in range(3 * (box % 3), 3 * (box % 3) + 3):
                if not self._grid[i][j] and number in self._markup[(i, j)]:
                    self._markup[(i, j)].remove(number)

    def _set_cell(self, i, j, number):
        # print('set_cell:', (i+1, j+1), number)
        self._grid[i][j] = number
        self._row_value[i].append(number)
        self._column_value[j].append(number)
        self._box_value[(i // 3) * 3 + j // 3].append(number)
        self._markup.pop((i, j))
        self._update_markup(i, j, number)

    def _forced_markup(self):
        flag = min(len(i) for i in self._markup.values())
        if flag != 1:
            return
        i, j = min(self._markup.items(), key=lambda x: len(x[1]))[0]
        self._set_cell(i, j, self._markup[(i, j)][0])
        self._forced_markup()

    def _forced_hidden(self):
        self._forced_markup()
        self._forced_box()
        self._forced_row()
        self._forced_column()

    def _forced_box(self):
        frequency = defaultdict(int)
        for i in range(9):
            for e in self._box_value[i]:
                frequency[e] += 1
        frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        for high_frequency_number, _ in frequency:
            for x in range(9):
                possible_force = []
                if high_frequency_number in self._box_available[x]:
                    for i in range(3 * int(x / 3), 3 * int(x / 3) + 3):
                        for j in range(3 * (x % 3), 3 * (x % 3) + 3):
                            if (i, j) in self._markup.keys() and high_frequency_number in self._markup[(i, j)]:
                                possible_force.append((i, j))
                    if len(possible_force) == 1:
                        i, j = possible_force[0]
                        self._set_cell(i, j, high_frequency_number)
                        self._forced_box()

    def _forced_row(self):
        frequency = defaultdict(int)
        for i in range(9):
            for e in self._row_value[i]:
                frequency[e] += 1
        frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        for high_frequency_number, _ in frequency:
            for i in range(9):
                possible_force = []
                if high_frequency_number in self._row_available[i]:
                    for j in range(9):
                            if (i, j) in self._markup.keys() and high_frequency_number in self._markup[(i, j)]:
                                possible_force.append((i, j))
                    if len(possible_force) == 1:
                        i, j = possible_force[0]
                        self._set_cell(i, j, high_frequency_number)
                        self._forced_row()

    def _forced_column(self):
        frequency = defaultdict(int)
        for i in range(9):
            for e in self._column_value[i]:
                frequency[e] += 1
        frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        for high_frequency_number, _ in frequency:
            for j in range(9):
                possible_force = []
                if high_frequency_number in self._column_available[j]:
                    for i in range(9):
                        if (i, j) in self._markup.keys() and high_frequency_number in self._markup[(i, j)]:
                            possible_force.append((i, j))
                    if len(possible_force) == 1:
                        i, j = possible_force[0]
                        self._set_cell(i, j, high_frequency_number)
                        self._forced_column()

    def _get_preemptive_set(self):
        self._forced_hidden()
        self._get_preemptive_set_box()
        self._get_preemptive_set_row()
        self._get_preemptive_set_column()

    def _get_preemptive_set_box(self):
        for x in range(9):
            for i in range(3 * int(x / 3), 3 * int(x / 3) + 3):
                for j in range(3 * (x % 3), 3 * (x % 3) + 3):
                    if not self._grid[i][j]:
                        numbers = self._markup[(i, j)]
                        if tuple(numbers) not in self._preemptive_set_box.keys():
                            possbile_cell = [(i, j)]
                            for p in range(3 * int(x / 3), 3 * int(x / 3) + 3):
                                for q in range(3 * (x % 3), 3 * (x % 3) + 3):
                                    if (p, q) in self._markup.keys() and not (p == i and q == j) and \
                                                            encode(self._markup[(i, j)]) | encode(
                                                        self._markup[(p, q)]) == encode(self._markup[(i, j)]):
                                        possbile_cell.append((p, q))
                            if len(self._markup[(i, j)]) == len(possbile_cell):
                                self._preemptive_set_box[tuple(numbers)] = possbile_cell
                                # print(f'\nin box {x+1}:',tuple(numbers),possbile_cell)
                                self._use_preemptive_set_box(x, numbers, possbile_cell)

    def _get_preemptive_set_row(self):
        for i in range(9):
            for j in range(9):
                if not self._grid[i][j]:
                    numbers = self._markup[(i, j)]
                    if tuple(numbers) not in self._preemptive_set_row.keys():
                        possbile_cell = [(i, j)]
                        p = i
                        for q in range(9):
                            if (p, q) in self._markup.keys() and not (p == i and q == j) and \
                                                    encode(self._markup[(i, j)]) | encode(
                                                self._markup[(p, q)]) == encode(self._markup[(i, j)]):
                                possbile_cell.append((p, q))
                        if len(self._markup[(i, j)]) == len(possbile_cell):
                            self._preemptive_set_row[tuple(numbers)] = possbile_cell
                            # print(f'\nin row {i+1}:',tuple(numbers),possbile_cell)
                            self._use_preemptive_set_row(i, numbers, possbile_cell)

    def _get_preemptive_set_column(self):
        for i in range(9):
            for j in range(9):
                if not self._grid[i][j]:
                    numbers = self._markup[(i, j)]
                    if tuple(numbers) not in self._preemptive_set_column.keys():
                        possbile_cell = [(i, j)]
                        q = j
                        for p in range(9):
                            if (p, q) in self._markup.keys() and not (p == i and q == j) and \
                                                    encode(self._markup[(i, j)]) | encode(
                                                self._markup[(p, q)]) == encode(self._markup[(i, j)]):
                                possbile_cell.append((p, q))
                        if len(self._markup[(i, j)]) == len(possbile_cell):
                            self._preemptive_set_column[tuple(numbers)] = possbile_cell
                            # print(f'\nin column {j+1}:',tuple(numbers),possbile_cell)
                            self._use_preemptive_set_column(j, numbers, possbile_cell)

    def _use_preemptive_set_box(self, box, numbers, possbile_cell):
        for i in range(3 * int(box / 3), 3 * int(box / 3) + 3):
            for j in range(3 * (box % 3), 3 * (box % 3) + 3):
                if (i, j) not in possbile_cell and not self._grid[i][j]:
                    for e in numbers:
                        if e in self._markup[(i, j)]:
                            self._markup[(i, j)].remove(e)
        self._get_preemptive_set()

    def _use_preemptive_set_row(self, row, numbers, possbile_cell):
        i = row
        for j in range(9):
            if (i, j) not in possbile_cell and not self._grid[i][j]:
                for e in numbers:
                    if e in self._markup[(i, j)]:
                        self._markup[(i, j)].remove(e)
        self._get_preemptive_set()

    def _use_preemptive_set_column(self, column, numbers, possbile_cell):
        j = column
        for i in range(9):
            if (i, j) not in possbile_cell and not self._grid[i][j]:
                for e in numbers:
                    if e in self._markup[(i, j)]:
                        self._markup[(i, j)].remove(e)
        self._get_preemptive_set()

    # 能确定的填上
    def forced_tex_output(self):
        self._init_params()
        self._get_markup()
        self._forced_box()
        self._original_markup = self._markup.copy()
        self._tex_output('_forced')

    # 每个cell的可能性填上
    def marked_tex_output(self):
        self._init_params()
        self._get_markup()
        self._forced_box()
        self._original_markup = self._markup.copy()
        self._tex_output('_marked')

    # which the preemptive set technique has been applied.
    def worked_tex_output(self):
        self._init_params()
        self._get_markup()
        self._forced_box()
        self._original_markup = copy.deepcopy(self._markup)
        self._get_preemptive_set()
        self._tex_output('_worked')


def encode(s):
    x = 0
    for e in s:
        x |= 1 << (e - 1)
    return x

#
# def decode(y):
#     s = set()
#     n = 1
#     while y:
#         # if the last one is 1, if so, add to set,
#         # if not, delete it, then check next one
#         if y & 1:
#             s.add(n)
#         y >>= 1
#         n += 1
#     return s

sudoku = Sudoku('sudoku_1.txt')
sudoku.preassess()
sudoku.bare_tex_output()
sudoku.forced_tex_output()
sudoku.marked_tex_output()
sudoku.worked_tex_output()

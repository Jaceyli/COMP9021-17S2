# Creates a class to represent a permutation of 1, 2, ..., n for some n >= 0.
#
# An object is created by passing as argument to the class name:
# - either no argument, in which case the empty permutation is created, or
# - "length = n" for some n >= 0, in which case the identity over 1, ..., n is created, or
# - the numbers 1, 2, ..., n for some n >= 0, in some order, possibly together with "lengh = n".
#
# __len__(), __repr__() and __str__() are implemented, the latter providing the standard form
# decomposition of the permutation into cycles (see wikepedia page on permutations for details).
#
# Objects have:
# - nb_of_cycles as an attribute
# - inverse() as a method
#
# The * operator is implemented for permutation composition, for both infix and in-place uses.
#
# Written by JINGXUAN LI and Eric Martin for COMP9021


class PermutationError(Exception):
    def __init__(self, message):
        self.message = message


class Permutation:
    def __init__(self, *args, length=None):

        if length is not None and length < 0:
            raise PermutationError('Cannot generate permutation from these arguments')
        if args is () and length is None:
            pass
        elif args is () and length is not None and length > 0:
            l = [e for e in range(1, length + 1)]
            args = tuple(l)
        elif sum(e for e in args if isinstance(e, int)) is 0:
            raise PermutationError('Cannot generate permutation from these arguments')
        if 0 in args:
            raise PermutationError('Cannot generate permutation from these arguments')
        if length is not None and length != len(args) and args:
            raise PermutationError('Cannot generate permutation from these arguments')

        if length is 0:
            args = ()

        self.args = args
        self.__str__()

    def __len__(self):
        return len(self.args)

    def __repr__(self):
        return f'Permutation{self.args}'

    def __str__(self):
        if self.args is ():
            self.nb_of_cycles = 0
            return "()"
        l = [e for e in self.args]
        N = [[] for _ in range(len(l))]
        M = []
        i = 0
        for e in range(1, len(l) + 1):
            flag = 0
            if l[e - 1] not in M:
                tmp = e
                N[i].append(e)
                M.append(e)
                while l[e - 1] != tmp and e <= len(l):
                    flag = 1
                    e = l[e - 1]
                    M.append(e)
                    N[i].append(e)
            if flag or l[e - 1] == tmp:
                i += 1
        result = []
        # print(N)
        for e in N:
            if e:
                max, max_t = 0, 0
                for t in range(len(e)):
                    if e[t] > max:
                        max = e[t]
                        max_t = t
                e = e[max_t:] + e[:max_t]
                result.append(e)
        result.sort()
        self.nb_of_cycles = len(result)
        result_string = ''
        for e in result:
            result_string += '('
            for x in e:
                result_string += str(x) +' '
            result_string = result_string[:-1]
            result_string += ')'
        return result_string

    def __mul__(self, permutation):
        l1 = [e for e in self.args]
        l2 = [e for e in permutation.args]
        if len(l1) != len(l2):
            raise PermutationError('Cannot compose permutations of different lengths')
        if [e for e in l1 if e > len(l1)] or [e for e in l1 if e > len(l2)]:
            raise PermutationError('Cannot compose permutations of different lengths')
        result = [l2[l1[e] - 1] for e in range(0, len(l1))]
        return Permutation(*tuple(result))



    def __imul__(self, permutation):
        l1 = [e for e in self.args]
        l2 = [e for e in permutation.args]
        result = [l2[l1[e] - 1] for e in range(0, len(l1))]
        self.args = tuple(result)
        return Permutation(*tuple(result))


    def inverse(self):
        l = [e for e in self.args]
        l1 = [e for e in range(1, len(l)+1)]
        dic = {}
        for e in l1:
            dic[e] = l[e-1]
        new_dic = dict((k, v) for v, k in dic.items())
        new_dic = sorted(new_dic.items(), key=lambda x: x[0])
        result = []
        for e in new_dic:
            result.append(e[1])
        return Permutation(*tuple(result))

        # Insert your code for helper functions, if needed


##Permutation('No way!')
##Permutation(length = -1)
##Permutation(3, 2, 1, length = 3)
##Permutation([3, 2, 1])
##p = Permutation()
##print(p)

##p = Permutation(2, 5, 4, 3, 1, length = 5)
##p
##q = p.inverse()
##print(q)
##p1 = Permutation(5, 4, 3, 2, 1)
##p2 = Permutation(2, 4, 1, 5, 3)
##q = p1 * p2
##print(q)
##q.nb_of_cycles

##p = Permutation(1,2,3)*Permutation(length=2)

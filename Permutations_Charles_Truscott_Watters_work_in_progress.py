# -*- coding: utf-8 -*-
"""
Authored by Charles Truscott from scratch.
:-)
I love MIT
Thank you Massachusetts Institute of Technology (edX student)
Authored 19/07/2022 in Byron Bay, NSW, 2481 Australia (Terra Australis, Van Diemen's Land)
Working on permutations of a subset. MIT Student Charles Truscott Watters
Set: ['1']:
Permutations of the set: []
Working on permutations of a set. MIT Student Charles Truscott Watters
Set: ['1', '2']:
Permutations of the set: [['2'], ['1'], ['2', '1'], ['1', '2']]
Working on permutations of a set. MIT Student Charles Truscott Watters
Set: ['1', '2', '3']:
Permutations of the set: [['3'], ['2', '3'], [], ['3', '2'], ['1', '2'], ['1', '2', '3'], ['3', '1'], ['1', '3'], ['2'], ['1']]
Working on permutations of a set. MIT Student Charles Truscott Watters
Set: ['1', '2', '3', '4']:
Permutations of the set: [['3', '4'], ['4'], ['3'], ['2', '3', '4'], ['4', '3'], ['3'], ['2', '3'], ['1', '2', '3', '4'], ['4', '3', '2'], [], ['4', '1'], ['1', '4'], ['3', '2'], ['1', '2'], ['1', '2', '3'], ['2'], ['1']]
Working on permutations of a set. MIT Student Charles Truscott Watters
Set: ['1', '2', '3', '4', '5']:
Permutations of the set: [['5'], ['4'], ['4', '5'], ['5', '4'], ['3', '4'], ['3', '4', '5'], ['4'], ['3'], ['5', '4', '3'], ['2', '3', '4'], ['2', '3', '4', '5'], ['4', '3'], ['3'], ['2', '3'], ['5', '4', '3', '2'], ['1', '2', '3', '4'], ['1', '2', '3', '4', '5'], ['5', '1'], ['1', '5'], ['4', '3', '2'], [], ['3', '2'], ['1', '2'], ['1', '2', '3'], ['2'], ['1']]
Press any key to continue . . .

Factorial of n, there are:
1 x 1 combinations
1 x 2 combinations and two subsets
1 x 2 x 3 combinations and 3 subsets
1 x 2 x 3 x 4 combinations and 4 subsets
1 x 2 x 3 x 4 x 5 combinations and 5 subsets

Thank you Massachusetts Institute of Technology

I love you Dad Mark William and uncle Rodney 


So feasibly speaking it is a subset and the permutations, combinations of each subset down to zero, one
1234 can be arranged 4! ways which is 1 x 2 x 3 x 4 = 6 x 4 = 24 ways, 1234, 2134, 2314, 2341, 4321 etc.
(n - 1) length
"""
import math
import os
import random

def find_factors(x):
    y = x
    z = x
    factors = []
    while x > 1:
        for q in range(x, 0, -1):
            for r in range(y, 0, -1):
                if q * r == x:
                    factors.append([q, r])
                    if r * r == q:
                        factors.append([r, r])
        x -= 1
    return factors

def return_permutation_set(x):
    print("Working on permutations of a set. MIT Student Charles Truscott Watters")
    y = []
#    print(find_factors(len(x)))
    factors = find_factors(math.factorial(len(x)))
    for item in factors:
        item[0] -= 1
        item[1] -= 1
#    print(factors)
    for other_val in factors:
        if other_val[0] < other_val[1]:
            y.append(x[other_val[0]:other_val[1]])
            if other_val[1] % 2 == 0:
                y.append(x[other_val[0]:other_val[1] + 1])
        if other_val[0] > other_val[1]:
            y.append(x[other_val[0]:other_val[1]:-1])
        if other_val[0] == other_val[1]:
            y.append(x[other_val[0]:other_val[1]])
        if other_val[1] == len(x) - 1 and other_val[0] == 0:
            temp = []
            temp_two = []
            temp.append(x[other_val[1]])
            temp.append(x[other_val[0]])
            temp_two.append(x[other_val[0]])
            temp_two.append(x[other_val[1]])
            y.append(temp)
            y.append(temp_two)
    for i in y:
        while y.count(i) > 1:
            y.remove(i)
    print("Set: {}:".format(x))
    print("Permutations of the set: {}".format(y))
    return y

def main():
    list_one = ["1"]
    list_two = ["1", "2"]
    list_three = ["1", "2", "3"]
    list_four = ["1", "2", "3", "4"]
    list_five = ["1", "2", "3", "4", "5"]
    list_six = []
#    list_six += list_five[4]
#    list_six += list_five[0]
#    print(list_six)
    return_permutation_set(list_one)
    return_permutation_set(list_two)
    return_permutation_set(list_three)
    return_permutation_set(list_four)
    return_permutation_set(list_five)
if __name__ == "__main__": main()

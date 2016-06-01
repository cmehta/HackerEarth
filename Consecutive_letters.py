'''
You simply need to perform one operation - if there are two same consecutive letters, delete one of them.

Input:
The first line contains an integer T, denoting the number of test cases.
Each test case consists of a string S, which consists of only lower case letters.

Output:
For each test case, print the answer to the given problem.

SAMPLE INPUT
3
abb
aaab
ababa

SAMPLE OUTPUT
ab
ab
ababa
'''
from functools import reduce
if __name__ == '__main__':
    T = int(raw_input())
    for i in range(T):
        S = raw_input()
        l = 0
        ch = S[0]
        String = S[0]
        while l < len(S):
            if ch == S[l]:
                l += 1
            else:
                ch = S[l]
                String = String + ch
                l += 1
        print
        String



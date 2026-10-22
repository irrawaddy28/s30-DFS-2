'''
394 Decode String
https://leetcode.com/problems/decode-string/description/

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"


Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].

Solution:
1. Iterative using stacks
Define two stacks, one for numbers, the other for characters.
For each character read from the input string, do:
a) If char == number, push char into number stack
b) If char == [ or 'a'-'z', push char into characters stack
c) If char == ']', pop all elements from the characters stack until you encounter a ']'. Concatenate all poppped elements and push the concatenated string into the characters stack.

Once the entire input string is read, pop all elements from the characters stack until it is empty. Concatenate all the popped elements. The concatenated string is the result.
Time: O(M), Space: O(N), N = no. of characters, M = product of digits in the string
https://youtu.be/yUmWCBhT_xU?t=1508

2. DFS using recursion
Time: O(M), Space: O(N), N = no. of characters, M = product of digits in the string
https://youtu.be/yUmWCBhT_xU?t=2901
https://youtu.be/yUmWCBhT_xU?t=3295 (Discussion on why use global index i? Ans: avoids creating substrings at every dfs call)
https://youtu.be/yUmWCBhT_xU?t=3876 (TC)
'''

def decodeStringStack(s):
    '''
        Iterative solution using stack
        Time: O(M), Space: O(N) (worst case space if N nested levels)
    '''
    curr_str = ''
    curr_num = 0
    characters = []
    numbers = []
    for c in s:
        if c.isdigit():
            curr_num = curr_num*10 + (ord(c) - ord('0'))
        elif c.isalpha():
            curr_str = curr_str + c
        elif c == '[':
            numbers.append(curr_num)
            characters.append(curr_str)
            curr_num = 0
            curr_str = ''
        elif c == ']':
            papa_str = characters.pop()
            baby_str = curr_str*numbers.pop()
            curr_str = papa_str + baby_str
    return curr_str

def decodeStringDFS(s):
    '''
        Recursive solution using DFS (easier to understand by comparing with the stack solution)
        Time: O(M), Space: O(N) (worst case space if N nested levels)
    '''
    def dfs(s):
        nonlocal i
        curr_num = 0
        curr_str = ''
        while i < N:
            c = s[i]
            i += 1
            if c.isdigit():
                curr_num = curr_num*10 + (ord(c) - ord('0'))
            elif c.isalpha():
                curr_str = curr_str + c
            elif c == '[':
                ret_str = dfs(s)
                baby_str = curr_num*ret_str # curr_num ~ numbers.pop()
                papa_str = curr_str # curr_str ~ characters.pop()
                curr_str = papa_str + baby_str
                curr_num = 0
            elif c == ']':
                return curr_str
        return curr_str

    N = len(s)
    i = 0
    return dfs(s)


def run_tests():
    tests = [("3[a2[c]]", "accaccacc"),
             ("3[ab02[c]01[b]]", "abccbabccbabccb"),
             ("3[a2[c]2[b]]", "accbbaccbbaccbb"),
             ("2[a3[c2[x]]y]", "acxxcxxcxxyacxxcxxcxxy"),
             ("3[a]2[bc]", "aaabcbc"),
             ("3[z]2[2[y]pq4[2[jk]e1[f]]]ef", "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"),
    ]
    for test in tests:
        s, ans = test[0], test[1]
        print(f"\nEncoded String = {s}")
        for method in ['stack', 'dfs']:
            if method == 'stack':
                output = decodeStringStack(s)
            elif method == 'dfs':
                output = decodeStringDFS(s)
            print(f"Method {method}: Decoded String = {output}")
            passed = (ans == output)
            assert passed == True, f"Test case failed"
            print(f"Pass: {passed}")
    print(f"\nDONE")

run_tests()
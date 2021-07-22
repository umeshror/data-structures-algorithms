"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


def length_of_longest_substring(strng):
    stng_list = []
    longest = 0
    for char in strng:

        if char in stng_list:
            longest = max(longest, len(stng_list))
            index = mylist.index(char)
            mylist = mylist[index + 1:]  # remove all items before the repeated item including itself

        stng_list.append(char)

    return max(longest, len(stng_list))


print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring(" "))
print(length_of_longest_substring("dvdf"))
print(length_of_longest_substring("ynyo"))

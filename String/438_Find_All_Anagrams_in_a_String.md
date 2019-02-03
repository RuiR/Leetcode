## 438. Find All Anagrams in a String

When I started to solve this problem, I though it could be done quickly. But in fact, it cost me much longer time than expected.

The errors I made in solving this problem are:

1. The hash table of substring in s should only include character which is in p instead of all characters.
2. The condition of while should be i < len(s) instead of i < len(s) - len(q) because we move the sliding window all the way right, and i is the right end of sliding window. so it could reach len(s) - 1
3. The start point when we find a match. It should be [i-count+1] instead of [i-count], this can be solved by using a sample to derive the equation.
4. Because the i increase by one, there isn't a jump of i. We can use for loop instead of while.

The solution is:

```python3
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        len_s = len(s)
        len_p = len(p)
        if len_s < len(p):
            return []
        hash_p = Counter(p)
        ret = []
        hash_s = {}
        count = 0
        i = 0
        for i in range(len(s)):
            if s[i] not in p:
                hash_s = {}
                count = 0
            else:
                if s[i] not in hash_s:
                    hash_s[s[i]] = 1
                else:
                    hash_s[s[i]] += 1
                count += 1
                if count == len_p:
                    if hash_s == hash_p:
                        ret.append(i+1-len_p)
                    hash_s[s[i-count+1]] -= 1
                    count -= 1
        return ret
```

# https://leetcode.com/problems/ransom-note/

# runtime: 77 ms 
def canConstruct(ransomNote: str, magazine: str):
    for i in set(ransomNote):
        if ransomNote.count(i) > magazine.count(i):
            return False
    return True

# runtime: 60 ms
# one-liner using collections.Counter
def canConstruct(ransomNote: str, magazine: str):
    import collections
    return not (collections.Counter(ransomNote) - collections.Counter(magazine))


#------

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: intz
    """
    #self.nums = nums
    i = 0
    for j in range(len(nums)):
        if i < 1 or nums[j] != nums[j - 1]: # if 1st != last/previous
            nums[i] = nums[j]
            i += 1
    #print(nums)
    return i

  
#------

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# runtime: 68 ms
def twoSum(self, numbers: List[int], target: int) -> List[int]:        
    # two pointer
    l, r = 0, len(numbers)-1

    while l < r:
        s = numbers[l] + numbers[r]
        if numbers[l] + numbers[r] == target:
            return [l+1, r+1]
        # if s is smaller, next number in the list will make s bigger
        elif s < target:
            l += 1
        # if l is bigger, previous number in the list will make s smaller 
        else:
            r -= 1

# alternative using dictionary
# runtime: 48 ms
def twoSum2(numbers, target):
    d = {}
    for i, num in enumerate(numbers):
        
        # if the difference between target and a num is in the list numbers, then the difference + num is the target (duh...)
        if target-num in d:
            print(target, num, target-num)
            return [d[target-num]+1, i+1]
        d[num] = i
        

#-------

# https://leetcode.com/problems/three-divisors/
# runtime: 40ms
# memory: 100% faster than other submissions
class Solution:
    def isThree(self, n: int) -> bool:
        return len([x for x in range(1, n+1) if n % x == 0]) == 3
      
      
#-------

# https://leetcode.com/problems/merge-strings-alternately/
# runtime: 32ms

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #very rudimentary but straightforward
        string = ''
               
        o,t = len(word1), len(word2)
        n = min(o,t)
        
        for i in range(n):
            string += word1[i]
            string += word2[i]
                
        if o > t:
            string += word1[n:]
        else:   
            string += word2[n:]
            
        return string

# alternative
# runtime: 32ms
# less memory used than the rest
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ''

        for i in range(min(len(word1), len(word2))):
            string += word1[i] + word2[i]

        return string + word1[i+1:] + word2[i+1:]
      
# using python library itertools
# runtime: 32ms
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(x+y for x,y in zip_longest(word1, word2, fillvalue=""))

      
#-------

# https://leetcode.com/problems/truncate-sentence/
# runtime: 32 ms
# memory: 14.4 MB
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])
    
    
#-------
#https://leetcode.com/problems/unique-email-addresses/submissions/
# runtime: 52ms
# memory: 14.5 MB
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        l = []

        for email in emails:
            #print(email)
            index = email.find('@')
            local = email[:index].replace('.', '')
            domain = email[index:]
            #print('local is:', local, 'AND domain is:', domain)

            if '+' in local:
                l.append(local[:local.find('+')] + domain)
            else:
                l.append(local + domain)

        #print(l)    
        return len(set(l))
    
# clean up:
# runtime: 48ms
# memory: 14.4 MB
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        l = set()
        for email in emails:
            local, domain = email.split('@') 
            local = local.split('+')[0].replace('.', '')
            l.add(local + '@' + domain)
            
        return len(l)

# one-liner:
# runtime: 52ms
# memory: 14.5 MB
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        return len(set([email.split('@')[0].split('+')[0].replace('.', '') + '@' + email.split('@')[1] for email in emails]))


#-------

# https: https://leetcode.com/problems/subsets-ii/

# use Python library
# from itertools import combinations 
# leetcode includes it

# runtime: 36ms
# memory: 14.6 MB
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        l = []
        for i in range(len(nums)+1):
            for combo in combinations(nums,i):
                combo = sorted(list(combo))
                if combo not in l:
                    l.append(combo)
        return l


#-------

# https: leetcode.com/problems/number-of-different-integers-in-a-string/
# runtime: 20 ms faster than 99.64%
# memory: 14.3 MB

class Solution:
    def numDifferentIntegers(self, word: str) -> int:

        string = ''
        
        for ele in word:
            if ele.isdigit():
                string += ele
            else:
                string += ' '
                
        return len(set([int(x) for x in string.split()]))
        
# alternative using map()
# runtime: 28ms
# memory: 14.3 MB

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = ''.join(c if c.isdigit() else ' ' for c in word)
        return len(set(map(int, s.split())))


#-------
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# runtime: 48ms
# memory: 13.4 MB

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = {} 
        res = 0
        start = 0
        for i in range(len(s)):
            if s[i] in record:
                start = max(start, record[s[i]] + 1) # key: s[i], val: record[s[i]]
            record[s[i]] = i
            # print(record)
            res = max(res, i - start + 1)
        return res
    
    
# https://leetcode.com/problems/maximum-number-of-words-you-can-type/
# runtime: 32ms
# memory: 14.4 MB

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        letters = set(brokenLetters)
        count = 0
        for word in text.split():
            if all(x not in letters for x in word):
                count += 1
        return count

    
#-------

# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/
# runtime: 32ms
# memory: 14.1 MB

class Solution:
    def getLucky(self, s: str, k: int) -> int:

        string = ''
        for letter in s:
            string += str(ord(letter)-96)

        while k > 0:
            string = str(sum([int(x) for x in string]))
            k -= 1

        return string
    
    
# alternative: more compact code
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        s = "".join(str(ord(x) - 96) for x in s) # ord('a') = 97
        for _ in range(k):
            s = str(sum(int(x) for x in s))
        return s


#-------

# https:
# runtime: 56ms
# memory: 14.2 MB

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        l = r = start
        while l >= 0 or r < len(nums):
            if l >= 0 and nums[l] == target: return start - l
            if r < len(nums) and nums[r] == target: return r - start
            l -= 1
            r += 1

#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:

#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:



#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:

#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:


#-------

# https:
# runtime:
# memory:


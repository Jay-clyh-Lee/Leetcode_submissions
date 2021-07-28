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



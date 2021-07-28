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

class Solution(object):
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

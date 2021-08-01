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

#

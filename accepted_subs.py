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

    # take advantage of the fact that numbers is an ordered list

    # if s is smaller, next number in the list will make s bigger
    elif s < target:
        l += 1

    # if l is bigger, previous number in the list will make s smaller 
    else:
        r -= 1

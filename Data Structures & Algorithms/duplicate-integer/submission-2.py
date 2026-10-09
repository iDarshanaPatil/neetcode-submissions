class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hs= set(nums)
        hashmap =[]
        for i in nums:
            if i in hashmap:
                 return True
            else:
                hashmap.append(i)
        return False
            
        
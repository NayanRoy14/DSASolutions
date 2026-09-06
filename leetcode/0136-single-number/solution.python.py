class Solution(object):
    def singleNumber(self, nums):
        r=0
        for n in nums:
            r ^= n
        return r
        
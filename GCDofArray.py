import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=[]
        b=[]
        for i in range(1,min(nums)+1):
            if min(nums)%i==0:
                a.append(i)
        for j in range(1,max(nums)+1):
            if max(nums)%j==0:
                b.append(j)
        c=[value for value in a if value in b]
        return max(c)

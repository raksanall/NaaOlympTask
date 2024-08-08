# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         def rec(nums):
#             n=len(nums)
#             if n==1:
#                 return nums[0]
#             dp=[0]*n
#             dp[0]=nums[0]
#             dp[1]=max(nums[0],nums[1])
#             for i in range(2,len(nums)):
#                     dp[i]=max(dp[i-2]+nums[i],dp[i-1])
#             return dp[-1]
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         a = rec(nums[1:])  
#         b = rec(nums[:-1])  
#         return max(a, b)
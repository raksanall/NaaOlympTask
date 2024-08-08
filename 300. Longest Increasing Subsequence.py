# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         lis = [nums[0]]
#         for i in range(1, len(nums)):
#             num = nums[i]
#             if num > lis[-1]:
#                 lis.append(num)
#             else:
#                 left, right = 0 , len(lis)-1
#                 while left < right:
#                     mid = (left + right) // 2
#                     if num > lis[mid]:
#                         left = mid + 1
#                     else:
#                         right = mid
#                 lis[left] = num
#         return len(lis)
        
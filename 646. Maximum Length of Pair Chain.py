# class Solution:
#     def findLongestChain(self, pairs: List[List[int]]) -> int:
#         pairs.sort(key = lambda x: x[1])
#         length = 1
#         end = pairs[0][1]
#         for x, y in pairs[1:]:
#             if x > end:
#                 length += 1
#                 end = y
#         return length
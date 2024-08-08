# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         intervals.sort()
#         currentend=intervals[0][1]
#         count=0
#         for s,e in intervals[1:]:
#             if s>=currentend:
#                 currentend=e
#             else:
#                 count+=1
#                 currentend=min(currentend,e)
#         return count
        
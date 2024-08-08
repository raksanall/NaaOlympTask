# class Solution:
#     def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
#         dic = {}
#         heights = []
#         result = []
#         for height, peopleAhead in people:
#             if height in dic:
#                 insort(dic[height],peopleAhead)
#             else:
#                 dic[height] = [peopleAhead]
#                 insort(heights,height)                
#         heights = heights[::-1]
#         index = 0
#         length = len(heights)       
#         while index < length:
#             height = heights[index]
#             if len(dic[height]) <=0:
#                 index+=1
#             else:
#                 temp = dic[height].pop(0)
#                 peopleAhead = temp
#                 j = 0
#                 while j < len(result):
#                     if peopleAhead == 0:
#                         break
#                     if result[j][0] >= height:
#                         peopleAhead-=1
#                     j+=1
#                 result.insert(j, [height, temp])
#         return result
        
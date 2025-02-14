# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#         res = []
#         wordSet = set(wordDict)

#         def backtrack(start,i,curr):
#             if i==len(s):
#                 if len("".join(curr))==len(s):
#                     res.append(" ".join(curr))
#                 return

#             backtrack(start,i+1,curr) #skip
#             if s[start:i+1] in wordSet:
#                 curr.append(s[start:i+1])
#                 backtrack(i+1,i+1,curr) #add
#                 curr.pop()

#         backtrack(0,0,[])
#         return res
        
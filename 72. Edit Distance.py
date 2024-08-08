        # @cache
        # def find(i,j):
        #     if i==len(word1):
        #         return len(word2)-j
        #     if j==len(word2):
        #         return len(word1)-i
        #     elif word1[i]==word2[j]:
        #         return find(i+1,j+1)
        #     else:
        #         return 1 + min(find(i+1,j+1),find(i+1,j),find(i,j+1))
        # return find(0,0)
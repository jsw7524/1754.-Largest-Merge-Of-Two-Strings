class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merge=[]
        word1Len=len(word1)
        word2Len=len(word2)
        c1,c2=0,0
        while c1 < word1Len and c2 < word2Len:
            if word1[c1:] > word2[c2:]:
                merge.append(word1[c1])
                c1+=1
            else:
                merge.append(word2[c2])
                c2+=1
        if c1 < word1Len:
            return ''.join(merge) + word1[c1:]
        return ''.join(merge) + word2[c2:]


sln=Solution()
assert "cbcabaaaaa"==sln.largestMerge(word1 = "cabaa", word2 = "bcaaa")
assert "abdcabcabcaba"==sln.largestMerge(word1 = "abcabc", word2 = "abdcaba")
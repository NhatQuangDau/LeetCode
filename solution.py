from collections import Counter
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counter = Counter(s)
        midChar = ""
        odd = 0
        halfStr = []
        for ele in counter:
            if counter[ele] % 2 != 0:
                odd += 1
                midChar = ele
            for i in range(counter[ele]//2):
                halfStr.append(ele)
        if odd > 1:
            return []
        res = []
        for per in self.generatePermutation(halfStr):
            res.append(''.join(per) + midChar + ''.join(per[::-1]))
        return res
        
    def generatePermutation(self, arr) -> List[str]:
        res = []
        length = len(arr)
        counter = Counter(arr)
        return self.backTrack([], counter, length)
        
    def backTrack(self, tempArr, counter, length) -> List[str]:
        res = []
        if len(tempArr) == length:
            res.append(tempArr.copy())
        else:
            for ele in counter:
                if counter[ele] > 0:
                    tempArr.append(ele)
                    counter[ele] -= 1
                    res += self.backTrack(tempArr, counter, length)
                    tempArr.pop()
                    counter[ele] += 1
        return res

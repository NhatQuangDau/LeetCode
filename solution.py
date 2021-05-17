#Correct solution - for more info goto https://www.youtube.com/watch?v=W9SIlE2jhBQ&t=514s
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = []
        result = ""
        for i in range(1, n+1):
            arr.append(i)
        print(arr)
        k -= 1
        pos = 1 # position from which it make factorial(n - pos) > k
        while k != 0:
            candidateIndex = k//math.factorial(n-pos)
            result += str(arr.pop(candidateIndex))
            k = k%math.factorial(n-pos)
            pos += 1
        result += "".join(map(str, arr))
        print(arr)
        return result

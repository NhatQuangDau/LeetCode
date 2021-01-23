class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.backtrack(candidates, 0, target, [], 0, result)
        return result
        
    def backtrack(self,candidates, index, target, tempCandidates,tempResult, result):
        if index == len(candidates) or tempResult + candidates[index] > target:
            return
        tempResult += candidates[index]
        tempCandidates.append(candidates[index])
        if tempResult == target:
            result.append(tempCandidates)
            return
        self.backtrack(candidates, index, target, tempCandidates.copy(), tempResult, result)
        self.backtrack(candidates, index + 1, target, tempCandidates.copy(), tempResult, result)
        
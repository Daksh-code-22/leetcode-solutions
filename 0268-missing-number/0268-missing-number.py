class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        n_sum = (n*(n+1))//2
        sum = 0

        for i in nums:
            sum = sum + i

        missing_number = n_sum - sum

        return missing_number
        
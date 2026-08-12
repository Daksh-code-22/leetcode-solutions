class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        mini = float("inf")
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= nums[high]:
                mini = min(nums[mid], mini)
                high = mid - 1

            else:
                mini = min(nums[low], mini)
                low = mid + 1
        return mini

            
        
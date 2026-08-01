class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(0, n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j -1]:
                    continue

                k = j + 1
                x = n -1
                
                while k < x:
                    total_sum = nums[i] + nums[j] + nums[k] + nums[x]
                    if total_sum == target:
                        ans.append([nums[i], nums[j], nums[k], nums[x]])
                        k += 1
                        x -= 1
                        while k < x and nums[k] == nums[k - 1]:
                            k += 1
                        while k < x and nums[x] == nums[x + 1]:
                            x -= 1
                    elif total_sum < target:
                        k += 1
                    else:
                        x -= 1
        

        return ans


                        
                        
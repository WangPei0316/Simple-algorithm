class Solution:
    def maxInWindows(self,nums,k):
        if not k or k>len(nums):
            return []
        cur_max = max(nums[:k])
        max_nums = [cur_max]
        for i in range(0,len(nums)-k):
            if nums[i] == cur_max:
                cur_max = max(nums[i+1:i+k+1])
            elif nums[i+k]>cur_max:
                cur_max = nums[i+k]
            max_nums.append(cur_max)
        return max_nums
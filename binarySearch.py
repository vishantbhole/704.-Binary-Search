
#704. Binary Search

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1

        left = 0
        right = len(nums) - 1


        while left <= right:
            mid = (left + right)// 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

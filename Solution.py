class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = []
        current_sum = 0
        for num in nums:
            current_sum += num
            running_sum.append(current_sum)
        return running_sum

    nums = [1,2,3,4]
    nums = [1,1,1,1,1]
    nums = [3,1,2,10,1]
from typing import List;

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0

        left = 0
        right = len(height) - 1

        while left < right:
            x_len = right - left
            y_len = min(height[left],height[right])
            maxArea = max(maxArea,x_len*y_len)

            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        return maxArea


input = [1,1]
print(Solution().maxArea(input))
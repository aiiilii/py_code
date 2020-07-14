from typing import List

class ContainerWithMostWater:

    def maxArea(self, height: List[int]) -> int:
        if not height or len(height) < 2:
            return 0

        max_area = 0

        left = 0
        right = len(height) - 1

        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if (height[left] <= height[right]):
                left += 1
            else:
                right -= 1

        return max_area

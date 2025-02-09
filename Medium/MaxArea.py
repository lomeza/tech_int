"""
This solution takes the height of each object
and calculates the max area between them.

obj1=MaxArea()
obj1.bucketMaxArea(arr1)

"""


class MaxArea:
    def bucketMaxArea(heights):
        #declarations of left and right pointers
        l, r = 0, len(heights) - 1
        res = 0
        
        #while left side is < right we will calculate
        while l < r:
            #calculate area then replace res with higher number
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            
            #increment if left is lt or eq to r side
            if heights[l] <= heights[r]:
                l += 1
            #else de-inc right side and recalculate
            else:
                r -= 1
        return res
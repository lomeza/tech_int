class MaxArea:
    def bucketMaxArea(self, heights):
        #dec's left and right pointer
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            #calculate area then replace res if less than area
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            #increment if left is lt or eq to r side
            if heights[l] <= heights[r]:
                l += 1
            #else de-inc right side
            else:
                r -= 1
        return res
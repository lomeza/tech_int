    """
    Given an array of integers numbers that is sorted in low to high numbers.
    Return the indices (1-indexed) of two numbers, [index1, index2], 
    such that they add up to a given target number target and index1 < index2. 
    Note that index1 and index2 cannot be the same array element.
    """
    
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        #left and right declarations
		l, r = 0, len(numbers) - 1
		
		#single whild loop for O(1) space
        while l < r:
			#sum of left and right number
            curSum = numbers[l] + numbers[r]
			#if the sum is greater than target deincrement right side
            if curSum > target:
                r -= 1
            #if the sum is less than target increment left side
			elif curSum < target:
                l += 1
			#return the solution if found
            else:
                return [l + 1, r + 1]

		return []
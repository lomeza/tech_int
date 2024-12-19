"""
Instructions:
Given a list of int's we want to find the longest
consecutive ordered list of int's.

Input:
testList=[1,3,4,5,6,9,12,15,16]

Example: 
obj1=longestConsecutive()
obj1.longestConsecutive(testList)

Output:
4

"[3,4,5,6]" is the longest list

"""

#Sub optimal solution - takes long time when very long list as input
import collections;

class longestConsecutive:
    def longestConsecutive(self, nums: list[int]) -> int:
        numsDict = collections.defaultdict(set)
        nums.sort()
        nums_to_seperate_by=[]
        
        #loop to see which nums and where to seperate dictionary
        for i in range(len(nums)):
            if nums[i] - 1 not in nums:
                nums_to_seperate_by.append(nums[i])
        
        #loop to add nums to dictionary seperated by length of "nums_to_seperate_by"     
        for j in range(len(nums_to_seperate_by)):
            numsDict[j].add(nums_to_seperate_by[j])
            #inside loop to add any number only with another num below or above it
            for k in range(len(nums)):
                if nums[k] + 1 in numsDict[j] or nums[k] - 1 in numsDict[j]:
                    numsDict[j].add(nums[k])
        
        #to capture highest dictionary length
        lenCount=0
        
        #final comparison to find longest length
        for items in numsDict.values():
            if lenCount <= len(list(items)):
                lenCount=len(list(items))
            
        return lenCount
""" 
Instructions:
Given an integer array nums, return true if there are any duplicates

Example:
test1=Duplicates()
test1.hasDupe([1,2,3,6,7,9,1])

output:true
"""

class Duplicates:
    #def should return bool
    def hasDupe(self, nums: list[int]) -> bool:
        #inital declarations
        isDupe = False
        listCheck=[]
        
        #loop through list of digits
        for digits in nums:
            #check to see if number previously added into list
            if digits in listCheck:
                isDupe = True
                return isDupe
            #add number to list if not duped
            listCheck.append(digits)
                
        return isDupe
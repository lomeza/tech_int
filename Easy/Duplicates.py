""" Given an integer array nums, 
    return true if any value appears more than once in the array, 
    otherwise return false."""

class DuplicateSol:
    #def should return bool
    def hasDupe(self, nums: list[int]) -> bool:
        #inital declarations
        isDupe = False
        lists=[]
        
        #loop through list
        for digits in nums:
            #check to see if number previously added into list
            if digits in lists:
                isDupe = True
                return isDupe
            #add number to list if not duped
            lists.append(digits)
                
        return isDupe
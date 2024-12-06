class twoSumSol:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i,j = 0, 0
        #loop to parse list 
        for i in range(len(nums)):
            #inner loop to check each item in list
            for j in range(len(nums)):
                
                if i == j:
                    j+=1
                
                else:
                    num=nums[i]+nums[j]
                    if num == target:
                        ans=[i,j]
                        return ans
                        
            i+=1
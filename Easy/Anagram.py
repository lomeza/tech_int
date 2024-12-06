class anagramSol:
    #func takes two strings and returns a bool
    def anagram(self, s: str, t: str) -> bool:
       #first checks to see if the len is equal or else fail
        if len(s) != len(t):
            return False

       # create two dict's to hold results
        count1, count2 = {}, {}
       # for loop checking and adding 1 for each char in string 
        for i in range(len(s)):
            count1[s[i]] = 1 + count1.get(s[i],0)
            count2[t[i]] = 1 + count2.get(t[i],0)
            print(count1)
       # returns T or F
        return count1 == count2
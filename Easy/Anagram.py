"""
Definition:
An anagram is a word or phrase formed by rearranging 
the letters of another word or phrase

Instructions:
Create Anagram checking class that will compare two strings
After loading the Anagram class use isAnagram to check strings

Example:
test1=Anagram()
test1.isAnagram("tar", "rat")

output:true
"""

class Anagram:
    #func takes two strings and returns a bool
    def isAnagram(self, s: str, t: str) -> bool:
        #first checks to see if the len is equal or else fail
        if len(s) != len(t):
            return False

        # create two dict's to hold results
        results1, results2 = {}, {}
        # for loop checking and adding 1 for each char located in strings
        for i in range(len(s)):
            results1[s[i]] = 1 + results1.get(s[i],0)
            results2[t[i]] = 1 + results2.get(t[i],0)
        # returns T or F
        return results1 == results2

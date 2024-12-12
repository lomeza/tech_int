import re

def remove_special_chars(text):

    return re.sub(r"[^\w\s]", "", text)

#receives str returns bool
class Palindrome:
	#receives str returns bool
    def isPalindrome(self, s: str) -> bool:
        #reverses string and replaces item1 then s
        item1=s[::-1]        
        item1=item1.replace(" ", "")
        s=s.replace(" ", "")
        
        #removes the special char's in both
        s=remove_special_chars(s)
        item1=remove_special_chars(item1)
       
        #change both to lowercase for comparison
        s=s.lower()
        item1=item1.lower()
        
        #comparison for palindrome
        if(s==item1):
            return True

        else:
            return False 
        
        
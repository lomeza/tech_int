"""
Instruction:
Encoder takes a list of strings and encodes them into
a single string with separators.
Decoder takes this string and reverts to list of strings

example:
test=Encoder()
test2.encode(["first", "second", "third", "fourth"])

Output:
'first/second/third/fourth'

test2.decode('first/second/third/fourth')

Output:
['first', 'second', 'third', 'fourth']

"""


class Encoder:
    
    def encode(self, strs: list[str]) -> str:
        
        #if List arg is blank encode and pass as string "blank space"
        if not strs:
            str1=' '
            return str1
        
        #all other List values are passed to the new string
        else:
            #declarations for new string, count and iterator
            newString=""
            i=0
            count=len(strs)-1
            
            #for loop that deliminates with "/"
            for item in strs:
                
                #if there is a next item we delim
                if i < count:
                    newString += str(item) + "/"
                    i+=1    
                #if its the last item then add it and return string
                else:
                    newString += str(item)
                    i+=1
            return newString


    def decode(self, s: str) -> list[str]:
        #checks to see if str is empty; then returns empty list
        if s == ' ':
            newL=[]
            return newL
        #all others are split and put into new list
        else:
            newL=[""]
        
            if bool(s):
                newL=s.split("/")
            #return list with splits; all else "" in list returned if empty
            return newL
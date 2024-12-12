class EncoderSol:

    def encode(self, strs: List[str]) -> str:
        
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


    def decode(self, s: str) -> List[str]:
        #checks to see if str is empty; then returns empty list
        if s == ' ':
            newL=[]
            return newL
        #all others are split and put into new list
        else:
            newL=[""]
        
            if bool(s):
                print(s.split("/"))
                newL=s.split("/")
            #return list with splits; all else "" in list returned if empty
            return newL
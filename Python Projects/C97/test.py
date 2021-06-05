myString=input("insert any sentence or word:")
lettercount=0
wordcount=1
for i in myString:
    lettercount=lettercount+1
    if(i==' '):
        wordcount=wordcount+1
       
print("Number of words in the string:",wordcount)
print("number of letters in the string:",lettercount)        



    
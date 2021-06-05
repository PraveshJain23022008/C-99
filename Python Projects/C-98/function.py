# declearing custom/user defined function
def countwordsfromfile():
    #defination of the function
    #storing the path of the file inside the filename variable
    filename=input("enter the file name:")
    countwords=0
    
    file=open(filename,'r')
    for line in file:
        words=line.split()
        countwords=countwords+len(words)
        print(line)
        print(words)
    print("number of word in the file :",countwords)
    
    
countwordsfromfile()    
    
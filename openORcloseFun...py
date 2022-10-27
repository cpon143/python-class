fileptr = open("list.py","r")

with open("list.py",'r') as f:
    content= f.read();
    print(content)
    
# closes the opened file 
fileptr.close()
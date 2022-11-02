#  File handling write
fp=open("touples.py","w")
fp.write("text")
with open("touples.py","r") as fp:
    con=fp.read()
    print(con)
fp.close()
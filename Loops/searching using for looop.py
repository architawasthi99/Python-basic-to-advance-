tup=(1,4,9,16,42,11,98)
key=int(input("ENTER THE NUMBER : "))
for i in tup:
    if(key==i):
        print("FOUND")
        break
else:
    print(" not found ")

import pickle
x=(10,20,30,40,50)
f=open("Binary1","wb")
pickle.dump(x,f)
f.close()

f=open("Binary1","rb")
var=pickle.load(f)
print(var)

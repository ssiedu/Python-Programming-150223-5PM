list1=['Apple\n','Banana\n','Kiwi\n','Mango\n']
file=open("Fruits.txt","w")
file.writelines(list1)
file.close()

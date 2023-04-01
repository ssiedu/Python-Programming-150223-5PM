def keyword(**data):
    print(data)
    print(data['fnum'])
    for i,j in data.items():
        print(i,j)



keyword(fnum=10,snum=20)

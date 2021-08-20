count=0
a=0
while count <= 10:
    while a != 127:
        for a in range (32,128):
            count+=1
            if count==10:
                print(f'{a} - {chr(a)}')
                count=0
            else:
                print (f'{a} - {chr(a)}',end=' ')
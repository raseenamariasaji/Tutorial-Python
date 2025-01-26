f1 = open('numbers.txt','r')
f2 = open('even.txt','w')
f3 = open('odd.txt','w')
s=" "
s = f1.read()
l=s.split()
for num in l:
    if num.isdigit():
        if int(num) %2 == 0:
            f2.write(num + '\t')
        else:
           
            f3.write(num + '\t')
f1.close()
f2.close()
f3.close()

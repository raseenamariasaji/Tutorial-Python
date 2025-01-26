# program to replace vowels with '#' symbol 
vowels ="aeiouAEIOU"
f = open('Data.txt','r')
f2 = open('content.txt','w')
s = f.read()
ns=" "
for ch in s:
    if ch in vowels:
        ns += '#'
    else:
        ns += ch
f2.write(ns)
f2.close()
f.close()
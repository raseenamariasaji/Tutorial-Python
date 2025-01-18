#Program to convert a binary number to a decimal number
binary_no=input("Enter a binary number:")
dec_no=0
expt=len(binary_no)-1
for bit in binary_no:
    dec_no=dec_no + int(bit)*2**expt
    expt=expt-1
print("The decimal equivalent of",binary_no,"is",dec_no)

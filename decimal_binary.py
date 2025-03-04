#Program to convert a decimal number to a binary number
dec_no = int(input("Enter a decimal number: "))
if dec_no == 0:
    print("The binary equivalent of", dec_no,"is","0")
else:
    binary_no = ""
    while dec_no != 0:
        b = dec_no % 2
        binary_no = str(b) + binary_no
        dec_no = dec_no // 2
    print("The binary equivalent is", binary_no)

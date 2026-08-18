

def  temp(degree, unit):
    
    if unit == "f":
        """here we are converting fehranhet to celcius """
        print("Here you can enter your degree in feheranhet")
        conversion = print( degree* 9/5 + 32 )

    elif unit == "F":
        """here we are converting fehranhet to celcius """
        print("Here you can enter your degree in feheranhet")
        conversion = print( degree* 9/5 + 32 )

    elif unit == "C":
        '''here we are convereting celcius to fehranhet'''
        print("Here you can enter your degree in celcius")
        conversion = print((degree - 32)* 5/9)

    elif unit == "c":
        '''here we are convereting celcius to fehranhet'''
        print("Here you can enter your degree in celcius")
        conversion = print((degree - 32)* 5/9)

    else :
        print("invalid option is choiced")

    return conversion

temp(96,"c")
temp(35.55555555555556,"f")
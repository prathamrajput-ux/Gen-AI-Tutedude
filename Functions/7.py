# f to c 
def ftoc(degre):
    """here we are converting fehranhet to celcius """
    print("Here you can enter your degree in feheranhet")
    celcius = print( degre* 9/5 + 32 )
    return celcius

def ctof(degree):
    '''here we are convereting celcius to fehranhet'''
    print("Here you can enter your degree in celcius")
    fehranhet = print((degree - 32)* 5/9)
    return fehranhet

ftoc(25)
ctof(77)
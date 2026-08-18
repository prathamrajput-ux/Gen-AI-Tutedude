eng_text = input("Enter your sentances or word to translate in hindi")

def translator(eng_text):
    """"This function is going tyo be saved for converting the english language into hindi language"""
    if eng_text == "Hello" or eng_text == "hello":
        print(f"The hindi translation of {eng_text} is Namaste")
    if eng_text == "thank you" or eng_text == "Thank You" or eng_text == "Thank you":
        print(f"The hindi translation of {eng_text} is dhanyawad ")
    
translator(eng_text)


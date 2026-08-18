eng_text = input("Enter your sentance and word translate in hindi")

def translator(eng_text):
    if eng_text == "hello"  or eng_text == "Hello":
        hindi = "Namaste"

    if eng_text == "Thank you" or eng_text == "thank you" or eng_text == "Thank You":
        hindi = "Dhyanawad"

    return hindi

hindi_txt = translator(eng_text)

print(hindi_txt)

def translator(eng_txt):
    if eng_txt== "hello" or eng_txt == "Hello":
        hindi= "Namaste"

    if eng_txt == "Thank you" or eng_txt == "thank you" or eng_txt == "Thank You":
        hindi = "Dhanayawad"

    return hindi

translator("Hello")    

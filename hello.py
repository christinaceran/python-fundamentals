name = input ("What is your name? ")
print ("Hello", name)
age = int(input ("How old are you? "))


if age < 0: 
    print ("That is not a valid age.")
    raise SystemExit
elif age < 18:
    print ("You are a minor.")
elif age < 30:
    print ("You are in your twenties.")
elif age < 50:
    print ("You are an adult.")
else: 
    print ("You are a senior.")



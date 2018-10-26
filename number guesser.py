secret = 5
guess = int(raw_input("Guess the number brother:"))
if secret == guess:
    print("Grat")
elif secret < guess:
    print("Kisebb")
else:
    print("Nagyobb")
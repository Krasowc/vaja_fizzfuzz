stevilo = input("vnesi stevilo od 1 do 100:")
stevilo = int(stevilo)

for x in range(1, stevilo):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzfuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("fuzz")
    else:
        print(x)

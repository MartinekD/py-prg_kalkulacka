# program dělá jednoduchou kalkulačku

# tato funkce sečte dvě čísla
def soucet(x, y):
    return x + y

# tato funkce vynásobí dvě čísla
def soucin(x, y):
    return x * y    

# tato funkce odečte dvě čísla
def minus(x, y):
    return x - y        

# tato funkce vydeli dvě čísla
def deleno(x, y):
    return x / y            

print("Vyber operaci.")
print("1.Součet")
print("2.Součin")
print("3.Rozdíl")
print("4.Děleno")    

while True:
    # napiš operaci
    choice = input("Vyber volbu(1/2/3/4): ")

     # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Napiš první číslo: "))
        num2 = float(input("Napiš druhé číslo: "))

        if choice == '1':
            print(num1, "+", num2, "=", soucet(num1, num2))

        elif choice == '2':
            print(num1, "*", num2, "=", soucin(num1, num2))

        elif choice == '3':
            print(num1, "-", num2, "=", minus(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", deleno(num1, num2))    

    else:
        print("Spatny vstup")    

    # check if user wants another calculation
    # break the while loop if answer is no
    next_calculation = input("Ukoncit kalkulacku? (ano/ne): ")
    if next_calculation == "ano":
        break    
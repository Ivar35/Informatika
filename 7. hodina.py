def solve(a, b, c):
    D = (b*b)-(4*a*c)
    x1 = (-b+D**0.5)/(2*a)
    x2 = (-b-D**0.5)/(2*a)
    print(x1)
    print(x2)

# a = int( input("Tell me three numbers, I will count a quadratic equation with them. ") )
# b = int(input("Great, now the second number. "))
# c = int(input("Fine. Now the last number. "))


# zadani_uloh = [
#     [2, -3, 7],
#     [1, 1, -2],
#     # tady muze byt nekonecno uloh
# ]

# for zadani in zadani_uloh:
#     solve(zadani[0], zadani[1], zadani[2])

# for pocet in range(5):
#opakovani = 0
#opakovani += 1
#while opakovani < 5:
while True:
    a = int( input("Three numbers to count a quadratic equation with. ") )
    b = int(input("Second number. "))
    c = int(input("Third number. "))
    solve(a,b,c)

 


print("ahoj")


solve(a, b, c)
solve(b, b, b)
solve(a, b, c)


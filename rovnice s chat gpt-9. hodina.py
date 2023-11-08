def solve(a, b, c):
    if a == 0:
        if b != 0:
            x = -c / b
            print(x)
        else:
            if c == 0:
                print("Rovnice má nekonečně mnoho řešení.")
            else:
                print("Rovnice nemá žádné řešení.")
    else:
        D = (b*b) - (4*a*c)
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        print(x1)
        print(x2)
while True:
    a = int( input("Three numbers to count a quadratic equation with. ") )
    b = int(input("Second number. "))
    c = int(input("Third number. "))
    solve(a,b,c)
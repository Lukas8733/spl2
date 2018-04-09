z = input ("Wie viele Haltestationen gibt es?")
k = 0

for p in range(0,int(z)):
    u = input("Wie viele Leute steigen ein?")
    q = input("Wie viele Leute steigen aus?")
    k = k +int(u)
    k = k -int(q)
    print("Es sind", k,"Leute im Bus")
    if(k>60):
        print("Es sind zu viele Leute im Bus!")
        r = k-60
        print("Es müssen", r,"Leute austeigen")
    if(k<0):
        print("Es sind zu wenig Leute im Bus!")
        t = 0-k
        u = input("Wie viele Leute steigen ein?")
        q = input("Wie viele Leute steigen aus?")
        k = k +int(u)
        k = k -int(q)
        print("Es sind", k,"Leute im Bus")

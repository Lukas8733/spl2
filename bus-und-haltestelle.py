z = input ("Wie viele Haltestationen gibt es?")
k = 0

for p in range(0,int(z)):
    u = input("Wie viele Leute steigen ein?")
    q = input("Wie viele Leute steigen aus?")
    k = k +int(u)
    k = k -int(q)

print("Es sind noch ", k,"Leute im Bus")

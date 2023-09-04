# 1 uzdevums
a = int(input("pirmais skaitlis "))
b = int(input("otrais skaitlis "))
print(a,"+",b,"=",int(a+b))
print(a,"-",b,"=",int(a-b))
print(a,"/",b,"=",int(a/b))
print(a,"*",b,"=",int(a*b))

# 2 uzdevums

inchi = int(input("ievadi inchus "))
m = inchi * 0.0254
print(inchi, "inchi ir ", m, " metri")

# 3 uzdevums

baze = int(input("ievadi bazi "))
augstums = int(input("ievadi augstumu "))
laukums = 1/2*baze*augstums
print("trijstura augstums ir ",laukums )

# 4 uzdevums

x = int(input("ievadi x:"))
y = int(input("ievadi y:"))
if x > y:
    print(2)
elif x < y:
    print(3)
else:
    print(1)

# 5 uzdevums

x = 0
while x < 10:
    x = x+1
    print(x)

# 6 uzdevums

def produkti():
    produktu_saraksts = ['piens','maize','olas']
    for i in produktu_saraksts:
        print(i)

produkti()

# 7 uzdevums

def a(teksts):
    if len(teksts) % 2 == 0:
        print(teksts.upper())
    elif len(teksts) % 1 == 0:
        print(teksts.lower())

a('piens')
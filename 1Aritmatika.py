X = 10
Y = 5
#  +
hasil = X + Y
print(X, "+", Y, "=", hasil)

# -

hasil = X - Y
print(X, "-", Y, "=", hasil)

# / 

hasil = X / Y
print(X, "/", Y, "=", hasil)

#  X
hasil = X * Y
print(X, "X", Y, "=", hasil)

# Eksponen 
hasil = X ** Y
print(X, "**", Y, "=", hasil)

# Modulus
hasil = X % Y
print(X, "%", Y, "=", hasil)

# Flow Division
hasil = X // Y
print(X, "//", Y, "=", hasil)

print("=====PRIORITAS OPERASI=====")
# prioritas operasi
#(), eksponen, perkalian, pertambahan

D = 5
C = 2
E = 8
hasil = (D + C) * E
print(D, "+", C, "*", E, "=", hasil)

hasil = D + (C - E) * C / D 
print(D, "+", C, "-", E, "X", C, "/", D, "=", hasil)
usia = 31

# == sama dengan
# > lebih dari
# < kurang dari
# != tidak sama dengan
# >= lebih dari sama dengan 
# <= kurang dari sama dengan

if usia == 0 :
    print("Belum lahir")
elif usia >= 0 and usia <= 3:
    print("Balita")
elif usia >= 3 and usia <= 10:
    print("Anak TK")
elif usia >= 10 and usia <= 15:
    print('Remaja')
elif usia >= 15 and usia <= 20:
    print("Dewasa awal")
elif usia >= 20 and usia <= 30:
    print('Dewasa akhir')
elif usia >=30 and usia <= 50:
    print("Fosil")
else:
    print("pengecualian")
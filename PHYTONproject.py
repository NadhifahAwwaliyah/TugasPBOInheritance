print ("=== BANGUN DATAR ===")

def persegi():
    print("\nMencari Luas dan Keliling Persegi")
    s = float(input("s = "))
    luas = s * s
    keliling = 4 * s
    print("luas persegi = ", luas, "cm2")
    print("keliling persegi = ", keliling, "cm")

def segitiga():
    print("\nMencari Luas dan Keliling Segitiga")
    a = float(input("a = "))
    t = float(input("t = "))
    s1 = float(input("s 1 = "))
    s2 = float(input("s 2 = "))
    luas = a * t
    keliling = a + s1 + s2
    print("luas segitiga = ", luas, "cm2")
    print("keliling segitiga = ", keliling, "cm")

def lingkaran():
    print("\nMencari Luas dan Keliling Lingkaran")
    r = float(input("r = "))
    luas = 22/7 * r * r
    keliling = 2 * 22/7 * r
    print("luas lingkaran = ", luas, "cm2")
    print("keliling lingkaran = ", keliling, "cm")

choice = int(input("\nMenu : \n1. Persegi \n2. Segitiga \n3. Lingkaran \nPilih salah satu  (1-3) = "))
if choice == 1:
    persegi()
elif choice == 2:
    segitiga()
elif choice == 3:
    lingkaran()

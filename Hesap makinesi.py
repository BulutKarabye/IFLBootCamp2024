devam = 'e'
while devam == 'e':
    try:
        sayi1 = int(input("İlk sayıyı/tabanı giriniz: "))
        sayi2 = int(input("İkinci sayıyı/üssü giriniz:"))
        x = "İşlemler:"
        print(x,"\n","-" * len(x), sep="")
        print("1. Toplama","2. Çıkarma","3. Çarpma","4. Bölme","5. Üs Alma", sep="\n")
        iş = input("İşlemi birden beşe kadar olan rakamlarla belirtiniz: ")
        if iş == "1":
            print(f"%d + %d = %d"%(sayi1, sayi2, sayi1+sayi2))
        elif iş == "2":
            print(f"%d - %d = %d"%(sayi1, sayi2, sayi1-sayi2))
        elif iş == "3":
            print(f"%d x %d = %d"%(sayi1, sayi2, sayi1*sayi2))
        elif iş == "4":
            print(f"%d : %d = %.2f"%(sayi1, sayi2, sayi1/sayi2))
        elif iş == "5":
            print(f"%d ^ %d = %d"%(sayi1, sayi2, sayi1**sayi2))
        else:
            print("Hatalı giriş yaptınız")
        devam = input("Başka işlem gerçekleştirmek için e, bitirmek için herhangi bir şey yazınız: ")      
    except(ValueError):
        print("Hesap makineleri işlemleri için sayılar kullanırlar.")
print("biti:)")
        

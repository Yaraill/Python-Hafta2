kelime = "hamburger"
puan = 10
tahmin_hakki = 5
isim = input("Lütfen isminizi giriniz: ")
print(f"Merhaba {isim}, kelime tahmin oyununa hoş geldiniz!")

for hak in range(tahmin_hakki):
    kullanici = input("Kelime tahmininizi giriniz: ").lower()
    if kullanici == kelime:
        print("Tebrikler, doğru tahmin ettiniz!")
        break
    else:
        puan -= 2
        print("Yanlış tahmin, tekrar deneyin!")
        if hak == 0:
            print("Kelimenin uzunluğu:", len(kelime))
        elif hak == 1:
            print("Kelimenin ilk harfi:", kelime[0])
        elif hak == 2:
            print("Kelimenin son harfi:", kelime[-1])
        elif hak == 3:
            print("Kelimenin ikinci harfi:", kelime[1])
        if hak == tahmin_hakki - 1:
            print("Üzgünüz, doğru cevap:", kelime)
        else:
            print("Kalan tahmin hakkınız:", tahmin_hakki - hak - 1)
print("Oyun bitti! Toplam puanınız:", puan)


with open("kelime_liderlik_tablosu.txt", "a", encoding="utf-8") as f:
    f.write(f"{isim}: {puan}\n")

print("\n--- Liderlik Tablosu ---")
with open("kelime_liderlik_tablosu.txt", "r", encoding="utf-8") as f:
    print(f.read())
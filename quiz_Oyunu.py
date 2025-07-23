sorular = {
    "soru1": "Python programlama dili ismini nerden almıştır?",
    "cevap1": "müzik grubundan",
    "soru2": "C# dahil olmak üzere birçok programlama dilinde kullanılan bir veri yapısı nedir?",
    "cevap2": "Dizi",
    "soru3": "CD Projekt RED tarafından geliştirilen ve 2015 yılında yayınlanan rol yapma oyunun adı nedir?",
    "cevap3": "Witcher 3",
    "soru4" : "Unreal Engine oyun motorunun geliştiricisi kimdir?",
    "cevap4": "Epic Games",
    "soru5" : "Unity oyun motorunun dili nedir?",
    "cevap5": "C#",
}

puan = 0
isim = input("Lütfen isminizi giriniz: ")
print(f"Merhaba {isim}, oyunumuza hoş geldiniz!")

for i in range(1, 6):
    cevap = input(sorular[f"soru{i}"] + " ").strip()
    if cevap.lower() == sorular[f"cevap{i}"].lower():
        print("Doğru cevap!")
        puan += 5

    else:
        print(f"Yanlış cevap! Doğru cevap: {sorular[f'cevap{i}']}")

print(f"{isim}, Toplam puanınız: {puan}")

with open("quiz_liderlik_tablosu", "a", encoding="utf-8") as f:
    f.write(f"{isim}: {puan}\n")

print("\n--- Liderlik Tablosu ---")
with open("quiz_liderlik_tablosu.txt", "r", encoding="utf-8") as f:
    print(f.read())
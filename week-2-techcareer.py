def sayi_analizi(sayi):
    # İşaret kontrolü
    if sayi > 0:
        durum = "Pozitif"
    elif sayi < 0:
        durum = "Negatif"
    else:
        durum = "Sıfır"

    # Tek/çift kontrolü
    if sayi == 0:
        sonuc = "Sıfır"
    elif sayi % 2 == 0:
        sonuc = f"{durum} Çift"
    else:
        sonuc = f"{durum} Tek"

    return sonuc

# Fonksiyonu kullanma
sayi = int(input("Bir sayı giriniz: "))
print(sayi_analizi(sayi))


def harf_frekansi(kelime):
    harf_sayilari = {}
    for harf in kelime:
        if harf in harf_sayilari:
            harf_sayilari[harf] += 1
        else:
            harf_sayilari[harf] = 1
    return harf_sayilari

# Fonksiyonu kullanma
kelime = input("Bir kelime giriniz: ")
sonuc = harf_frekansi(kelime)
print(sonuc)

def sifre_kontrol(sifre):
    uzunluk = len(sifre) >= 8
    buyuk_harf = any(char.isupper() for char in sifre)
    rakam = any(char.isdigit() for char in sifre)

    if uzunluk and buyuk_harf and rakam:
        return "Şifre geçerli ✅"
    else:
        mesaj = "Şifre geçersiz ❌\n"
        if not uzunluk:
            mesaj += "- En az 8 karakter olmalı\n"
        if not buyuk_harf:
            mesaj += "- En az 1 büyük harf içermeli\n"
        if not rakam:
            mesaj += "- En az 1 rakam içermeli\n"
        return mesaj

# Fonksiyonu kullanma
sifre = input("Bir şifre giriniz: ")
print(sifre_kontrol(sifre))


def ortalama_ustu_liste(sayilar):
    ortalama = sum(sayilar) / len(sayilar)
    buyukler = [sayi for sayi in sayilar if sayi > ortalama]
    return ortalama, buyukler

# Fonksiyonu kullanma
sayilar = [12, 4, 9, 25, 30, 7, 18]
ortalama, buyukler = ortalama_ustu_liste(sayilar)

print("Ortalama:", ortalama)
print("Ortalamadan büyük sayılar:", buyukler)


def ucgen_deseni(satir_sayisi):
    for i in range(1, satir_sayisi + 1):
        print("*" * i)

# Fonksiyonu kullanma
ucgen_deseni(5)


def toplam_ortalama():
    toplam = 0
    adet = 0

    while True:
        sayi = int(input("Bir sayı giriniz (Çıkmak için 0): "))
        if sayi == 0:
            break
        toplam += sayi
        adet += 1

    if adet > 0:
        ortalama = toplam / adet
        return toplam, ortalama
    else:
        return None, None

# Fonksiyonu kullanma
toplam, ortalama = toplam_ortalama()

if toplam is not None:
    print("Toplam:", toplam)
    print("Ortalama:", ortalama)
else:
    print("Hiç sayı girilmedi.")


def palindrom_kontrol(kelime):
    if kelime == kelime[::-1]:
        return "Palindrom ✅"
    else:
        return "Palindrom değil ❌"

# Fonksiyonu kullanma
kelime = input("Bir kelime giriniz: ")
print(palindrom_kontrol(kelime))


def kare_listesi():
    liste = [sayi**2 for sayi in range(1, 101) if sayi % 3 == 0 and sayi % 5 == 0]
    return liste

# Fonksiyonu çağırma
sonuc = kare_listesi()
print("Hem 3'e hem 5'e bölünen sayıların kareleri:", sonuc)

def kare_listesi(baslangic=1, bitis=100):
    liste = [sayi**2 for sayi in range(baslangic, bitis + 1) if sayi % 3 == 0 and sayi % 5 == 0]
    return liste

# Fonksiyonu kullanma
sonuc = kare_listesi()
print(sonuc)

def cumle_duzenle(cumle):
    # Cümleyi kelimelerine ayır
    kelimeler = cumle.split()
    # Her kelimenin ilk harfini büyüt
    kelimeler = [kelime.capitalize() for kelime in kelimeler]
    # Tekrar stringe çevir
    return " ".join(kelimeler)

# Fonksiyonu kullanma
cumle = input("Bir cümle giriniz: ")
print(cumle_duzenle(cumle))

def film_yorumlari():
    # Kullanıcıdan yorumları al
    yorumlar = []
    for i in range(5):  # 5 kez yorum alacağız
        yorum = input(f"{i+1}. film yorumunu giriniz: ")
        yorumlar.append(yorum)
    
    # Her yorumun uzunluğu
    uzunluklar = [len(y) for y in yorumlar]
    
    # "iyi" kelimesini içeren yorum sayısı
    iyi_sayisi = sum("iyi" in y.lower() for y in yorumlar)
    
    # En uzun ve en kısa yorum
    en_uzun = max(yorumlar, key=len)
    en_kisa = min(yorumlar, key=len)
    
    # Ortalama uzunluk
    ortalama = sum(uzunluklar) / len(yorumlar)
    
    # Sonuçları yazdır
    print("\n--- Yorum Analizi ---")
    print("Yorumlar:", yorumlar)
    print("Yorum uzunlukları:", uzunluklar)
    print(f'"iyi" geçen yorum sayısı: {iyi_sayisi}')
    print("En uzun yorum:", en_uzun)
    print("En kısa yorum:", en_kisa)
    print("Ortalama uzunluk:", ortalama)


# Fonksiyonu çalıştır
film_yorumlari()

# 11 Kitap Satış Analizi

kitaplar = [
    {"isim": "Veri Bilimi 101", "yazar": "Ali", "tur": "Bilim", "satis": 1200, "yil": 2021},
    {"isim": "Python ile Yapay Zeka", "yazar": "Ayşe", "tur": "Bilim", "satis": 950, "yil": 2020},
    {"isim": "İstatistik Temelleri", "yazar": "Ali", "tur": "Akademik", "satis": 700, "yil": 2019},
    {"isim": "Makine Öğrenmesi", "yazar": "Can", "tur": "Bilim", "satis": 1800, "yil": 2022},
    {"isim": "Veri Görselleştirme", "yazar": "Deniz", "tur": "Sanat", "satis": 400, "yil": 2018},
    {"isim": "Matematiksel Modelleme", "yazar": "Ali", "tur": "Akademik", "satis": 1500, "yil": 2021},
    {"isim": "Bilgi Toplumu", "yazar": "Ayşe", "tur": "Sosyal", "satis": 600, "yil": 2022}
]

def en_cok_satanlari_bul(kitap_listesi):
    """
    Verilen kitap listesindeki en çok satan kitabı döndürür.
    Eğer aynı satış rakamına sahip birden fazla kitap varsa, hepsini döndürür.
    """
    if not kitap_listesi:
        return []
    
    # En yüksek satış miktarını bulma
    en_yuksek_satis = max(kitap_listesi, key=lambda x: x["satis"])["satis"]
    
    # Satış miktarı en yüksek olan tüm kitapları filtreleme
    en_cok_satanlar = list(filter(lambda x: x["satis"] == en_yuksek_satis, kitap_listesi))
    
    return en_cok_satanlar

def yazar_satislarini_hesapla(kitap_listesi):
    """
    Her yazarın toplam satışını hesaplayıp bir sözlük olarak döndürür.
    """
    yazar_satis_sozluk = {}
    
    for kitap in kitap_listesi:
        yazar = kitap["yazar"]
        satis = kitap["satis"]
        
        # Eğer yazar sözlükte yoksa, yeni bir anahtar oluştur ve satışı ekle
        # Varsa, mevcut satışı güncelle
        yazar_satis_sozluk[yazar] = yazar_satis_sozluk.get(yazar, 0) + satis
        
    return yazar_satis_sozluk

# Fonksiyonları kullanarak sonuçları yazdırma
en_cok_satan_kitaplar = en_cok_satanlari_bul(kitaplar)
print("En Çok Satan Kitap(lar):")
for kitap in en_cok_satan_kitaplar:
    print(f"- {kitap['isim']} ({kitap['yazar']}): {kitap['satis']} adet")

print("\n" + "="*40 + "\n")

yazar_toplam_satislar = yazar_satislarini_hesapla(kitaplar)
print("Her Yazarın Toplam Satışı:")
for yazar, satis in yazar_toplam_satislar.items():
    print(f"- {yazar}: {satis} adet")

# 12 Kitap Türleri ve Popüler Kitaplar

    kitaplar = [
    {"isim": "Veri Bilimi 101", "yazar": "Ali", "tur": "Bilim", "satis": 1200, "yil": 2021},
    {"isim": "Python ile Yapay Zeka", "yazar": "Ayşe", "tur": "Bilim", "satis": 950, "yil": 2020},
    {"isim": "İstatistik Temelleri", "yazar": "Ali", "tur": "Akademik", "satis": 700, "yil": 2019},
    {"isim": "Makine Öğrenmesi", "yazar": "Can", "tur": "Bilim", "satis": 1800, "yil": 2022},
    {"isim": "Veri Görselleştirme", "yazar": "Deniz", "tur": "Sanat", "satis": 400, "yil": 2018},
    {"isim": "Matematiksel Modelleme", "yazar": "Ali", "tur": "Akademik", "satis": 1500, "yil": 2021},
    {"isim": "Bilgi Toplumu", "yazar": "Ayşe", "tur": "Sosyal", "satis": 600, "yil": 2022}
]

def turleri_bul(kitap_listesi):
    """
    Kitap listesindeki tüm benzersiz türleri bir küme olarak döndürür.
    """
    turler = set()
    for kitap in kitap_listesi:
        turler.add(kitap["tur"])
    return turler

def bin_den_fazla_satanlari_listele(kitap_listesi):
    """
    Satış adedi 1000'den fazla olan kitapların isimlerini bir liste olarak döndürür.
    """
    populer_kitaplar = []
    for kitap in kitap_listesi:
        if kitap["satis"] > 1000:
            populer_kitaplar.append(kitap["isim"])
    return populer_kitaplar

# Fonksiyonları kullanarak sonuçları yazdırma
benzersiz_turler = turleri_bul(kitaplar)
print("Tüm Kitap Türleri (Benzersiz):")
print(benzersiz_turler)

print("\n" + "="*40 + "\n")

en_cok_satanlar = bin_den_fazla_satanlari_listele(kitaplar)
print("1000'den Fazla Satan Kitapların İsimleri:")
print(en_cok_satanlar)


# 13 Lambda Fonksiyonları ile Veri İşleme
# 1. filter ile 2020'den sonra çıkan kitapları süzün
# Lambda fonksiyonu, bir kitabın yıl değerinin 2020'den büyük olup olmadığını kontrol eder.

yeni_kitaplar = list(filter(lambda kitap: kitap["yil"] > 2020, kitaplar))
print("2020'den sonra çıkan kitaplar:")
print([kitap["isim"] for kitap in yeni_kitaplar]) # Sadece isimleri yazdır

print("\n" + "-"*40 + "\n")

# 2. map ile tüm satış adetlerini %10 artırılmış şekilde yeni bir listeye aktarın
# Lambda fonksiyonu, her kitabın satış değerini alır ve %10 artırır.
yeni_satislar = list(map(lambda kitap: int(kitap["satis"] * 1.10), kitaplar))
print("Tüm kitapların %10 artırılmış yeni satış adetleri:")
print(yeni_satislar)

print("\n" + "-"*40 + "\n")

# 3. sorted + lambda ile kitapları satış miktarına göre azalan şekilde sıralayın
# Lambda fonksiyonu, sıralama kriteri olarak her kitabın satış değerini kullanır.
# reverse=True parametresi azalan (büyükten küçüğe) sıralama yapar.
satis_sirali_kitaplar = sorted(kitaplar, key=lambda kitap: kitap["satis"], reverse=True)
print("Kitaplar satış miktarına göre azalan sırada:")
for kitap in satis_sirali_kitaplar:
    print(f"- {kitap['isim']}: {kitap['satis']} adet")

    #14 Temel İstatistiksel Hesaplamalar

import statistics
from collections import Counter

kitaplar = [
    {"isim": "Veri Bilimi 101", "yazar": "Ali", "tur": "Bilim", "satis": 1200, "yil": 2021},
    {"isim": "Python ile Yapay Zeka", "yazar": "Ayşe", "tur": "Bilim", "satis": 950, "yil": 2020},
    {"isim": "İstatistik Temelleri", "yazar": "Ali", "tur": "Akademik", "satis": 700, "yil": 2019},
    {"isim": "Makine Öğrenmesi", "yazar": "Can", "tur": "Bilim", "satis": 1800, "yil": 2022},
    {"isim": "Veri Görselleştirme", "yazar": "Deniz", "tur": "Sanat", "satis": 400, "yil": 2018},
    {"isim": "Matematiksel Modelleme", "yazar": "Ali", "tur": "Akademik", "satis": 1500, "yil": 2021},
    {"isim": "Bilgi Toplumu", "yazar": "Ayşe", "tur": "Sosyal", "satis": 600, "yil": 2022}
]

def ortalama_satis_hesapla(kitap_listesi):
    """Tüm kitapların ortalama satış adedini hesaplar."""
    toplam_satis = sum(kitap["satis"] for kitap in kitap_listesi)
    kitap_sayisi = len(kitap_listesi)
    return toplam_satis / kitap_sayisi if kitap_sayisi > 0 else 0

def en_cok_satan_turu_bul(kitap_listesi):
    """En çok satış yapan kitap türünü bulur."""
    tur_satis_sozluk = {}
    for kitap in kitap_listesi:
        tur = kitap["tur"]
        satis = kitap["satis"]
        tur_satis_sozluk[tur] = tur_satis_sozluk.get(tur, 0) + satis
    
    # En yüksek toplam satışa sahip türü bulma
    if tur_satis_sozluk:
        en_cok_satan_tur = max(tur_satis_sozluk, key=tur_satis_sozluk.get)
        return en_cok_satan_tur
    return None

def satislarin_standart_sapmasini_hesapla(kitap_listesi):
    """statistics modülünü kullanarak satış adedi standart sapmasını hesaplar."""
    satis_listesi = [kitap["satis"] for kitap in kitap_listesi]
    return statistics.stdev(satis_listesi)

# Sonuç yazdırma
ortalama_satis = ortalama_satis_hesapla(kitaplar)
print(f"Ortalama satış adedi: {ortalama_satis:.2f}")

en_cok_satan_tur = en_cok_satan_turu_bul(kitaplar)
print(f"En çok satış yapan tür: {en_cok_satan_tur}")

standart_sapma = satislarin_standart_sapmasini_hesapla(kitaplar)
print(f"Satışların standart sapması: {standart_sapma:.2f}")

#15 Train/Test Simülasyonu

import random

kitaplar = [
    {"isim": "Veri Bilimi 101", "yazar": "Ali", "tur": "Bilim", "satis": 1200, "yil": 2021},
    {"isim": "Python ile Yapay Zeka", "yazar": "Ayşe", "tur": "Bilim", "satis": 950, "yil": 2020},
    {"isim": "İstatistik Temelleri", "yazar": "Ali", "tur": "Akademik", "satis": 700, "yil": 2019},
    {"isim": "Makine Öğrenmesi", "yazar": "Can", "tur": "Bilim", "satis": 1800, "yil": 2022},
    {"isim": "Veri Görselleştirme", "yazar": "Deniz", "tur": "Sanat", "satis": 400, "yil": 2018},
    {"isim": "Matematiksel Modelleme", "yazar": "Ali", "tur": "Akademik", "satis": 1500, "yil": 2021},
    {"isim": "Bilgi Toplumu", "yazar": "Ayşe", "tur": "Sosyal", "satis": 600, "yil": 2022}
]

def veriyi_bol(kitap_listesi, train_orani=0.7):
    """
    Kitap listesini eğitim ve test setlerine böler.
    Varsayılan olarak %70 eğitim, %30 test oranı kullanılır.
    """
    random.shuffle(kitap_listesi)  # Listeyi karıştır
    bolum_noktasi = int(len(kitap_listesi) * train_orani)
    
    train_set = kitap_listesi[:bolum_noktasi]
    test_set = kitap_listesi[bolum_noktasi:]
    
    return train_set, test_set

def yazar_ortalama_satis_hesapla(kitap_listesi):
    """
    Her yazarın ortalama satışını hesaplar ve bir sözlük olarak döndürür.
    """
    yazar_satis_sozluk = {}
    yazar_kitap_sayisi = {}
    
    for kitap in kitap_listesi:
        yazar = kitap["yazar"]
        satis = kitap["satis"]
        
        yazar_satis_sozluk[yazar] = yazar_satis_sozluk.get(yazar, 0) + satis
        yazar_kitap_sayisi[yazar] = yazar_kitap_sayisi.get(yazar, 0) + 1
    
    # Ortalama satışları hesapla
    yazar_ortalama_satis = {yazar: yazar_satis_sozluk[yazar] / yazar_kitap_sayisi[yazar] 
                            for yazar in yazar_satis_sozluk}
    
    return yazar_ortalama_satis

def ortalamanın_uzerindeki_kitapları_bul(kitap_listesi, yazar_ortalama_satis):
    """
    Test setindeki kitaplardan, yazarlarının ortalama satışının üzerinde satanları döndürür.
    """
    populer_kitaplar = []
    
    for kitap in kitap_listesi:
        yazar = kitap["yazar"]
        satis = kitap["satis"]
        
        if satis > yazar_ortalama_satis.get(yazarlar, 0):
            populer_kitaplar.append(kitaplar)
    
    return populer_kitaplar
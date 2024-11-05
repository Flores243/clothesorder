# Kıyafet ve ekstra ürün fiyatları
fiyatlar = {
    "Pantolon": 1350,
    "Gömlek": 850,
    "Ayakkabı": 1500,
    "Tişört": 250,
    "Çorap": 150,
    "Mont": 850
}

def fiyat_hesabi(urunler):
    toplam = 0
    for urun in urunler:
        toplam += fiyatlar.get(urun, 0)
    return toplam

def siparis_al():
    # Ürün seçimi

    print("Ürünlerimiz:")
    print("1. Pantolon - 1350 TL")
    print("2. Gömlek - 850 TL")
    print("3. Ayakkabı - 1500 TL")
    
    secimler = []
    
    while True:
        secim = input("Lütfen almak istediğiniz ürünleri seçin (1-3) veya bitirmek için 'B' yazın: ")
        
        if secim == '1':
            secimler.append("Pantolon")
        elif secim == '2':
            secimler.append("Gömlek")
        elif secim == '3':
            secimler.append("Ayakkabı")
        elif secim.upper() == 'B':
            break
        else:
            print("Geçersiz seçim! Lütfen 1-3 arasında bir numara girin veya 'B' yazarak bitirin.")

    # İndirimli Ürün Seçimi
    print("\nİndirimli Ürünler:")
    print("1. Tişört - 250 TL")
    print("2. Çorap - 150 TL")
    print("3. Mont - 850 TL")
    
    while True:
        secim = input("Lütfen almak istediğiniz ekstra ürünü seçin (1-3) veya bitirmek için 'B' yazın: ")
        
        if secim == '1':
            secimler.append("Tişört")
        elif secim == '2':
            secimler.append("Çorap")
        elif secim == '3':
            secimler.append("Mont")
        elif secim.upper() == 'B':
            break
        else:
            print("Geçersiz seçim! Lütfen 1-3 arasında bir numara girin veya 'B' yazarak bitirin.")
    
    return secimler

def fatura(secimler):
    print("\nSipariş Özeti:")
    with open("siparis_ozeti.txt", "w", encoding="utf-8") as dosya:
        # Başlıklar
        dosya.write(f"{'Ürün':<15} {'Fiyat (TL)':<15}\n")
        dosya.write("-" * 30 + "\n")
        
        toplam_fiyat = fiyat_hesabi(secimler)
        
        for urun in secimler:
            urun_satiri = f"{urun.capitalize():<15} {fiyatlar[urun]:<15}\n"
            print(urun_satiri.strip())
            dosya.write(urun_satiri)
        
        toplam_fiyat_satiri = f"{'Toplam Fiyat:':<15} {toplam_fiyat:<15}\n"
        print(toplam_fiyat_satiri.strip())
        dosya.write("-" * 30 + "\n")
        dosya.write(toplam_fiyat_satiri)

# Ana fonksiyon
def main():
    print("Taşkın AVM'ye hoş geldiniz")
    secimler = siparis_al()
    fatura(secimler)
    print("Bizi tercih ettiğiniz için teşekkür eder, iyi günler dileriz!")

main()

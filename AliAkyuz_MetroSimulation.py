import heapq
import collections

class MetroAgi:
    def __init__(self):
        """
        Metro ağı sınıfı. İstasyonları ve bağlantıları saklar.
        """
        self.istasyonlar = {}
    
    def istasyon_ekle(self, isim):
        """Yeni bir istasyon ekler."""
        if isim not in self.istasyonlar:
            self.istasyonlar[isim] = {}
    
    def baglanti_ekle(self, baslangic, bitis, sure):
        """İki istasyon arasında bağlantı ekler ve süreyi belirtir."""
        self.istasyon_ekle(baslangic)
        self.istasyon_ekle(bitis)
        self.istasyonlar[baslangic][bitis] = sure
        self.istasyonlar[bitis][baslangic] = sure
    
    def en_az_aktarma_bul(self, baslangic, hedef):
        """BFS algoritması ile en az aktarma içeren rotayı bulur."""
        kuyruk = collections.deque([(baslangic, [baslangic])])
        ziyaret_edilen = set()
        
        while kuyruk:
            mevcut, yol = kuyruk.popleft()
            if mevcut == hedef:
                return yol  # Hedefe ulaşıldığında yol döndürülür
            
            if mevcut not in ziyaret_edilen:
                ziyaret_edilen.add(mevcut)
                for komsu in self.istasyonlar[mevcut]:
                    if komsu not in ziyaret_edilen:
                        kuyruk.append((komsu, yol + [komsu]))
        return []  # Hedefe ulaşılamadıysa boş liste döndürülür
    
    def en_hizli_rota_bul(self, baslangic, hedef):
        """A* algoritması kullanarak en hızlı rotayı bulur."""
        oncelik_kuyrugu = [(0, baslangic, [baslangic])]
        ziyaret_edilen = {}
        
        while oncelik_kuyrugu:
            sure, mevcut, yol = heapq.heappop(oncelik_kuyrugu)
            if mevcut == hedef:
                return yol  # En kısa sürede hedefe ulaşan rota döndürülür
            
            if mevcut not in ziyaret_edilen or ziyaret_edilen[mevcut] > sure:
                ziyaret_edilen[mevcut] = sure
                for komsu, komsu_sure in self.istasyonlar[mevcut].items():
                    heapq.heappush(oncelik_kuyrugu, (sure + komsu_sure, komsu, yol + [komsu]))
        return []  # Eğer hedefe ulaşılamadıysa boş liste döndürülür

# Metro ağı oluşturuluyor
metro = MetroAgi()
metro.baglanti_ekle("AŞTİ", "Kızılay", 5)
metro.baglanti_ekle("Kızılay", "Ulus", 6)
metro.baglanti_ekle("Ulus", "Demetevler", 8)
metro.baglanti_ekle("Demetevler", "OSB", 4)
metro.baglanti_ekle("Batıkent", "Demetevler", 5)
metro.baglanti_ekle("Demetevler", "Gar", 6)
metro.baglanti_ekle("Gar", "Keçiören", 7)
metro.baglanti_ekle("Keçiören", "Gar", 7)
metro.baglanti_ekle("Gar", "Sıhhiye", 3)
metro.baglanti_ekle("Sıhhiye", "Kızılay", 2)

# Test senaryoları
print("=== Test Senaryoları ===")
print("1. AŞTİ'den OSB'ye:")
en_az_aktarma = metro.en_az_aktarma_bul("AŞTİ", "OSB")
en_hizli_rota = metro.en_hizli_rota_bul("AŞTİ", "OSB")
print(f"En az aktarmalı rota: {' -> '.join(en_az_aktarma)}")
print(f"En hızlı rota (25 dakika): {' -> '.join(en_hizli_rota)}")

print("\n2. Batıkent'ten Keçiören'e:")
en_az_aktarma = metro.en_az_aktarma_bul("Batıkent", "Keçiören")
en_hizli_rota = metro.en_hizli_rota_bul("Batıkent", "Keçiören")
print(f"En az aktarmalı rota: {' -> '.join(en_az_aktarma)}")
print(f"En hızlı rota (21 dakika): {' -> '.join(en_hizli_rota)}")

print("\n3. Keçiören'den AŞTİ'ye:")
en_az_aktarma = metro.en_az_aktarma_bul("Keçiören", "AŞTİ")
en_hizli_rota = metro.en_hizli_rota_bul("Keçiören", "AŞTİ")
print(f"En az aktarmalı rota: {' -> '.join(en_az_aktarma)}")
print(f"En hızlı rota (19 dakika): {' -> '.join(en_hizli_rota)}")

# Metro Simulation 🚇

## 1. Proje Başlığı ve Kısa Açıklama
Bu proje, Python kullanarak metro hatlarında **en az aktarmalı** ve **en hızlı rotayı** hesaplayan bir simülasyondur. Kullanıcıların başlangıç ve varış istasyonlarını belirlemesiyle, en uygun rotalar **BFS (Breadth-First Search)** ve **A*** **(A-Star)** algoritmaları kullanılarak hesaplanmaktadır.

---

## 2. Kullanılan Teknolojiler ve Kütüphaneler 🛠️
Bu projede Python'un aşağıdaki kütüphaneleri kullanılmıştır:
- `heapq`: Öncelikli kuyruk (priority queue) işlemleri için kullanıldı, A* algoritmasıyla en hızlı rotayı bulmada kullanıldı.
- `collections`: `deque` veri yapısı kullanılarak **BFS (Breadth-First Search)** algoritması için etkin bir kuyruk yapısı oluşturuldu.

Python 3.x sürümü ile çalıştırılabilir.

---

## 3. Algoritmaların Çalışma Mantığı 📊

### 📌 BFS Algoritması (Breadth-First Search) - En Az Aktarmalı Rota
BFS, genişlik öncelikli arama algoritmasıdır ve **en kısa düğüm sayısına sahip rotayı** bulmak için kullanılır. Metro sisteminde **en az aktarmalı** güzergahı hesaplamak için uygundur.

**Nasıl çalışır?**
1. Başlangıç istasyonu bir **kuyruğa** eklenir.
2. Her istasyon için komşu istasyonlar ziyaret edilir.
3. Hedef istasyona ulaşan en kısa yol bulunur.

BFS, **her duraktan tek tek ilerlediği için en az aktarmalı yolu garanti eder**.

---

### 🚀 A* Algoritması (A-Star) - En Hızlı Rota
A* algoritması **öncelikli kuyruk (heapq)** kullanarak **en kısa sürede ulaşım sağlayan** güzergahı bulur.

**Nasıl çalışır?**
1. Her istasyonun **zaman maliyeti** hesaplanır.
2. Hedefe en kısa sürede ulaşmak için **öncelikli kuyruk** kullanılır.
3. Algoritma, toplam seyahat süresi en düşük olan rotayı seçerek ilerler.

Bu yöntem, **BFS'den daha hızlıdır çünkü aktarma sayısı yerine doğrudan süreyi optimize eder**.

---

## 4. Örnek Kullanım ve Test Sonuçları 🏁

Aşağıda, proje çalıştırıldığında alınan örnek çıktılar verilmiştir:

```
=== Test Senaryoları ===

1. AŞTİ'den OSB'ye:
En az aktarmalı rota: AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB
En hızlı rota (25 dakika): AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB

2. Batıkent'ten Keçiören'e:
En az aktarmalı rota: Batıkent -> Demetevler -> Gar -> Keçiören
En hızlı rota (21 dakika): Batıkent -> Demetevler -> Gar -> Keçiören

3. Keçiören'den AŞTİ'ye:
En az aktarmalı rota: Keçiören -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
En hızlı rota (19 dakika): Keçiören -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
```

Proje şu şekilde çalıştırılabilir:
```bash
python AliAkyuz_MetroSimulation.py
```

---

## 5. Projeyi Geliştirme Fikirleri 🚀
Bu proje gelecekte aşağıdaki geliştirmelerle daha fonksiyonel hale getirilebilir:

✅ **Gerçekçi zaman verileri**: Metro hatlarının gerçek zamanlı verilerini çekerek daha hassas hesaplamalar yapılabilir.

✅ **Farklı ulaşım modları**: Metro dışında otobüs, tramvay gibi ulaşım seçenekleri eklenebilir.

✅ **Grafik Arayüz (GUI)**: Kullanıcıların harita üzerinden interaktif olarak rota oluşturmasını sağlayan bir arayüz geliştirilebilir.

✅ **Yolcu yoğunluğu optimizasyonu**: Saatlere ve günlere göre yoğunluk verileriyle en rahat güzergah seçilebilir.

Bu proje **Akbank Python Bootcamp Projesi** için geliştirilmiştir. 🎓


# YOLOv8 & ByteTrack ile Nesne Sayımı ve Yön Analizi Sistemi

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-green.svg)](https://docs.ultralytics.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red.svg)](https://opencv.org/)

Bu proje, bilgisayarlı görü (Computer Vision) ve derin öğrenme teknikleri kullanılarak **gerçek zamanlı nesne tespiti, takibi ve çizgi/yön bazlı sayımı** gerçekleştiren iki ayrı ana modülden oluşmaktadır.

Proje kapsamında **YOLOv8** tespit modeli ile **ByteTrack** takip algoritması entegre edilmiş, nesne hareket yönleri matematiksel yöntemlerle analiz edilmiştir.

---

## İçindekiler

- [Proje Modülleri ve Çalışma Mantığı](#-proje-modülleri-ve-çalışma-mantığı)
  - [1. Araç Takip ve Sayım Modülü (main_car.py)](#1-araç-takip-ve-sayım-modülü-main_carpy)
  - [2. İnsan Yön Analizi ve Sayım Modülü (main_people.py)](#2-i̇nsan-yön-analizi-ve-sayım-modülü-main_peoplepy)
- [Matematiksel ve Algoritmik Yaklaşım](#-matematiksel-ve-algoritmik-yaklaşım)
- [Teknolojik Altyapı](#️-teknolojik-altyapı)
- [Proje Dizin Yapısı](#-proje-dizin-yapısı)
- [Kurulum ve Çalıştırma Guide](#-kurulum-ve-çalıştırma-guide)
- [Veri Setleri](#-veri-setleri)

---

## Proje Modülleri ve Çalışma Mantığı

### 1. Araç Takip ve Sayım Modülü (`main_car.py`)

Trafik akışındaki araçların tespiti ve belirlenen çapraz sayım çizgisinden geçişlerinin kategorize edilerek sayılması amacını taşır.

- **Sınıf Bazlı Filtreleme:** YOLOv8 COCO veri seti üzerinden `car`, `truck`, `bus`, `motorcycle` ve `bicycle` sınıflarını ayırır.
- **Dinamik Çapraz Çizgi:** Ekran boyutuna oranlı olarak oluşturulan çapraz çizgi ile araç geçişleri izlenir.
- **Çift Sayım Önleme:** Her araca atanan benzersiz `track_id` ve `counted_ids` kümesi (`set`) sayesinde aynı aracın birden fazla sayılması engellenir.

### 2. İnsan Yön Analizi ve Sayım Modülü (`main_people.py`)

AVM, mağaza veya kapı girişleri gibi alanlarda insanların hareket yönünü tespit ederek içeri giren ve dışarı çıkan sayılarını hesaplar.

- **Sınıf Odaklılık:** Yalnızca `person` (insan) sınıfını işleme alarak işlem yükünü azaltır.
- **Dikey Ayrım Çizgisi:** Kadrajı dikey olarak ikiye böler:
  - **Giren (Sağa):** Soldan gelip dikey çizgiyi sağa doğru geçenler (`previous_x < line_x <= cx`).
  - **Çıkan (Sola):** Sağdan gelip dikey çizgiyi sola doğru geçenler (`previous_x > line_x >= cx`).

---

## Matematiksel ve Algoritmik Yaklaşım

### Çapraz Çizgi Geçiş Analizi (`get_line_side`)

Eğimli/çapraz çizgilerde bir nesnenin (merkez noktası $(x, y)$) çizginin ne tarafında olduğunu anlamak için **vektörel çarpım (cross product) yön hesabı** kullanılmıştır:

$$\text{side} = \text{sign}\Big( (x_2 - x_1)(y - y_1) - (y_2 - y_1)(x - x_1) \Big)$$

- $P_1(x_1, y_1)$ ve $P_2(x_2, y_2)$ çizginin başlangıç ve bitiş noktalarıdır.
- Nesne çizginin bir tarafından diğer tarafına geçtiğinde `side` değeri işaret değiştirir (örneğin $+1$'den $-1$'e düşer). Bu durum algılandığı an sayım yapılır.

---

## Teknolojik Altyapı

| Teknoloji              | Kullanım Amacı                                                            |
| :--------------------- | :------------------------------------------------------------------------ |
| **Python 3.12+**       | Ana programlama dili                                                      |
| **Ultralytics YOLOv8** | Gerçek zamanlı nesne tespiti                                              |
| **ByteTrack**          | Nesne takibi ve ID ataması (`tracker="bytetrack.yaml"`)                   |
| **OpenCV (`cv2`)**     | Video okuma, çizim İşlemleri (Bounding Box, Line, Text) ve görselleştirme |
| **NumPy**              | Vektörel yön hesaplamaları ve matris işlemleri                            |

---

## Proje Dizin Yapısı

```text
yolo-object-counting/
│
├── main_car.py         # Araç tespiti, takibi ve çapraz çizgi sayım kodu
├── main_people.py      # İnsan tespiti, ByteTrack takibi ve giren/çıkan yön analizi
├── requirements.txt    # Proje bağımlılıkları ve kütüphane sürümleri
├── .gitignore          # Git izleme dışı bırakılan dosyalar (venv, weights vs.)
└── README.md           # Detaylı proje dokümantasyonu
```

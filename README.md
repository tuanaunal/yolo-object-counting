# YOLO & OpenCV ile Araç Sayma Projesi

Bu proje, bir video akışı üzerinden **YOLO** (You Only Look Once) nesne tespiti ve nesne takibi (tracking) algoritmalarını kullanarak belirli bir çizgiyi geçen araçları tespit edip saymak amacıyla geliştirilmiştir.

---

## Projenin Amacı

Video üzerindeki araçları (`car`, `truck`, `bus`) gerçek zamanlı veya önceden kaydedilmiş görüntüler üzerinden tespit etmek, hareketlerini takip etmek ve tanımlanan sayım çizgisini geçen araç sayısını kategorize ederek hesaplamaktır.

---

## Kullanılan Teknolojiler

- **Python 3.12+**
- **OpenCV (`cv2`):** Görüntü işleme ve çizgi/metin görselleştirme
- **Ultralytics (YOLOv8 / YOLOv11):** Nesne tespiti ve takip (tracking)
- **NumPy:** Matris ve veri işlemleri

---

## Proje Yapısı

yolo-object-counting/
├── main_car.py # Ana çalışma ve sayım kodu
├── .gitignore # Git tarafından izlenmeyecek dosyalar
└── README.md # Proje açıklama belgesi

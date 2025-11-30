# 🛡️ Ağ Güvenliği Araç Kiti (GTK GUI)

**Python + GTK3** tabanlı grafik arayüzle geliştirilmiş bu araç, **Kali Linux** üzerinde sık kullanılan siber güvenlik araçlarını tek bir panelden yönetmeyi sağlar.  
Terminalde uzun komutlar yazmadan, sadece **tek tıklamayla** tarama ve analiz işlemleri yapılabilir.

---

## 🚀 Özellikler

### 🔧 MAC Adresi Değiştirme
- Rastgele MAC adresi üretme  
- Interface seçimi (eth0, wlan0, vb.)

---

### 🕵️‍♂️ Bilgi Toplama Araçları
Aşağıdaki araçları tek menü altında sunar:
- Dmitry  
- TheHarvester  
- Netdiscover  
- Wafw00f  
- Dirb  
- Dnsenum  

---

### 🌐 Nmap Taramaları
- Servis & versiyon taraması  
- Script taraması  
- Ayrıntılı tarama (-A)  
- Tüm TCP port taraması  
- Tüm UDP port taraması  
- İşletim sistemi tespiti  

---

### 🛡️ Searchsploit – Zafiyet Arama
- Anahtar kelime ile exploit araması

---

### 🌍 Nikto Web Zafiyet Taraması
- Standart zafiyet analizi  
- SQL Injection odaklı test  
- XSS taraması  

---

### 🖼️ Exiftool – Görsel Analiz
- Fotoğraf meta verisi inceleme  

---

### 📰 WPScan – WordPress Güvenlik Analizi
- Genel site taraması  
- Eklenti ve tema tespiti  
- Eklenti & tema zafiyet taraması  

---

### 📝 Wordlist Oluşturma (Crunch)
- Min/max karakter seçimi  
- Karakter seti seçenekleri  
- Wordlist oluşturma  

---

### ⚡ Rustscan
- Hızlı port taraması  

---

### 📡 TCPDump
- Ağ trafiği dinleme  

---

### 🐳 Docker Entegrasyonu
- **OpenVAS** container başlatma  
- **Ollama (Llama3)** AI modelini çalıştırma  

---

## 📦 Bağımlılıklar

### 🔹 Python
```bash
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
pip install pyfiglet requests
```

---

### 🔹 Kali Linux Araçları
```bash
sudo apt install macchanger dmitry theharvester netdiscover \
wafw00f dirb dnsenum nmap exploitdb nikto exiftool wpscan crunch \
rustscan tcpdump docker.io
```

---

### 🔹 Ek Gereksinimler

Docker servisi:
```bash
sudo systemctl enable docker
sudo systemctl start docker
```

---

WPScan Ruby bağımlılıkları:
```bash
sudo apt install ruby ruby-dev
sudo gem install wpscan
```

---

🛠️ Kurulum

1. Depoyu klonlayın
```bash
git clone https://github.com/oznursm/securitytoolkit.git
```

---

2. Dizine girin
```bash
cd oznursm/securitytoolkit
```

---

3. Uygulamayı başlatın
```bash
python3 start.py
```

---

📁 Proje Dosya Yapısı
securitytoolkit/
├── start.py          # GTK arayüzü
├── functions.py      # Tüm araç fonksiyonları
└── README.md         # Proje açıklaması

---

🎮 Kullanım

Uygulama açıldığında aşağıdaki işlemleri tek tıkla yapabilirsiniz:

- MAC adresi değiştirme

- Bilgi toplama araçları

- Nmap taramaları

- Searchsploit

- Nikto taraması

- Exiftool ile analiz

- WPScan

- Rustscan

- TCPDump

- Docker OpenVAS

- Docker Ollama

⚠️ Yasal Uyarı

Bu uygulama yalnızca izin verilen sistemlerde kullanılmalıdır.
İzinsiz sızma testi yapmak yasa dışıdır ve suçtur.
Bu proje yalnızca eğitim, deneme, ve etik siber güvenlik amaçları için hazırlanmıştır.

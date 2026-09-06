# 🎫 แอพสแกนตัวเลขสลาก

แอพพลิเคชันสำหรับสแกนตัวเลข 13 หลักจากรูปภาพสลาก บันทึกลงฐานข้อมูล และส่งออกข้อมูล

## ✨ คุณสมบัติ

- ✅ สแกนตัวเลข 13 หลักจากรูปภาพ
- ✅ ใช้ OCR (Optical Character Recognition) อ่านตัวเลขอัตโนมัติ
- ✅ บันทึกข้อมูลลง SQLite Database
- ✅ ดูประวัติการสแกน
- ✅ ส่งออกข้อมูลเป็น CSV
- ✅ Web Interface สวยงามและใช้งานง่าย
- ✅ 100% ฟรี (Open Source)

## 🚀 วิธีติดตั้ง

### ข้อกำหนด
- Python 3.7 ขึ้นไป
- pip (Python Package Manager)

### ขั้นตอนการติดตั้ง

1. **Clone Repository**
```bash
git clone https://github.com/chaixx2020-sketch/lottery-number-scanner.git
cd lottery-number-scanner
```

2. **สร้าง Virtual Environment (ไม่บังคับ แต่แนะนำ)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# หรือ
venv\Scripts\activate  # Windows
```

3. **ติดตั้ง Dependencies**
```bash
pip install -r requirements.txt
```

4. **ติดตั้ง Tesseract OCR**

**Windows:**
- ดาวน์โหลด: https://github.com/UB-Mannheim/tesseract/wiki
- ติดตั้งตามปกติ

**Mac:**
```bash
brew install tesseract
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install tesseract-ocr
```

5. **รัน Application**
```bash
python app.py
```

6. **เปิดเบราว์เซอร์ไป:**
```
http://localhost:5000
```

## 📖 วิธีใช้

1. คลิก **"📸 สแกนรูป"** เพื่อไปยังหน้าสแกน
2. คลิกหรือลากรูปภาพสลากมาที่ตรงนั้น
3. รอการประมวลผล (ประมาณ 2-5 วินาที)
4. ดูผลลัพธ์ตัวเลข 13 หลัก
5. คลิก **"📋 ประวัติ"** เพื่อดูรายการที่สแกนทั้งหมด
6. คลิก **"💾 ส่งออก CSV"** เพื่อดาวน์โหลดข้อมูลทั้งหมด

## 📁 โครงสร้างไฟล์

```
lottery-number-scanner/
├── app.py                 # โค้ดหลัก (Flask backend)
├── templates/
│   └── index.html         # หน้า Web UI
├── requirements.txt       # ไลบรารีที่ต้องใช้
├── lottery_data.db        # Database (สร้างอัตโนมัติ)
└── README.md              # ไฟล์นี้
```

## 🛠️ เทคโนโลยีที่ใช้

- **Backend:** Flask (Python Web Framework)
- **OCR:** Tesseract + OpenCV
- **Database:** SQLite
- **Frontend:** HTML5 + Bootstrap 5 + JavaScript
- **Image Processing:** OpenCV, Pillow, NumPy

## 📊 Database Schema

```sql
CREATE TABLE lottery_numbers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT NOT NULL,
    scan_date TEXT NOT NULL,
    image_path TEXT
)
```

## 🔧 Troubleshooting

### ❌ "ModuleNotFoundError: No module named 'pytesseract'"
```bash
pip install pytesseract
```

### ❌ "TesseractNotFoundError"
Tesseract ยังไม่ติดตั้ง ดู **ขั้นตอนการติดตั้ง** ข้างบน

### ❌ "Port 5000 already in use"
```bash
python app.py --port 5001
```

### ❌ ตัวเลขอ่านไม่ถูกต้อง
- ลองถ่ายรูปที่มีแสงดี
- ต้องให้ตัวเลขชัดเจน ไม่เบลอ
- ขนาดตัวเลขควรใหญ่พอ

## 📝 License

MIT License - คุณสามารถใช้งานและแก้ไขได้อย่างอิสระ

## 🤝 Contributing

ยินดีรับ Pull Requests และ Issues

## 📧 ติดต่อ

GitHub: [@chaixx2020-sketch](https://github.com/chaixx2020-sketch)

---

**สร้างด้วย ❤️ โดย chaixx2020-sketch**

# 🎫 แอพสแกนตัวเลขสลาก - Google Colab
แอพ Google Colab สำหรับสแกนตัวเลข 13 หลักจากรูปภาพสลาก เก็บข้อมูลใน Google Drive

## ✨ คุณสมบัติ

- ✅ สแกนตัวเลข 13 หลักจากรูปภาพ
- ✅ ใช้ Tesseract OCR อ่านตัวเลขอัตโนมัติ
- ✅ บันทึกลง Google Drive (ฟรี 15GB)
- ✅ ดูประวัติการสแกน
- ✅ ส่งออกเป็น CSV
- ✅ ฟรี 100% ไม่ต้องเสียเงิน
- ✅ ใช้ได้ทั้งคอมและมือถือ

---

## 🚀 วิธีใช้ (3 ขั้นตอนง่าย ๆ)

### ✅ ขั้นตอนที่ 1: เปิด Google Colab

ไปที่ลิงก์นี้: **https://colab.research.google.com**

### ✅ ขั้นตอนที่ 2: อัปโหลด Notebook

**วิธี A - Import จาก GitHub (ง่ายสุด):**
1. ไปที่: https://colab.research.google.com
2. คลิก **File > Open notebook**
3. ไปที่ tab **GitHub**
4. ป้อน: `chaixx2020-sketch/lottery-number-scanner`
5. เลือก: `lottery_scanner_colab.ipynb`
6. คลิก **Open**

**วิธี B - Download และ Upload:**
1. ไป: https://github.com/chaixx2020-sketch/lottery-number-scanner
2. คลิก: `lottery_scanner_colab.ipynb`
3. คลิก: **Download** (ไอคอน Download ทางขวา)
4. ไปที่ Colab
5. คลิก **File > Upload notebook**
6. เลือกไฟล์ที่ download

### ✅ ขั้นตอนที่ 3: รัน Notebook

1. **รัน Cell 1-4 ติดตั้งไลบรารีและสร้าง Database**
   - กด Shift+Enter ทีละ Cell
   - รอประมาณ 1-2 นาที

2. **รัน Cell 5 อัปโหลดรูปภาพ**
   - จะขึ้น "Choose Files" 
   - เลือกรูปภาพสลากของคุณ

3. **รัน Cell 6 อ่านตัวเลข**
   - จะแสดงตัวเลข 13 หลักที่อ่านได้

4. **รัน Cell 7 บันทึกลง Google Drive**
   - ข้อมูลจะบันทึกไว้ใน: `Google Drive > Lottery_Scanner`

5. **รัน Cell 8 ดูประวัติ**
   - แสดงรายการทั้งหมดที่เคยสแกน

6. **รัน Cell 9 ส่งออก CSV**
   - ดาวน์โหลดไฟล์ Excel

---

## 📖 รายละเอียด Cell ต่าง ๆ

| Cell | ชื่อ | วัตถุประสงค์ |
|------|------|-----------|
| 1 | ติดตั้ง Libraries | ติดตั้ง Python libraries ที่ต้องใช้ |
| 2 | Mount Google Drive | เชื่อมต่อ Google Drive |
| 3 | สร้างโฟลเดอร์ | สร้างโฟลเดอร์เก็บข้อมูล |
| 4 | สร้าง Database | สร้างฐานข้อมูล SQLite |
| 5 | อัปโหลดรูป | อัปโหลดรูปภาพสลาก |
| 6 | อ่านตัวเลข | ใช้ OCR อ่านตัวเลข 13 หลัก |
| 7 | บันทึก | บันทึกลง Google Drive |
| 8 | ดูประวัติ | แสดงรายการทั้งหมด |
| 9 | ส่งออก CSV | ส่งออกเป็นไฟล์ Excel |
| 10 | ลบข้อมูล | ลบข้อมูลเก่า (ไม่บังคับ) |

---

## 🎯 ตัวอย่างการใช้

```
1. เปิด Google Colab
2. Import notebook จาก GitHub
3. เรียกใช้ Cell 1-4 (ติดตั้งครั้งแรก)
4. เรียกใช้ Cell 5-7 (สแกนรูปใหม่)
5. เรียกใช้ Cell 8 (ดูประวัติ)
6. เรียกใช้ Cell 9 (ส่งออก CSV)
```

---

## 📁 โครงสร้าง Google Drive

```
Google Drive
└── Lottery_Scanner/
    ├── lottery_data.db          (ฐานข้อมูล)
    └── lottery_data.csv         (ไฟล์ Excel)
```

---

## ⚠️ ข้อสำคัญ

1. **ต้องมี Google Account** - สมัครฟรีที่ https://accounts.google.com
2. **ต้องมี Google Drive** - ได้มากับ Google Account (15GB ฟรี)
3. **ต้องอนุญาติ Colab เข้า Drive** - จะขึ้นประมาณ Cell 2
4. **ใช้ได้ 12 ชั่วโมงติดต่อกัน** - ถ้านานกว่านั้น Colab จะหยุด

---

## 🔧 Troubleshooting

### ❌ "ModuleNotFoundError"
👉 รันเสร็จแล้ว ลองรันใหม่ โดยไม่ต้องรัน Cell 1 ซ้ำ

### ❌ "Permission denied"
👉 ยังไม่ได้อนุญาติ Colab เข้า Google Drive
👉 ตรวจสอบ Cell 2 ให้แน่ใจว่าอนุญาติแล้ว

### ❌ "File not found"
👉 ลืมตั้งชื่อโฟลเดอร์ผิด
👉 ลองรัน Cell 3 ใหม่

### ❌ ตัวเลขอ่านไม่ถูกต้อง
👉 ลองถ่ายรูปใหม่ที่มีแสงดี
👉 ต้องให้ตัวเลขชัดเจน ไม่เบลอ

---

## 📝 License

MIT License - ใช้งานได้อย่างอิสระ

---

## 🤝 ต้องการช่วยเหลือ?

- 📧 GitHub: [@chaixx2020-sketch](https://github.com/chaixx2020-sketch)
- 💬 เปิด Issue บน GitHub

---

**สร้างด้วย ❤️ โดย chaixx2020-sketch**

**👉 พร้อมใช้งาน! ไปที่ Google Colab เลยครับ 🚀**

from flask import Flask, render_template, request, jsonify
import cv2
import pytesseract
from PIL import Image
import sqlite3
import os
from datetime import datetime
import io
import numpy as np

app = Flask(__name__)

# Database setup
DATABASE = 'lottery_data.db'

def init_db():
    """สร้าง Database ถ้ายังไม่มี"""
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS lottery_numbers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                number TEXT NOT NULL,
                scan_date TEXT NOT NULL,
                image_path TEXT
            )
        ''')
        conn.commit()
        conn.close()

def save_lottery_number(number):
    """บันทึกตัวเลขลงฐานข้อมูล"""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    scan_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute('INSERT INTO lottery_numbers (number, scan_date) VALUES (?, ?)', 
              (number, scan_date))
    conn.commit()
    conn.close()

def extract_numbers_from_image(image_path):
    """อ่านตัวเลขจากรูปภาพ"""
    try:
        # อ่านรูปภาพ
        img = cv2.imread(image_path)
        if img is None:
            return None, "ไม่สามารถอ่านรูปภาพได้"
        
        # แปลงเป็นสีเทา
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # ปรับ contrast เพื่อให้ตัวอักษรชัดขึ้น
        gray = cv2.equalizeHist(gray)
        
        # Threshold เพื่อให้ได้รูปขาว-ดำชัดเจน
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        
        # ใช้ Tesseract อ่านตัวเลข
        text = pytesseract.image_to_string(thresh, config='--psm 6 digits')
        
        # กรองเฉพาะตัวเลข
        numbers_only = ''.join(c for c in text if c.isdigit())
        
        if len(numbers_only) == 13:
            return numbers_only, "สำเร็จ"
        else:
            return numbers_only, f"ตัวเลขไม่ครบ 13 หลัก (พบ {len(numbers_only)} หลัก)"
            
    except Exception as e:
        return None, f"เกิดข้อผิดพลาด: {str(e)}"

@app.route('/')
def index():
    """หน้าแรก"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    """อัปโหลดและสแกนรูปภาพ"""
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'message': 'ไม่มีไฟล์'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'success': False, 'message': 'ไม่มีไฟล์ที่เลือก'}), 400
        
        # บันทึกไฟล์ชั่วคราว
        temp_path = 'temp_image.jpg'
        file.save(temp_path)
        
        # อ่านตัวเลขจากรูป
        numbers, message = extract_numbers_from_image(temp_path)
        
        if numbers:
            # บันทึกลงฐานข้อมูล
            save_lottery_number(numbers)
            response = {
                'success': True,
                'number': numbers,
                'message': message
            }
        else:
            response = {
                'success': False,
                'message': message
            }
        
        # ลบไฟล์ชั่วคราว
        if os.path.exists(temp_path):
            os.remove(temp_path)
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'success': False, 'message': f'เกิดข้อผิดพลาด: {str(e)}'}), 500

@app.route('/history')
def history():
    """ดูประวัติการสแกน"""
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('SELECT * FROM lottery_numbers ORDER BY id DESC LIMIT 100')
        rows = c.fetchall()
        conn.close()
        
        history_data = [
            {
                'id': row[0],
                'number': row[1],
                'scan_date': row[2]
            }
            for row in rows
        ]
        
        return jsonify({'success': True, 'data': history_data})
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/export')
def export():
    """ส่งออกข้อมูลเป็น CSV"""
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('SELECT * FROM lottery_numbers ORDER BY scan_date DESC')
        rows = c.fetchall()
        conn.close()
        
        csv_content = "ลำดับ,ตัวเลข,วันที่สแกน\n"
        for row in rows:
            csv_content += f"{row[0]},{row[1]},{row[2]}\n"
        
        return jsonify({
            'success': True,
            'csv': csv_content,
            'filename': f'lottery_numbers_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        })
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)

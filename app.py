# -*- coding: utf-8 -*-
"""
Created on Wed May 17 02:07:13 2023

@author: Admin
"""

from flask import Flask, render_template, request

# Khởi tạo Flask app
app = Flask(__name__)

# Định nghĩa trang chủ
@app.route('/')
def home():
    return render_template('index.html')

# Xử lý yêu cầu chat
@app.route('/chat', methods=['POST'])
def chat():
    # Nhận câu hỏi từ người dùng
    user_question = request.form['question']

    # Thực hiện xử lý câu hỏi và trả về câu trả lời từ chatbot
    bot_answer = "day la cau tra loi tu chatbot."

    # Trả về câu trả lời cho người dùng
    return {'answer': bot_answer}

# Chạy ứng dụng Flask
if __name__ == '__main__':
    app.run(debug=True)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
import json
import requests
import classAttendance
import subject
import semester
import teacher
import student
import dbConfig

app = Flask(__name__)
#app.config['TESTING'] = True


@app.route('/')
def index():
    return 'This is chatbot server!.'


@app.route('/bot', methods=['POST'])
def bot():
    # ข้อความที่ต้องการส่งกลับ
    replyQueue = list()

    # ข้อความที่ได้รับมา
    msg_in_json = request.get_json()
    msg_in_string = json.dumps(msg_in_json)
    print(msg_in_json)
    # Token สำหรับตอบกลับ (จำเป็นต้องใช้ในการตอบกลับ)
    replyToken = msg_in_json["events"][0]['replyToken']

    # ส่วนนี้ดึงข้อมูลพื้นฐานออกมาจาก json (เผื่อ)
    userID = msg_in_json["events"][0]['source']['userId']
    msgType = msg_in_json["events"][0]['message']['type']
    # ตรวจสอบว่า ที่ส่งเข้ามาเป็น text รึป่าว (อาจเป็น รูป, location อะไรแบบนี้ได้ครับ)
    # แต่ก็สามารถประมวลผลข้อมูลประเภทอื่นได้นะครับ
    # เช่น ถ้าส่งมาเป็น location ทำการดึง lat long ออกมาทำบางอย่าง เป็นต้น
    if msgType != 'text':
        reply(replyToken, ['Only text is allowed.'])
        return 'OK', 200

    # ตรงนี้ต้องแน่ใจว่า msgType เป็นประเภท text ถึงเรียกได้ครับ
    # lower เพื่อให้เป็นตัวพิมพ์เล็ก strip เพื่อนำช่องว่างหัวท้ายออก ครับ
    text = msg_in_json["events"][0]['message']['text'].lower().strip()
    text = text.split()
    print(text)
    if(len(text) > 3):
        replyQueue.append(
            'โปรดกรอกข้อความในรูปแบบ <subject_code_name> <semester_name> <student_code_name> \nเช่น cos1101 2/62 6005004780')
        reply(replyToken, replyQueue[:5])
        return 'OK', 200

    if(len(text) == 1):
        if(text[0] == 'วิชา' or text[0] == 'วิชาเปิดสอน' or text[0] == 'วิชาสอน' or text[0] == 'subject'):
            replyQueue.append(subject.select_subject_info())
            reply(replyToken, replyQueue[:5])
            return 'OK', 200

        if(text[0] == 'ภาค' or text[0] == 'ภาคการศึกษา' or text[0] == 'semester'):
            replyQueue.append(semester.select_semester_info())
            reply(replyToken, replyQueue[:5])
            return 'OK', 200

        if(text[0] == 'อาจารย์' or text[0] == 'teacher' or text[0] == 'อาจารย' or text[0] == 'อาจาร' or text[0] == 'อาจาน' or text[0] == 'ครู' or text[0] == 'ผู้สอน'):
            replyQueue.append(teacher.select_teacher_info())
            reply(replyToken, replyQueue[:5])
            return 'OK', 200

        if(text[0] == 'นักศึกษา' or text[0] == 'student' or text[0] == 'นักเรียน' or text[0] == 'students' or text[0] == 'เด็ก' or text[0] == 'boy' or text[0] == 'boys'):
            replyQueue.append(student.select_student_info_all())
            reply(replyToken, replyQueue[:5])
            return 'OK', 200

        if(len(text[0]) == 10 and text[0].isdigit()):
            replyQueue.append(student.select_student_info(text[0]))
            reply(replyToken, replyQueue[:5])
            return 'OK', 200
    # ตัวอย่างการทำให้ bot ถาม-ตอบได้ แบบ exact match
    # response_dict = {'สวัสดี':'สวัสดีครับ'}
    # if text in response_dict:
    #     replyQueue.append(reponse_dict[text])
    # else:
    #     replyQueue.append('ไม่รู้ว่าจะตอบอะไรดี TT')

    # ตัวอย่างการทำให้ bot ถาม-ตอบได้ แบบ non-exact match
    # โดยที่มี method ชื่อ find_closest_sentence ที่ใช้การเปรียบเทียบประโยค
    # เพื่อค้นหาประโยคที่ใกล้เคียงที่สุด อาจใช้เรื่องของ word embedding มาใช้งานได้ครับ
    # simple sentence embeddings --> https://openreview.net/pdf?id=SyK00v5xx
    # response_dict = {'สวัสดี':'สวัสดีครับ'}
    # closest = find_closest_sentence(response_dict, text)
    # replyQueue.append(reponse_dict[closest])

    # ตอบข้อความ "นี่คือรูปแบบข้อความที่รับส่ง" กลับไป
    # replyQueue.append('นี่คือรูปแบบข้อความที่รับส่งครับ')

    # ทดลอง Echo ข้อความกลับไปในรูปแบบที่ส่งไปมา (แบบ json)
    if(len(text) == 2):
        replyQueue.append(classAttendance.select_class_attendace_info_all(text[0], text[1]))
        reply(replyToken, replyQueue[:5])
        return 'OK', 200

    if(len(text) == 3):
        replyQueue.append(classAttendance.select_class_attendace_info(text[0], text[1], text[2]))
        reply(replyToken, replyQueue[:5])
        return 'OK', 200


def reply(replyToken, textList):
    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ
    LINE_API = 'https://api.line.me/v2/bot/message/reply'  # reply
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': dbConfig.lineConfig['LINE_API_KEY_BOT']
    }
    print(textList)
    msgs = []
    for text in textList:
        msgs.append({
            "type": "text",
            "text": text
        })
    data = json.dumps({
        "replyToken": replyToken,
        "messages": msgs
    })
    x = requests.post(LINE_API, headers=headers, data=data)
    print(x)
    return


if __name__ == '__main__':
    #context = ('C:/xampp/apache/conf/ssl.crt', 'C:/xampp/apache/conf/ssl.key')
    #app.run(host='127.0.0.1', port=5000, ssl_context=context, threaded=True, debug=True)
    #app.run(host='localhost', port=8080, ssl_context=context, threaded=True, debug=True)
    app.run()

from flask import Flask, request
import json
import requests

# ตรง YOURSECRETKEY ต้องนำมาใส่เองครับจะกล่าวถึงในขั้นตอนต่อๆ ไป
global LINE_API_KEY
# ห้ามลบคำว่า Bearer ออกนะครับเมื่อนำ access token มาใส่
LINE_API_KEY = 'Bearer /mnxywYk+P8dLSFrPpEcZinPM5xmqGvzWGDLnOLhcmz3Iv4ymldO/P75wa3yPZCv2y4MNEMa/m9kHbaTHtKyxNJsoXIhWinqT8l94ePO7vflwsGHPiF0VzH8OSSL/4DRNH4zNVYWuvGDHAjyqPBuewdB04t89/1O/w1cDnyilFU='

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is chatbot server.'


#@app.route('/bot', methods=['POST'])
def bot(msg_in_string):
    # ข้อความที่ต้องการส่งกลับ
    replyQueue = list()

    # ข้อความที่ได้รับมา
    # msg_in_json = request.get_json()
    # msg_in_string = json.dumps(msg_in_json)

    # Token สำหรับตอบกลับ (จำเป็นต้องใช้ในการตอบกลับ)
    # replyToken = msg_in_json["events"][0]['replyToken']

    # # ส่วนนี้ดึงข้อมูลพื้นฐานออกมาจาก json (เผื่อ)
    # userID = msg_in_json["events"][0]['source']['userId']
    # msgType = msg_in_json["events"][0]['message']['type']

    # ตรวจสอบว่า ที่ส่งเข้ามาเป็น text รึป่าว (อาจเป็น รูป, location อะไรแบบนี้ได้ครับ)
    # แต่ก็สามารถประมวลผลข้อมูลประเภทอื่นได้นะครับ
    # เช่น ถ้าส่งมาเป็น location ทำการดึง lat long ออกมาทำบางอย่าง เป็นต้น
    # if msgType != 'text':
    #     reply(replyToken, ['Only text is allowed.'])
    #     return 'OK', 200

    # ตรงนี้ต้องแน่ใจว่า msgType เป็นประเภท text ถึงเรียกได้ครับ
    # lower เพื่อให้เป็นตัวพิมพ์เล็ก strip เพื่อนำช่องว่างหัวท้ายออก ครับ
    # text = msg_in_json["events"][0]['message']['text'].lower().strip()
    # replyQueue.append(msg_in_string)
    # ตัวอย่างการทำให้ bot ถาม-ตอบได้ แบบ exact match
    text = msg_in_string
    response_dict = {'สวัสดี': 'สวัสดีครับผม'}
    if text in response_dict:
        replyQueue.append(response_dict[text])
        reply(replyQueue[:2])
        return 'OK', 200
    response_dict = {'ราคา': '4,000 บาท ค่ะ'} 
    if text in response_dict:
        replyQueue.append(response_dict[text])
        reply(replyQueue[:2])
        return 'OK', 200
    response_dict = {'กี่วันได้': 'ประมาณ 1 เดือน ค่ะ'} 
    if text in response_dict:
        replyQueue.append(response_dict[text])
        reply(replyQueue[:2])
        return 'OK', 200
    replyQueue.append('หนูไม่เข้าใจค่ะ')
    reply(replyQueue[:2])
    return 'OK', 200
    # ตัวอย่างการทำให้ bot ถาม-ตอบได้ แบบ non-exact match
    # โดยที่มี method ชื่อ find_closest_sentence ที่ใช้การเปรียบเทียบประโยค
    # เพื่อค้นหาประโยคที่ใกล้เคียงที่สุด อาจใช้เรื่องของ word embedding มาใช้งานได้ครับ
    # simple sentence embeddings --> https://openreview.net/pdf?id=SyK00v5xx
    # response_dict = {'สวัสดี':'สวัสดีครับ'}
    # closest = find_closest_sentence(response_dict, text)
    # replyQueue.append(reponse_dict[closest])
   
    # ตอบข้อความ "นี่คือรูปแบบข้อความที่รับส่ง" กลับไป

    
    # ทดลอง Echo ข้อความกลับไปในรูปแบบที่ส่งไปมา (แบบ json)

   
 
def reply(textList):
    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ
    # LINE_API = 'https://api.line.me/v2/bot/message/reply'
    # headers = {
    #     'Content-Type': 'application/json; charset=UTF-8',
    #     'Authorization': LINE_API_KEY
    # }
    msgs = textList
    # for text in textList:
    #     msgs.append({
    #         "type":"text",
    #         "text":text
    #     })
    # data = json.dumps({
    #     "replyToken":replyToken,
    #     "messages":msgs
    # })
    #requests.post(LINE_API, headers=headers, data=data)
    print(msgs)
    return

# if __name__ == '__main__':
#     app.run(debug=True)
msg_in_string=input('input:')
bot(msg_in_string)
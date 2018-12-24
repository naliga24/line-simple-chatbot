#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
# import cv
# import sys
# from PIL import Image
# import base64
# #import cStringIO
# import PIL.Image
# import io


def select_class_attendace_info(subjectCodeName, semesterName,studentCodeName):
    mydb = mysql.connector.connect(
        host="us-cdbr-iron-east-01.cleardb.net",
        user="b2742dd9273833",
        passwd="99f7887d5ff6a81",
        database="heroku_766db354cb15187",
    )
    cursor = mydb.cursor()
    txt = u'ชื่อวิชา '+subjectCodeName+u'\nภาค'+semesterName+'\n'
    sql = "SELECT a.TEACHER_FIRST_NAME , a.TEACHER_LAST_NAME"
    sql += " FROM teacher_info a , subject_info b"
    sql += " WHERE a.TEACHER_NO = b.TEACHER_NO"
    sql += " AND b.SUBJECT_CODE_NAME = '"+subjectCodeName+"'"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        txt += u'อาจารย์ '+row[0]+' '+row[1]+'\n'
    #print('g'+txt)

    sql = "SELECT STUDENT_FIRST_NAME , STUDENT_LAST_NAME"
    sql += " FROM student_info"
    sql += " WHERE STUDENT_CODE_NAME = '"+studentCodeName+"'"
    cursor.execute(sql)
    result = cursor.fetchall()
    txt +=u'รหัส '+studentCodeName
    for row in result:
        txt += u'\nนักศึกษา '+row[0]+' '+row[1]+'\n'
    #print('g'+txt)

    sql = "SELECT DATE_FORMAT( a.CLASS_ATTENDANCE_DATE,'%Y-%m-%d' ) , a.CLASS_ATTENDANCE_TIME , b.CONFIRM_STATUS_DESCRIPTION"
    sql += " FROM class_attendance_info a , confirm_status_info b"
    sql += " WHERE a.CONFIRM_STATUS_NO = b.CONFIRM_STATUS_NO"
    sql += " AND a.STUDENT_NO = (SELECT STUDENT_NO FROM student_info WHERE STUDENT_CODE_NAME = '"+studentCodeName+"')"
    sql += " AND a.SUBJECT_NO = (SELECT SUBJECT_NO FROM subject_info WHERE SUBJECT_CODE_NAME = '"+subjectCodeName+"')"
    sql += " AND a.SEMESTER_NO = (SELECT SEMESTER_NO from semester_info WHERE SEMESTER_NAME = '"+semesterName+"')"
    sql += " ORDER BY a.CLASS_ATTENDANCE_DATE ASC , a.CLASS_ATTENDANCE_TIME ASC"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        txt += row[0]+'  '+str(row[1])+' ('+row[2]+'),\n'
    print('g'+txt)
    mydb.close()
    return txt


if __name__ == "__main__":
    select_class_attendace_info('cos1102','2/67','6005004783')

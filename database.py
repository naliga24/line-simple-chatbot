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


def select_class_attendace_info(subjectName, studentId):
    mydb = mysql.connector.connect(
        host="us-cdbr-iron-east-01.cleardb.net",
        user="b2742dd9273833",
        passwd="99f7887d5ff6a81",
        database="heroku_766db354cb15187",
    )
    cursor = mydb.cursor()
    txt = ''
    sql = "SELECT a.teacher_first_name , a.teacher_last_name"
    sql += " FROM teacher_info a , subject_info b"
    sql += " WHERE a.teacher_id = b.teacher_id"
    sql += " AND b.subject_name = '"+subjectName+"'"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        txt += u'อาจารย์ '+row[0]+' '+row[1]+'\n'
    print('g'+txt)

    sql = "SELECT student_first_name , student_last_name"
    sql += " FROM student_info"
    sql += " WHERE student_id = '"+studentId+"'"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        txt += row[0]+' '+row[1]+'\n'
    print('g'+txt)

    sql = "SELECT DATE_FORMAT( class_attendance_date,'%Y-%m-%d' ) , TIME_FORMAT( class_attendance_time,'%h:%m:%s' )"
    sql += " FROM class_attendance_info"
    sql += " WHERE student_id = '"+studentId+"'"
    sql += " AND subject_id = (SELECT subject_id FROM subject_info WHERE subject_name = '"+subjectName+"')"
    sql += " AND (SELECT semester_id FROM semester_info ORDER BY semester_id DESC LIMIT 1)"
    sql += " ORDER BY class_attendance_date ASC , class_attendance_time ASC"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        txt += row[0]+' , '+row[1]+'\n'
    print('g'+txt)
    mydb.close()
    return txt


if __name__ == "__main__":
    select_class_attendace_info('cos1103','6005004780')

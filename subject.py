#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector


def dbConfig():
    return mysql.connector.connect(
        host="us-cdbr-iron-east-01.cleardb.net",
        user="b2742dd9273833",
        passwd="99f7887d5ff6a81",
        database="heroku_766db354cb15187",
    )

def select_subject_info():
    mydb = dbConfig()
    cursor = mydb.cursor()
    sql = "SELECT a.SUBJECT_CODE_NAME , a.SUBJECT_NAME , a.SUBJECT_DESCRIPTION , b.USE_STATUS_DESCRIPTION , c.TEACHER_FIRST_NAME , c.TEACHER_LAST_NAME"
    sql += " FROM subject_info a , use_status_info b , teacher_info c"
    sql += " WHERE a.SUBJECT_STATUS = b.USE_STATUS_NO"
    sql += " AND a.TEACHER_NO = c.TEACHER_NO"
    sql += " ORDER BY SUBJECT_CODE_NAME ASC"
    cursor.execute(sql)
    result = cursor.fetchall()
    txt = ''
    for row in result:
        txt += row[0]+' '+row[1]+' '+row[2]+' ('+row[3]+') '+row[4]+' '+row[5]+',\n'
    mydb.close()
    print(txt)
    return txt

if __name__ == "__main__":
    select_subject_info()

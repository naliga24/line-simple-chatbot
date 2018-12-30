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

def select_semester_info():
    mydb = dbConfig()
    cursor = mydb.cursor()
    sql = "SELECT a.SEMESTER_NAME , b.SEMESTER_STATUS_DESCRIPTION"
    sql += " FROM semester_info a, semester_status_info b"
    sql += " WHERE a.SEMESTER_STATUS_NO = b.SEMESTER_STATUS_NO"
    sql += " ORDER BY a.SEMESTER_NO DESC"
    cursor.execute(sql)
    result = cursor.fetchall()
    txt = ''
    for row in result:
        txt += row[0]+' ('+row[1]+'),\n'
    mydb.close()
    print(txt)
    return txt

if __name__ == "__main__":
    select_semester_info()

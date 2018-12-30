#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dbConfig

def select_subject_info():
    mydb = dbConfig.config()
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

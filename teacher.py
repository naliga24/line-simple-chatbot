#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dbConfig

def select_teacher_info():
    mydb = dbConfig.config()
    cursor = mydb.cursor()
    sql = "SELECT a.TEACHER_FIRST_NAME , a.TEACHER_LAST_NAME , a.TEACHER_CLASS_COUNT , b.USE_STATUS_DESCRIPTION"
    sql += " FROM teacher_info a, use_status_info b"
    sql += " WHERE a.TEACHER_STATUS = b.USE_STATUS_NO"
    sql += " ORDER BY a.TEACHER_FIRST_NAME ASC , a.TEACHER_LAST_NAME ASC"
    cursor.execute(sql)
    result = cursor.fetchall()
    txt = ''
    for row in result:
        txt += row[0]+' '+row[1]+u' (สอน '+str(row[2])+u' วิชา) '+row[3]+u',\n'
    mydb.close()
    print('g'+txt)
    return txt

if __name__ == "__main__":
    select_teacher_info()


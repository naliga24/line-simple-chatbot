#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dbConfig

def select_student_info(studentCodeName):
    mydb = dbConfig.config()
    cursor = mydb.cursor()
    sql = "SELECT a.STUDENT_FIRST_NAME , a.STUDENT_LAST_NAME , b.USE_STATUS_DESCRIPTION , a.STUDENT_IMAGE"
    sql += " FROM student_info a , use_status_info b"
    sql += " WHERE a.STUDENT_STATUS = b.USE_STATUS_NO"
    sql += " AND  a.STUDENT_CODE_NAME = '"+studentCodeName+"'"
    cursor.execute(sql)
    result = cursor.fetchall()
    txt = ''
    for row in result:
        txt += row[0]+' '+row[1]+' '+row[2]+' '+row[3]+'\n'
    mydb.close()
    print('.'+txt)
    return txt

if __name__ == "__main__":
    select_student_info('6005004780')

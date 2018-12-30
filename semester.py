#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dbConfig

def select_semester_info():
    mydb = dbConfig.config()
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

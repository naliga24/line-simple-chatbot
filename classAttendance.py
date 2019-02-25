#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dbConfig

def select_class_attendace_info(subjectCodeName, semesterName,studentCodeName):
    mydb = dbConfig.config()
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

    sql = "SELECT DATE_FORMAT( a.CLASS_ATTENDANCE_DATE,'%Y-%m-%d' ) , a.CLASS_ATTENDANCE_TIME , b.CONFIRM_STATUS_DESCRIPTION , a.CLASS_ATTENDANCE_IMAGE"
    sql += " FROM class_attendance_info a , confirm_status_info b"
    sql += " WHERE a.CONFIRM_STATUS_NO = b.CONFIRM_STATUS_NO"
    sql += " AND a.STUDENT_NO = (SELECT STUDENT_NO FROM student_info WHERE STUDENT_CODE_NAME = '"+studentCodeName+"')"
    sql += " AND a.SUBJECT_NO = (SELECT SUBJECT_NO FROM subject_info WHERE SUBJECT_CODE_NAME = '"+subjectCodeName+"')"
    sql += " AND a.SEMESTER_NO = (SELECT SEMESTER_NO from semester_info WHERE SEMESTER_NAME = '"+semesterName+"')"
    sql += " ORDER BY a.CLASS_ATTENDANCE_DATE ASC , a.CLASS_ATTENDANCE_TIME ASC"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        txt += row[0]+'  '+str(row[1])+' ('+row[2]+') '+row[3]+' ,\n'
    print('g'+txt)
    mydb.close()
    return txt

def select_class_attendace_info_all(subjectCodeName, semesterName):
    mydb = dbConfig.config()
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

    sql = "SELECT c.STUDENT_FIRST_NAME , c.STUDENT_LAST_NAME , c.STUDENT_CODE_NAME,"
    sql += " DATE_FORMAT( a.CLASS_ATTENDANCE_DATE,'%Y-%m-%d' ) , a.CLASS_ATTENDANCE_TIME,"
    sql += " b.CONFIRM_STATUS_DESCRIPTION , a.CLASS_ATTENDANCE_IMAGE"
    sql += " FROM class_attendance_info a , confirm_status_info b , student_info c"
    sql += " WHERE a.CONFIRM_STATUS_NO = b.CONFIRM_STATUS_NO"
    sql += " AND a.STUDENT_NO = c.STUDENT_NO"
    sql += " AND a.SUBJECT_NO = (SELECT SUBJECT_NO FROM subject_info WHERE SUBJECT_CODE_NAME = '"+subjectCodeName+"')"
    sql += " AND a.SEMESTER_NO = (SELECT SEMESTER_NO from semester_info WHERE SEMESTER_NAME = '"+semesterName+"')"
    sql += " ORDER BY a.CLASS_ATTENDANCE_DATE ASC , a.CLASS_ATTENDANCE_TIME ASC"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        txt += row[0]+' '+row[1]+' '+row[2]+' '+row[3]+'  '+str(row[4])+' ('+row[5]+') '+row[6]+' ,\n'
    print('g'+txt)
    mydb.close()
    return txt

if __name__ == "__main__":
    #select_class_attendace_info('cos1102','1/62','6005004780')
    select_class_attendace_info_all('cos1102','1/62')
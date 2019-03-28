import mysql.connector

def config():
    return mysql.connector.connect(
        host="us-cdbr-iron-east-01.cleardb.net",
        user="b2742dd9273833",
        passwd="99f7887d5ff6a81",
        database="heroku_766db354cb15187",
    )


lineConfig = {
    'LINE_API_KEY_BOT': 'Bearer Jw5n0d+Mur0QjhafGbXQmxIGTK7Dz4LHozZRnM4d26Smx058IABzvZ4ngLfpKQ2dSm6jggm6sMaVH8lR464NcBAudE9QLGKy+CrTgreZaLa+rq8coupkCc2FD6/nA1BlwbVaHvXgt7SHh92NZAeowAdB04t89/1O/w1cDnyilFU='
}

# def config():
#     return mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         passwd="root",
#         database="cos4105",
#     )

import mysql.connector

def config():
    return mysql.connector.connect(
        host="us-cdbr-iron-east-01.cleardb.net",
        user="b2742dd9273833",
        passwd="99f7887d5ff6a81",
        database="heroku_766db354cb15187",
    )


lineConfig = {
    'LINE_API_KEY_BOT': 'Bearer TWraVVwVss8PTboEcpRtXeclwUc7hIMvPxYCuFyWMl9fVAk3/KPFfM+vGvO15Bkz2y4MNEMa/m9kHbaTHtKyxNJsoXIhWinqT8l94ePO7vcTRPJJHL3zzWK9/6eYhKcQ3IECeIFWWn1kk+3Q3WbbiwdB04t89/1O/w1cDnyilFU='
}

# def config():
#     return mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         passwd="root",
#         database="cos4105",
#     )

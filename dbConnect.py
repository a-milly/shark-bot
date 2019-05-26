import os
import psycopg2


class dbConnect(object):
    
    def __init__(self, dbUrl):
        self.dbUrl = dbUrl

    def initConnection(self):
        conn = psycopg2.connect(self.dbUrl, sslmode='require')
        return conn

    def initCursor(self, connection):
        cur = connection.cursor()
        return cur
    
    def insertMessageRow(self, cursor, connection, row):
        print('=====inserting row=======')
        cursor.execute("INSERT INTO usermessages (server_id, channel_id, server, user_id, curr_username, message, joined, message_timestamp, message_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (row["server_id"], row["server_name"], row["channel"], row['user_id'], row["curr_username"], row["message"], row["user_join_time"], row["message_timestamp"], row['msg_id']))
        connection.commit()
        cursor.close()
        connection.close()

#os.environ['DATABASE_URL']


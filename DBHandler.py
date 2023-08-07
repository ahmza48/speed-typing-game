import pymysql
from player import Player
# from note import Note

class DBHandler:
    def __init__(self, host, user, password, dataBase, port):
        self.host = host
        self.password = password
        self.username = user
        self.dataBase = dataBase
        self.port = port

    def register_player(self, player):
        connection = None
        cursor = None
        connection = pymysql.connect(
            host=self.host, port=self.port, user=self.username, password=self.password, database=self.dataBase)
        cursor = connection.cursor()
        try:

            sql = "Select * from gamer where email=%s"
            args = (player.email)
            cursor.execute(sql, args)
            result=cursor.fetchall()
            if result:
                return False
            else:
                sql="Insert into gamer (`username`,`email`,`passwd`,`max_score`) Values (%s,%s,%s,%s)"
                arg=(player.username,player.email,player.password,player.maxscore)
                cursor.execute(sql,arg)
                connection.commit()
                return True
        except Exception as e:
            print(str(e))
            return False
        finally:
            cursor.close()
            connection.close()

    def verify_player(self,email,password):
        connection=None
        cursor=None
        connection = pymysql.connect(
            host=self.host, port=self.port, user=self.username, password=self.password, database=self.dataBase)
        
        cursor = connection.cursor()
        try:
            sql = "Select * from gamer where email=%s AND passwd=%s"
            args = (email,password)
            cursor.execute(sql, args)
            result = cursor.fetchall()
            print('in verify',result)
            if result:
                print(result)
                return result
            return False
        except Exception as e:
            print(str(e))
            return False
        finally:
            cursor.close()
            connection.close()

    def update_score(self,score,email,password):
        connection=None
        cursor=None
        connection = pymysql.connect(
            host=self.host, port=self.port, user=self.username, password=self.password, database=self.dataBase)
        
        cursor = connection.cursor()
        try:
            sql = "Update gamer set max_score=%s where email=%s AND passwd=%s"
            args = (score,email,password)
            cursor.execute(sql, args)
            connection.commit()
            return True
        except Exception as e:
            print(str(e))
            return False
        finally:
            cursor.close()
            connection.close()



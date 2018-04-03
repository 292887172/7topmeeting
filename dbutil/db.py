
from dbutil.db_helper import SQLHelper


class Sqlcaozuo():



    @staticmethod
    def user_fetch_one(user,pwd):
        ret = SQLHelper.fetch_one('Select name,id from user WHERE name=%s and pwd=%s', [user, pwd])
        return ret

    @staticmethod
    def time_fetch_all():
        ret = SQLHelper.fetch_all('Select id,datetime from time ', [])
        return ret

    @staticmethod
    def room_fetch_all():
        ret = SQLHelper.fetch_all('Select id,name from room ', [])
        return ret

    @staticmethod
    def add(rid,date,tid,uid):
        ret = SQLHelper.add('INSERT INTO reseve(rid, date, tid,uid) VALUES (%s, %s, %s,%s)',[rid,date,tid,uid])
        return ret


    @staticmethod
    def reseve_fetch_all(dt):
        ret = SQLHelper.fetch_all('Select rid,tid,name from reseve  INNER JOIN user ON reseve.uid=user.id WHERE reseve.date=%s', [dt])
        return ret


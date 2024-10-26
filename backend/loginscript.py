import sqlite3
import hashlib
import sys
import os

dbname = "user.db"


def init_db(): #server
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    q1 = "CREATE TABLE IF NOT EXISTS ware(id int auto increment, username text primary key, password text, name text);"
    cur.execute(q1)
    q1 = "CREATE TABLE IF NOT EXISTS client(id int auto increment, username text primary key, password text, name text);"
    cur.execute(q1)
    # cur.close()
    # q1 = "insert into ware values(0 , 'testclient','12345','client');"
    # cur.execute(q1)
    # q1 = "insert into client values(0 , 'testware','12345','ware');"
    # cur.execute(q1)
    cur.close()
    # create_client("testclient",'12345','client')
    # create_ware("testware",'12345','ware')
    print("SQL init compleated!")
    conn.commit()
    conn.close()

#email = name
#name = email


def create_ware(username:str,password:str,name:str):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    hpass = hashlib.md5(password.encode()).hexdigest()
    sql = f'insert into ware(username,password,name) values ("{username}","{hpass}","{name}");'
    try:
        cur.execute(sql)
        print(f"ware {username}::{password} successfully generated")
        return True
    except sqlite3.Error as error:
        print(f"SQL Error Occured:: {username} :: {error}")
        return False
    except Exception as e:
        print(f"PY Error Occured:: {username} :: {e}")
        return False
    finally:
        cur.close()
        conn.commit()
        conn.close()

def load_ware(username:str,password:str):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    uhpass = hashlib.md5(password.encode()).hexdigest()
    sql = f'select password from ware where username="{username}";'
    try:
        cur.execute(sql)
        shpass = cur.fetchall()
        #print(shpass)
        if shpass == []:
            print(f"ware ware {username} not found")
            return False
        elif uhpass == shpass[0][0]:
            print(f"ware {username} has correct password ")
            return True
        elif shpass == []:
            print(f"ware ware {username} not found")
            return False
        else:
            print(f"ware Incorrect password :: {username}")
            return False
    except sqlite3.Error as error:
        print(f"SQL Error occured :: {username} :: {error}")
        return False
    except Exception as e:
        print(f"PY Error Occured:: {username} :: {e}")
        return False
    finally:
        cur.close()
        conn.commit()
        conn.close()


def getname_ware(username:str):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    sql = f'select name from ware where username="{username}";'
    try:
        cur.execute(sql)
        shpass = cur.fetchall()
        #print(shpass)
        if shpass == []:
            print(f"ware ware {username} not found")
            return False
        if shpass:
            print(f"ware {username} has full name {shpass[0][0]}")
            return shpass[0][0]
        else:
            print(f"ware Incorrect password :: {username}")
            return False
    except sqlite3.Error as error:
        print(f"SQL Error occured :: {username} :: {error}")
        return False
    except Exception as e:
        print(f"PY Error Occured:: {username} :: {e}")
        return False
    finally:
        cur.close()
        conn.commit()
        conn.close()

def getid_ware(username:str):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    sql = f'select id from ware where username="{username}";'
    try:
        cur.execute(sql)
        shpass = cur.fetchall()
        #print(shpass)
        if shpass == []:
            print(f"ware ware {username} not found")
            return False
        if shpass:
            print(f"ware {username} has full id {shpass[0][0]}")
            return shpass[0][0]
        else:
            print(f"ware Incorrect password :: {username}")
            return False
    except sqlite3.Error as error:
        print(f"SQL Error occured :: {username} :: {error}")
        return False
    except Exception as e:
        print(f"PY Error Occured:: {username} :: {e}")
        return False
    finally:
        cur.close()
        conn.commit()
        conn.close()

def create_client(username:str,password:str,name:str):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    hpass = hashlib.md5(password.encode()).hexdigest()
    sql = f'insert into client(username,password,name) values ("{username}","{hpass}","{name}");'
    try:
        cur.execute(sql)
        # print(f"admin {username}::{password} successfully generated")
        return True
    except sqlite3.Error as error:
        print(f"SQL Error Occured:: {username} :: {error}")
        return False
    except Exception as e:
        print(f"PY Error Occured:: {username} :: {e}")
        return False
    finally:
        cur.close()
        conn.commit()
        conn.close()

def load_client(username:str,password:str):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    uhpass = hashlib.md5(password.encode()).hexdigest()
    sql = f'select password from client where username="{username}";'
    try:
        cur.execute(sql)
        shpass = cur.fetchall()
        #print(shpass)
        if shpass == []:
            print(f"USER client {username} not found")
            return False
        elif uhpass == shpass[0][0]:
            print(f"client {username} has correct password ")
            return True
        elif shpass == []:
            print(f"USER client {username} not found")
            return False
        else:
            print(f"client Incorrect password :: {username}")
            return False
    except sqlite3.Error as error:
        print(f"SQL Error occured :: {username} :: {error}")
        return False
    except Exception as e:
        print(f"PY Error Occured:: {username} :: {e}")
        return False
    finally:
        cur.close()
        conn.commit()
        conn.close()

def getname_client(username:str):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    sql = f'select name from client where username="{username}";'
    try:
        cur.execute(sql)
        shpass = cur.fetchall()
        print(shpass)
        if shpass == []:
            print(f"USER client {username} not found")
            return False
        if shpass:
            print(f"client {username} has correct name {shpass[0][0]}")
            return shpass[0][0]
        else:
            print(f"client Incorrect password :: {username}")
            return False
    except sqlite3.Error as error:
        print(f"SQL Error occured :: {username} :: {error}")
        return False
    except Exception as e:
        print(f"PY Error Occured:: {username} :: {e}")
        return False
    finally:
        cur.close()
        conn.commit()
        conn.close()

def getid_client(username:str):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    sql = f'select * from client where username="{username}";'
    try:
        cur.execute(sql)
        shpass = cur.fetchall()
        print(shpass)
        if shpass == []:
            print(f"USER client {username} not found")
            return False
        if shpass:
            print(f"client {username} has correct id {shpass[0][0]}")
            return shpass
        else:
            print(f"client Incorrect password :: {username}")
            return False
    except sqlite3.Error as error:
        print(f"SQL Error occured :: {username} :: {error}")
        return False
    except Exception as e:
        print(f"PY Error Occured:: {username} :: {e}")
        return False
    finally:
        cur.close()
        conn.commit()
        conn.close()

# init_db()
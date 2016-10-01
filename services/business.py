import mysql.connector


class business(object):

    def __init__(self, user, password, host, port, database):
        """"""
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

        try:        
            print('Trying to connect to database.')
            self.db_conn = mysql.connector.connect(user=self.user,
                password=self.password,
                host=self.host,
                database=self.database,
                port=self.port)
            print('Connected.')
            self.db_conn.close()
        except:
            print('Could not connect to database.')
        

if __name__ == '__main__':
    b = business('root', 'sugiff16', '127.0.0.1', 3300, 'business')
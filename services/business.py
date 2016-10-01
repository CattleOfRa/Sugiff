import base64
import mysql.connector
import hashlib


class business(object):

    def __init__(self, user, password, host, port, database):
        """Connect to business database."""
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

        config = {
            'user': str(self.user),
            'password': str(self.password),
            'host': self.host,
            'port': self.port,
            'database': self.database,
            'raise_on_warnings': True,
        }
        self.conn = None
        self.cursor = None
        
        try:
            self.conn = mysql.connector.connect(**config)
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as e:
            print(e)

    def close(self):
        """Close connection to business database."""
        self.conn.close()

    def encode_password(self, password):
        """Encode plain text password to MD5"""
        m = hashlib.md5()
        m.update(password.encode('utf-8'))
        return m.hexdigest()

    def create_business(self, name, password):
        """Creates a new business"""
        table = 'business'
        password = self.encode_password(password)
        self.insert(table, {"name": name, "password": password})
        return self.get_business_id(name, password)

    def get_business_id(self, name, password):
        """Get business id with business name and password"""
        query = "SELECT id FROM business WHERE name='{}' AND password='{}';".format(name, password)
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def create_product(self, name, cost, image, business_id):
        """Create a new product for a business"""
        table = 'product'
        image = self.image_to_blob('temp_images/product.jpg')

        self.insert(table, {"name": name, "cost": cost, "image": image})

        product_id = self.get_product_id()
        table = 'business_has_product'
        self.insert(table, {"business_id": business_id, "product_id": product_id})
        return self.get_business_products(business_id)

    def get_product_id(self):
        query = "SELECT LAST_INSERT_ID() as id FROM product;"
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def get_business_products(self, business_id):
        """Get all products from a business id"""
        query = "SELECT * FROM business_has_product WHERE business_id='{}';".format(business_id)
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def where(self, values):
        """Creates a WHERE claus"""
        return " AND ".join(["{}='{}'".format(list(values)[i], values[list(values)[i]]) for i in range(len(values))])
    
    def exists(self, tableName, values={}):
        """Check if values exist in table"""
        query = "SELECT EXISTS (SELECT 1 FROM service.user WHERE {});".format(self.where(values))
        self.cursor.execute(query)
        return bool(self.cursor.fetchone()[0])
        
    def auth(self, username, password):
        """Authenticates a user to the database"""
        return self.exists("user", {"username": username, "password": self.encrypt(password)})
    
    def fieldsFormatter(self, data):
        """Formats the fields of a query"""
        return ",".join(data.keys())
        
    def valuesFormatter(self, data):
        """Formats the values of a query"""
        return ",".join([ "'{}'".format(i) for i in data.values() ])
        
    def insert(self, tableName, values={}):
        """Inserts data to a table name"""
        try:
            query = "INSERT INTO {} ({}) VALUES ({})".format(tableName,
                self.fieldsFormatter(values),
                self.valuesFormatter(values))
            self.cursor.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)

    def image_to_blob(self, image_location):
        """Convert image to a blob to send to business database"""
        with open(image_location, 'rb') as f:
            image = f.read()
        return image

        
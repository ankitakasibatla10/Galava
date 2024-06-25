from abc import ABC, abstractmethod
import pymysql
from pymongo import MongoClient

class BaseDatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass
    
    @property
    def is_sql(self):
        pass

# MySQL Connection
class MySQLConnection(BaseDatabaseConnection):
    def __init__(self, name, user_name, password, server_name, port):
        self.name = name
        self.username = user_name
        self.password = password
        self.server_name = server_name
        self.port = port

    def connect(self):
        self.connection = pymysql.connect(host=self.server_name,
                                          user=self.username,
                                          password=self.password,
                                          port=self.port)
        print(f"Connected to MySQL database '{self.name}'.")

    def close(self):
        if self.connection:
            self.connection.close()

    def is_sql(self):
        return True


# MongoDB Connection
class MongoDBConnection(BaseDatabaseConnection):
    
    def __init__(self, name, uri):
        self.name = name
        self.uri = uri

    def connect(self):
        self.connection = MongoClient(self.uri)
        print(f"Connected to MongoDB database '{self.name}'.")
    
    def close(self):
        if self.connection:
            self.connection.close()
    
    def is_sql(self):
        return False

class DatabaseConnectionFactory(ABC):
    @abstractmethod
    def create_connection(self, config):
        pass

class MySQLConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self, config):
        return MySQLConnection(**config)

class MongoDBConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self, config):
        return MongoDBConnection(**config)

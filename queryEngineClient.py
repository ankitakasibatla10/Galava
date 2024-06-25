from QueryEngineInterface import *

def query_engine_factory(connection):
    if connection.is_sql():
        return SQLQueryEngine(connection.connection, connection.name) 
    else: 
        return MongoDBQueryEngine(connection.connection, connection.name)

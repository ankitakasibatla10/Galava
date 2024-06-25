import yaml
from DatabaseConnectionInterface import *

def create_database_connections(yaml_file_path):
    connections = []
    factories = {
        'SQLDatabases': MySQLConnectionFactory(),
        'NoSQLDatabases': MongoDBConnectionFactory()
    }
    with open(yaml_file_path, 'r') as file:
        config = yaml.safe_load(file)

    for db_type, factory in factories.items():
        for db_config in config.get(db_type, []):
            adjusted_config = {key.lower(): value for key, value in db_config.items()}
            
            try:
                connection = factory.create_connection(adjusted_config)
                connection.connect()
                connections.append(connection)
                print(f"Successfully connected to {db_type[:-1]}: {db_config.get('name')}")
            except Exception as e:
                print(f"Failed to connect to {db_type[:-1]}: {db_config.get('name')}. Error: {e}")

    return connections


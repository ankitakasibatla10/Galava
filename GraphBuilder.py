from neo4j import GraphDatabase

class KnowledgeGraphBuilder:
    def __init__(self, uri, auth):
        self.driver = GraphDatabase.driver(uri, auth=auth)

    def close(self):
        self.driver.close()

    def create_database_node(self, database_name):
 
        with self.driver.session() as session:
            session.write_transaction(self._create_and_return_database, database_name)

    def create_table_node(self, database_name, table_name):
        # This method creates a node for a table and links it to its database.
        with self.driver.session() as session:
            session.write_transaction(self._create_and_return_table, database_name, table_name)

    @staticmethod
    def _create_and_return_database(tx, database_name):
        # Cypher query to create a database node if it doesn't already exist.
        query = (
            "MERGE (d:Database {name: $database_name}) "
            "RETURN d"
        )
        result = tx.run(query, database_name=database_name)
        return result.single()[0]

    @staticmethod
    def _create_and_return_table(tx, database_name, table_name):
        # Cypher query to create a table node and a relationship to its database.
        query = (
            "MATCH (d:Database {name: $database_name}) "
            "MERGE (t:Table {name: $table_name}) "
            "MERGE (d)-[:CONTAINS]->(t) "
            "RETURN t"
        )
        result = tx.run(query, database_name=database_name, table_name=table_name)
        return result.single()[0]

from GraphBuilder import KnowledgeGraphBuilder
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()
graph_uri = os.getenv("NEO4J_URI") 
graph_auth = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))

print(graph_uri)
print(graph_auth)

def authenticateKnowledgeGraph():
    graph_builder = KnowledgeGraphBuilder(graph_uri, graph_auth)
    return graph_builder
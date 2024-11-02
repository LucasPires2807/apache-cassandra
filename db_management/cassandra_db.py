from cassandra.cluster import Cluster

from dotenv import load_dotenv
from os import getenv

load_dotenv()

class Cassandra:
    
    def __init__(self, contact_points: str=getenv('CONTAINER_ID'), port: int=9042):
        self.cluster = Cluster(contact_points, port)
        self.session = self.cluster.connect()

    def execute_query(self, query: str):
        try:
            result_set = self.session.execute(query)
            
            if query.strip().upper().startswith("SELECT"):
                return result_set
            else:
                return None 
            
        except Exception as e:
            print(f"Error executing query: {e}")
            raise Exception

    def close(self):
        self.cluster.shutdown()

    def __del__(self):
        self.close()

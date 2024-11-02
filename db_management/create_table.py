from .cassandra_db import Cassandra

class CreateTable(Cassandra):
    def __init__(self, contact_points, port, keyspace_name):
        super().__init__(contact_points, port)
        self.keyspace_name = keyspace_name
    
    def create_table(self, table_name, schema):
        query = f"CREATE TABLE IF NOT EXISTS {self.keyspace_name}.{table_name} ({schema})"
        self.execute_query(query)

    def __del__(self):
        super().__del__()
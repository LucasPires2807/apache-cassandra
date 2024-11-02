from .cassandra_db import Cassandra

class CreateKeyspace(Cassandra):
    def __init__(self, contact_points, port):
        super().__init__(contact_points, port)
    
    def create_keyspace(self, keyspace_name, replication_strategy='SimpleStrategy', replication_factor=1):
        query = f"CREATE KEYSPACE IF NOT EXISTS {keyspace_name} WITH REPLICATION = {{ 'class' : '{replication_strategy}', 'replication_factor' : {replication_factor} }}"
        self.execute_query(query)

    def __del__(self):
        super().__del__()

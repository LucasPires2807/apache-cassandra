from db_management.cassandra_db import Cassandra
from typing import Union, List

class InsertData(Cassandra):
    
    def __init__(self, contact_points, port, keyspace, table):
        super().__init__(contact_points, port)
        self.keyspace = keyspace
        self.table = table

    def insert_one_data(self, columns: Union[list, tuple], values: Union[list, tuple]):
        query = f"""INSERT INTO {self.table} ({self.table.rstrip('s')}_id, {', '.join(columns)}, created_at, updated_at)
            VALUES (uuid(), {', '.join(values)}, toTimestamp(now()), toTimestamp(now()))
        """
        self.execute_query(query)

    def insert_batch_data(self, columns: Union[list, tuple], batch_values: List[Union[list, tuple]]):
        # Start the batch statement
        batch_query = "BEGIN BATCH\n"

        for values in batch_values:
            # Convert all values to string for SQL insertion
            string_values = [f"'{value}'" if isinstance(value, str) else str(value) for value in values]
            
            # Create individual insert query for each set of values
            insert_query = f"""INSERT INTO {self.keyspace}.{self.table} ({self.table.rstrip('s')}_id, {', '.join(columns)}, created_at, updated_at)
                VALUES (uuid(), {', '.join(string_values)}, toTimestamp(now()), toTimestamp(now()));"""
            batch_query += insert_query + "\n"

        # End the batch statement
        batch_query += "APPLY BATCH;"

        # Execute the batch query
        self.execute_query(batch_query)

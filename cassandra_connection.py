from cassandra.cluster import Cluster
from dotenv import load_dotenv
from os import getenv

load_dotenv()

cluster = Cluster(getenv('CONTAINER_ID'), port=9042)  # Default port is 9042
session = cluster.connect()

# Optional: Select a keyspace if you already have one
# session.set_keyspace("your_keyspace")

if session:
    print('Connected')

# Close connection
cluster.shutdown()

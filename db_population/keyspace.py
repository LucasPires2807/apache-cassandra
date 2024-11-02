from db_management.create_keyspace import CreateKeyspace

from dotenv import load_dotenv
from os import getenv

load_dotenv()

create_keyspace = CreateKeyspace(getenv('CONTAINER_ID'), 9042)
create_keyspace.create_keyspace('store')
create_keyspace.close()
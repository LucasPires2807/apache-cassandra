# apache-cassandra

## Pre-requirements
- Python 3.11
- Docker 27.3.1

## Prepare environment

- Create a ```venv``` using ```python3.11 -m venv venv```;
- Actiavte it with ```. venv/bin/activate``` if in linux or ```. venv/Scripts/activate``` if in windows;
- Install the dependencies of the project by running ```pip install -r requirements.txt```;
- Create a ```.env``` file to put informations such as ```CASSANDRA_USER```, ```CASSANDRA_PASSWORD```;
- At the root of the project, execute ```docker compose up```;
- The value in ```CONTAINER_IP``` would be the result of the cmd command ```docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_name_or_id>```.

## Structure of the project

- Currently, the project has classes for connecting to Apache Cassandra in the container, creating a keyspace, creating tables and for insertions.
- The connecting, creating keyspace and tables classes are present under the folder db_management. The creating classes inherit from the Cassandra class which establishes connection between python and Apache Cassandra in the container.
- The insert file is the only one present in the db_manipulation folder yet. It has the class for inserting data into tables one at a time and in batches.
- There is a folder called db_population which can be used to test the behaviour of the other classes.

## Creating a local Apache Cassandra database

Simply run the following commands in sequence:

- ```python3 -m db_population.keyspace```
- ```python3 -m db_population.tables```
- ```python3 -m db_population.inserting```

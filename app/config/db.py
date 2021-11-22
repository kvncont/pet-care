import os

from azure.cosmos import CosmosClient

cosmos_url = os.environ["COSMOS_URI"]
cosmos_primary_key = os.environ["COSMOS_KEY"]
cosmos_database = os.environ["COSMOS_DB"]
cosmos_container = os.environ["COSMOS_CONTAINER"]

client = CosmosClient(cosmos_url, credential=cosmos_primary_key)
database = client.get_database_client(cosmos_database)
container = database.get_container_client(cosmos_container)

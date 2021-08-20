import logging
from azure.cosmos import CosmosClient, PartitionKey
import azure.functions as func
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Initialize the Cosmos client
    endpoint = "https://username-cosmosdb.documents.azure.com:443/"
    key = 'w2sUERZPDD7PewElhWBeDtYJfK5YKTdDLPCGiDaMKOBdXx1eaaUApdO5e3M2S2FgYo6NpWN7nUfDCKZ8fYfj0A=='

    # <create_cosmos_client>
    client = CosmosClient(endpoint, key)
    # </create_cosmos_client>

    # Create a database
    database_name = 'AzureProjectDB'
    database = client.create_database_if_not_exists(id=database_name)

    #create a container
    container_name='Generated Username'
    container=database.create_container_if_not_exists(
        id=container_name,
        partition_key=PartitionKey(path="/username")
    )
    
    letter = requests.get('https://pdwusernameapp.azurewebsites.net/api/httptriggerletter?code=lTxoaVGHLEqClSxd6czJWs1mO6WLBfptqDb128m0QVb92G3UxvsAvA==')
    number = requests.get('https://pdwusernameapp.azurewebsites.net/api/httptriggernumber?code=f0rdoQ2z9I5TNoA04DrAhuwBCmFJbAZ/qNwrBr3CGNazEaL2C9RTlQ==')
    logging.info('Requests made.')
    username=str(letter.text+number.text)
    container_item={'id' : 'username_id' , 'username': username}
    container.create_item(container_item)
    return func.HttpResponse(
        str(username),
        status_code=200
    )


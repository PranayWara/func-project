import logging

import azure.functions as func
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    letter = requests.get('https://pdwusernameapp.azurewebsites.net/api/httptriggerletter?code=lTxoaVGHLEqClSxd6czJWs1mO6WLBfptqDb128m0QVb92G3UxvsAvA==')
    number = requests.get('https://pdwusernameapp.azurewebsites.net/api/httptriggernumber?code=f0rdoQ2z9I5TNoA04DrAhuwBCmFJbAZ/qNwrBr3CGNazEaL2C9RTlQ==')

    return func.HttpResponse(
        str(letter.text+number.text),
        status_code=200
    )


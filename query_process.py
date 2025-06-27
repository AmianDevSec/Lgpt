from requests import request, Timeout, RequestException
from urllib.parse import quote
from utils import  error_string_styled

def process_query(query: str, model: str) -> str:
    """
    Process the query session.

    Args:
        query (str): The query to process.
        model (str): The model to use for processing the query. Default is "deepseek-r1".
    Return:
        str: The processed query result.
    """
    if not bool(query.strip()) : return "Hey! You forgot to send a prompt. I'm just sitting here... waiting"
    url = f"https://lgpt-back-end.onrender.com/ai/{model}?prompt={query}"
    encoded_url = quote(url, safe=':/?&=-')

    response = ''
    
    try:
        send_query = request("GET", encoded_url, timeout=5)

        json_data = send_query.json()
        response = json_data["response"]

    except Timeout:
        response = error_string_styled(f"The request timed out")
    except RequestException as e:
        response = error_string_styled(f"An error occurred: {e}")

    return response







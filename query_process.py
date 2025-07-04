from requests import request, Timeout, RequestException
from urllib.parse import quote
from utils import  error_string_styled

LGPT_VERSION = "1.2.0"
def process_query(query: str, model: str) -> str:
    """
    Process the query session.

    Args:
        query (str): The query to process.
        model (str): The model to use for processing the query. Default is "deepseek-r1".
    Return:
        str: The processed query result.
    """

    default_reply = "Hey! You forgot to send a prompt. I'm just sitting here... waiting"
    if not bool(query.strip()) :  return default_reply
    
    url = f"https://lgpt-back-end.onrender.com/ai/{model}?prompt={query}&&version={LGPT_VERSION}"
    encoded_url = quote(url, safe=':/?&=-.')

    response = ''
    
    try:
        send_query = request("GET", encoded_url, timeout=60)

        json_data = send_query.json()
        response = json_data["response"]

    except Timeout:
        response = error_string_styled(f"The request timed out")
    except RequestException as e:
        response = error_string_styled(f"An error occurred: {e}")

    return response







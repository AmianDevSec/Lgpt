from requests import request
from urllib.parse import quote

def process_query(query: str, model: str) -> str:
    """
    Process the query session.

    Args:
        query (str): The query to process.
        model (str): The model to use for processing the query. Default is "deepseek-r1".
    Return:
        str: The processed query result.
    """

    url = f"https://lgpt-back-end.onrender.com/ai/{model}?prompt={query}"
    encoded_url = quote(url, safe=':/?&=-')

    send_query = request("GET", encoded_url)

    json_data = send_query.json()
    response = json_data["response"]

    return response

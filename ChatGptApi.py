# apis.py

class ChatGPTAPI:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def get_response(self, prompt):
        # Here you might make an API call to get a response for the given prompt
        # using the provided API key.
        # For this example, we'll just return a dummy response.
        return f"Response to '{prompt}'"
    def set_key(self, api_key):
        self.api_key = api_key

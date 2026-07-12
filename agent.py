from google import genai
from prompts import SALES_PROMPT


class AISalesCopilot:

    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    def receive_task(self, lead_information):
        return lead_information

    def think(self, lead_information):
        return SALES_PROMPT.format(
            lead_information=lead_information
        )

    def execute(self, prompt):

        response = self.client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return response.text

    def respond(self, result):
        return result
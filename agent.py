from google import genai


class AISalesCopilot:

    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    def receive_task(self, lead_information):
        return lead_information

    def think(self, lead_information):
        from prompts import SALES_PROMPT
        return SALES_PROMPT.format(
            lead_information=lead_information
        )

    def execute(self, prompt):
        try:
            response = self.client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt
)

            return response.text

        except Exception as e:
            return f"⚠️ Unable to analyze the lead at the moment.\n\nError: {e}"

    def respond(self, result):
        return result
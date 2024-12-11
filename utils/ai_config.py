import google.generativeai as genai
import os

class Gemini:
    def __init__(self):        
        genai.configure(api_key=os.getenv('GEMINI_API_KEY')) 
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generateText(self, instruction):
        try:
            title = self.model.generate_content(f"Baseado no texto que eu lhe der, retorne apenas o um título, sem falar nada mais: {instruction}")
        except Exception as e:
            return e
        
        try:
            body = self.model.generate_content(f"Baseado no texto que eu lhe der, retorne apenas o um texto, sem falar nada mais: {instruction}")
        except Exception as e:
            return e
        
        
        if hasattr(body, "text") and hasattr(title, "text"):
            return {
                "title": title.text,
                "body": body.text
            }
        return None

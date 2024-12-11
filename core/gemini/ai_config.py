from google import generativeai as genai
import os

def generate_ai_content(instruction: str):
    try:
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    
        response = genai.generate_text(prompt=instruction)
        print(response)
        generated_text = response.get('text', '')
        print(generated_text)

        if not generated_text:
            raise ValueError("Conteúdo gerado está vazio")

        title_instruction = f"Crie um título conciso e informativo para o seguinte texto: {generated_text}"
        print(title_instruction)
        title_response = genai.generate_text(prompt=title_instruction)
        print(title_response)
        title = title_response.get('text', 'Erro ao gerar título')
        print(title)

        return {
            "title": title.strip(),
            "original_text": generated_text.strip()
        }

    except Exception as e:
        print(f"Erro ao gerar conteúdo: {e}")
        return {
            "title": "Erro ao gerar título",
            "original_text": "Erro ao gerar conteúdo"
        }
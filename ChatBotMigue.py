from openai import OpenAI

class ChatbotIA:
    def __init__(self, api_key):
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com/v1"
        )

        self.historial = [
            {
                "role": "system",
                "content": (
                    "Eres un asistente experto en semiconductores y sistemas digitales en 2026. "
                    "Responde de forma clara, académica y bien estructurada."
                )
            }
        ]

    def enviar_mensaje(self, mensaje_usuario):
        self.historial.append({
            "role": "user",
            "content": mensaje_usuario
        })

        respuesta = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=self.historial
        )

        reply = respuesta.choices[0].message.content

        self.historial.append({
            "role": "assistant",
            "content": reply
        })

        return reply


def iniciar_chat():
    print("🤖 Chatbot IA - DeepSeek (versión pro)")
    print("Escribe 'salir' para terminar\n")

    bot = ChatbotIA("sk-2d5996dc3b04479e9dacbf5d0085ce60")

    while True:
        user_input = input("Tú: ")

        if user_input.lower() == "salir":
            print("Bot: Hasta luego 👋")
            break

        try:
            respuesta = bot.enviar_mensaje(user_input)
            print("\nBot:", respuesta, "\n")

        except Exception as e:
            print("⚠️ Error:", e)


# Ejecutar
if __name__ == "__main__":
    iniciar_chat()
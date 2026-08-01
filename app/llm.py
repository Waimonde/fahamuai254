from langchain_ollama import ChatOllama

print("Loading Qwen model...")

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0.2,
)

print("Qwen model ready.")


class LLMService:
    def ask(self, prompt: str):
        print("Sending prompt to Qwen...")
        response = llm.invoke(prompt)
        print("Received response.")
        return response.content


llm_service = LLMService()
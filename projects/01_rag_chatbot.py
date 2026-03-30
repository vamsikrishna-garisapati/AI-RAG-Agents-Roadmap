import openai
from typing import List


class RAGChatBot:
    """
    A simple Retrieval-Augmented Generation (RAG) chatbot.
    """

    def __init__(self, api_key: str):
        openai.api_key = api_key
        self.index: List[str] = []  # Knowledge base

    def add_to_knowledge_base(self, text: str) -> None:
        """
        Add a document to the knowledge base.
        """
        self.index.append(text)

    def retrieve(self, query: str) -> List[str]:
        """
        Retrieve relevant documents based on keyword matching.
        """
        query_lower = query.lower()
        relevant_docs = [
            doc for doc in self.index
            if query_lower in doc.lower()
        ]
        return relevant_docs

    def generate_response(self, query: str) -> str:
        """
        Generate a response using retrieved context and OpenAI API.
        """
        documents = self.retrieve(query)

        if not documents:
            return "I'm sorry, but I don't have information on that."

        context = "\n".join(documents)

        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nUser Question: {query}"
            }
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        return response.choices[0].message.content.strip()


if __name__ == "__main__":
    # Initialize chatbot
    chatbot = RAGChatBot(api_key="your_api_key_here")

    # Add knowledge
    chatbot.add_to_knowledge_base("Python is a programming language.")
    chatbot.add_to_knowledge_base("RAG stands for Retrieval-Augmented Generation.")

    # User query
    user_query = "What is RAG?"

    # Generate and print response
    response = chatbot.generate_response(user_query)
    print(response)
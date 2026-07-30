def build_prompt(context, question):
    """
    Build a prompt for the LLM using retrieved context
    """

    prompt= f"""
You are an AI assistant.

Answer the user's question ONLY using the context provided below.

If the answer is not available in the context, reply:

"I don't have enough information."

Context:
{context}

Question:
{question}

Answer:
"""
    return prompt



# Test File

if __name__== "__main__":

    context="""
Machine Learning is a subset of Artificial Intelligence.

Machine Learning enables computers to learn from data.
"""

question= "What is Machine Learning?"
prompt= build_prompt(context, question)
print(prompt)
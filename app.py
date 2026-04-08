import os
from openai import OpenAI

MODEL_NAME = "gpt-4o-mini"

SYSTEM_PROMPT = """
You are a helpful customer support assistant for a small online retail company.

Write a professional, polite, and concise email reply in English.

Rules:
- Acknowledge the customer's issue
- Apologize when appropriate
- Clearly explain the next step
- Do not invent missing order details
- If important information is missing, ask for clarification
- If the case involves safety risk or legal threats, recommend escalation to a human support manager
- Keep the response under 150 words
"""

def generate_reply(customer_message: str) -> str:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set in the environment.")

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": customer_message},
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content.strip()

def main():
    print("=== Customer Support Email Draft Generator ===")
    customer_message = input("Enter customer message: ").strip()

    reply = generate_reply(customer_message)

    print("\n=== Customer Message ===")
    print(customer_message)

    print("\n=== Draft Reply ===")
    print(reply)

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("=== Customer Message ===\n")
        f.write(customer_message + "\n\n")
        f.write("=== Draft Reply ===\n")
        f.write(reply)

    print("\nOutput saved to output.txt")

if __name__ == "__main__":
    main()
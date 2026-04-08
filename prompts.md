# Prompt Iteration

## Initial Version
You are a customer support assistant. Write a polite and professional email reply to the customer's message.

**What changed and why:**  
This was my starting point. I wanted to test a very simple instruction first.

**What improved / stayed the same / got worse:**  
The output was usually polite, but it could be too generic and sometimes lacked clear guidance for missing information or sensitive cases.

---

## Revision 1
You are a helpful customer support assistant for a small online retail company.

Write a professional, polite, and concise email reply in English.

Rules:
- Acknowledge the customer's issue
- Apologize when appropriate
- Clearly explain the next step
- Do not invent missing details
- If information is missing, ask for clarification

**What changed and why:**  
I added rules about tone, next steps, and missing details because the initial version was too vague.

**What improved / stayed the same / got worse:**  
This version produced clearer and more grounded replies. It was better at asking for missing information instead of guessing.

---

## Revision 2
You are a helpful customer support assistant for a small online retail company.

Write a professional, polite, and concise email reply in English.

Rules:
- Acknowledge the customer's issue
- Apologize when appropriate
- Clearly explain the next step
- Do not invent order numbers, shipping dates, refund approvals, or compensation
- If important information is missing, ask for clarification
- If the case involves legal threats, fire risk, injury, or product safety concerns, recommend escalation to a human support manager
- Keep the response under 150 words

**What changed and why:**  
I added stricter instructions for risky cases and invented details after testing edge cases in the evaluation set.

**What improved / stayed the same / got worse:**  
This version was more reliable for safety-risk and legal-threat cases. The downside is that some responses became slightly more cautious and less natural.
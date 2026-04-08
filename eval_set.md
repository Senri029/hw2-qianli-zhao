# Evaluation Set

## Case 1: Normal case
**Input:**  
I received the wrong item in my order. I ordered a blue wireless mouse, but I got a black keyboard instead. My order number is 48392.

**What a good output should do:**  
Acknowledge the mistake, apologize, mention the order issue clearly, and explain the next step in a professional tone.

---

## Case 2: Refund request
**Input:**  
The product arrived damaged and I would like a refund. The screen is cracked and the package was already torn when it arrived.

**What a good output should do:**  
Show empathy, apologize, explain refund or return steps clearly, and avoid sounding defensive.

---

## Case 3: Edge case - angry customer
**Input:**  
This is the second time your company messed up my order. I am extremely frustrated and I want this fixed immediately.

**What a good output should do:**  
Stay calm, remain professional, avoid arguing, apologize appropriately, and offer a clear next step.

---

## Case 4: Likely failure / needs human review
**Input:**  
Your product overheated, caused sparks, and almost started a fire in my apartment. I may take legal action.

**What a good output should do:**  
Avoid making legal admissions or promising compensation, avoid hallucinating details, and recommend escalation to human review or a safety team.

---

## Case 5: Incomplete information
**Input:**  
I need help with my order. It has not arrived yet.

**What a good output should do:**  
Politely ask for missing details such as the order number or shipping information instead of guessing.
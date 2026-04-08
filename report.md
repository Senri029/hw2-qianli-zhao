# Report

## Business Use Case
For this assignment, I built a simple GenAI workflow for drafting customer support email responses. The user in this case is a customer support employee at a small online retail company. The system takes in a customer complaint or request and generates a professional reply in English.

I think this is a useful task to automate, or at least partially automate, because support teams often spend a lot of time writing similar responses. For common cases like wrong items, damaged products, delayed shipping, or refund requests, an AI draft can help save time and make the workflow more efficient.

## Model Choice
At first, I tried to use the Gemini API because it was the default option recommended in the assignment. However, during testing I ran into repeated quota and availability issues, so it was difficult to get stable results. Because of that, I switched to the OpenAI API and used gpt-4o-mini for the final version.

I chose this model because it was easy to use with Python, responded quickly, and produced writing that matched the business tone I wanted for this workflow.

## Baseline vs Final Design
My first version used a very simple prompt that asked the model to write a polite and professional customer support reply. It worked okay for basic cases, but the responses were sometimes too general. It also did not do a good job when information was missing or when the case seemed more sensitive.

After that, I revised the prompt by adding clearer instructions. I told the model to acknowledge the issue, apologize when appropriate, explain the next step, and avoid making up missing details. In the final version, I added extra rules for legal threats, safety issues, and other risky situations, telling the model to recommend human review instead of responding too confidently.

Compared with the first version, the final version was more reliable. The responses were clearer, more controlled, and better at handling missing information. It also did a better job avoiding risky claims in more serious cases.

## Remaining Failure Cases / Human Review
Even after revision, I do not think this system should be used without human review. Cases involving legal threats, possible safety issues, compensation requests, or very angry customers still need a real person to check the response.

The model is helpful for producing a first draft, but it can still sound too confident or too generic in difficult situations. Because of that, human judgment is still necessary.

## Deployment Recommendation
I would recommend using this workflow only as a drafting assistant, not as a fully automatic customer support system. I think it would be useful in a human-in-the-loop setting, where the AI writes the first version and a support employee reviews it before sending.

For routine and low-risk cases, this could save time. But for more sensitive cases, it should only be used with clear review and escalation rules.
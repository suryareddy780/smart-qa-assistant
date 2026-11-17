"""Prompt construction and optional OpenAI API integration."""
from typing import Iterable, Mapping

STYLES = {
    "Clear and concise": "Give a direct answer in a few clear sentences.",
    "Step-by-step": "Explain the answer as numbered, logical steps.",
    "Beginner-friendly": "Use simple language, define unfamiliar terms, and include an everyday analogy.",
    "Detailed": "Give a thorough explanation with useful context and an example.",
    "Socratic": "Guide the learner with a short explanation and one thoughtful follow-up question.",
}

def build_prompt(role: str, style: str, tone: str, question: str,
                 examples: Iterable[Mapping[str, str]] = ()) -> str:
    role = role.strip() or "You are a helpful assistant"
    style_instruction = STYLES.get(style, STYLES["Clear and concise"])
    lines = [
        f"ROLE: {role}.",
        f"STYLE: {style_instruction}",
        f"TONE: Use a {tone.lower()} tone.",
        "INSTRUCTIONS: Answer the user's question accurately. If uncertain, say so.",
    ]
    examples = list(examples)
    if examples:
        lines.append("FEW-SHOT EXAMPLES:")
        for i, item in enumerate(examples, 1):
            lines.extend([
                f"Example {i} question: {item['question']}",
                f"Example {i} answer: {item['answer']}",
            ])
    lines.extend(["USER QUESTION:", question.strip(), "ASSISTANT ANSWER:"])
    return "\n".join(lines)

def answer_question(role: str, style: str, tone: str, question: str,
                    examples=(), api_key: str = "", model: str = "gpt-4o-mini"):
    prompt = build_prompt(role, style, tone, question, examples)
    if api_key:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model=model or "gpt-4o-mini",
                messages=[
                    {"role": "system", "content": f"{role}. {STYLES.get(style, STYLES['Clear and concise'])} Use a {tone.lower()} tone."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.5,
            )
            return {"answer": response.choices[0].message.content or "", "prompt": prompt, "mode": "OpenAI API"}
        except Exception as exc:
            return {"answer": f"API request failed: {exc}\n\nSwitch to demo mode by clearing the API key.", "prompt": prompt, "mode": "API error"}
    return {"answer": demo_answer(question, style), "prompt": prompt, "mode": "Built-in demo (no API key required)"}

def demo_answer(question: str, style: str) -> str:
    topic = question.strip().rstrip("?!.")
    if style == "Step-by-step":
        return (f"1. Identify the main idea in: **{topic}**.\n"
                "2. Break it into smaller parts and define any key terms.\n"
                "3. Connect the parts with an example.\n"
                "4. Review the main takeaway. (Demo response: connect an API key for a generated answer.)")
    if style == "Socratic":
        return (f"Let's explore **{topic}** together. What do you already know about it? "
                "A useful first step is to identify its key idea. (Demo response.)")
    return (f"**Let's look at: {topic}.**\n\n"
            "Start with the core idea, then consider a simple example and how the pieces connect. "
            "This is a sample response to demonstrate the interface. Add an OpenAI API key for live AI answers.")

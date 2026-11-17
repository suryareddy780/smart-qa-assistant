import unittest
from prompt_engine import build_prompt, demo_answer

class PromptEngineTests(unittest.TestCase):
    def test_role_and_question_are_in_prompt(self):
        prompt = build_prompt("You are a science tutor", "Detailed", "Friendly", "Explain gravity")
        self.assertIn("You are a science tutor", prompt)
        self.assertIn("Explain gravity", prompt)

    def test_few_shot_examples_are_included(self):
        prompt = build_prompt("Tutor", "Beginner-friendly", "Friendly", "What is rain?",
                              [{"question": "What is snow?", "answer": "Frozen precipitation."}])
        self.assertIn("Example 1 question: What is snow?", prompt)
        self.assertIn("Frozen precipitation.", prompt)

    def test_no_examples_section_when_empty(self):
        prompt = build_prompt("Tutor", "Clear and concise", "Neutral", "Hi", [])
        self.assertNotIn("FEW-SHOT EXAMPLES", prompt)

    def test_demo_answer(self):
        self.assertIn("gravity", demo_answer("Explain gravity", "Clear and concise"))

if __name__ == "__main__":
    unittest.main()

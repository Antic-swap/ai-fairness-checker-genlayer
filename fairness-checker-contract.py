# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *
import typing

class AIFairnessChecker(gl.Contract):
    # State variables - what the contract remembers
    input_text: str
    verdict: str
    is_fair: bool

    def __init__(self):
        # Runs once when you deploy
        self.input_text = ""
        self.verdict = "No content checked yet"
        self.is_fair = False

    @gl.public.write
    def check_fairness(self, content: str) -> None:
        """Submit any text/content and let AI judge if it's fair/reasonable"""
        self.input_text = content

        # Non-deterministic block: This is where the AI (LLM) runs
        # It must be inside a function with NO arguments
        def get_ai_judgment() -> typing.Tuple[str, bool]:
            prompt = f"""
            You are a neutral and fair judge on the GenLayer blockchain.
            Evaluate this content for fairness and reasonableness:

            Content: "{content}"

            Respond ONLY with this exact JSON format:
            {{
                "verdict": "One short sentence explaining your decision",
                "is_fair": true or false
            }}
            Use common sense. Be objective.
            """
            # Call the LLM (this is the non-deterministic part)
            raw_response = gl.nondet.exec_prompt(prompt)
            # Simple check for the flag (in real projects you can parse JSON better)
            is_fair_flag = "true" in raw_response.lower() or "fair" in raw_response.lower()
            return (raw_response, is_fair_flag)

        # Use Equivalence Principle so validators can agree even if LLM answers vary slightly
        result = gl.eq_principle.strict_eq(get_ai_judgment)

        self.verdict = result[0]
        self.is_fair = result[1]

    @gl.public.view
    def get_result(self) -> str:
        """Read the latest check result"""
        return f"Content: {self.input_text}\n\nVerdict: {self.verdict}\nFair: {self.is_fair}"

    @gl.public.view
    def get_full_status(self) -> dict:
        """Return all data as dictionary (easy to read in Studio)"""
        return {
            "input_text": self.input_text,
            "verdict": self.verdict,
            "is_fair": self.is_fair
        }

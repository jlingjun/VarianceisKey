import logging
from openai import OpenAI
from app.config import settings

logger = logging.getLogger(__name__)

REWRITE_PROMPT = "Revise the following text:"
SYSTEM_PROMPT = """\
You are a text rewriting assistant.
Rules:
- Output rewritten text only
- No explanations
- No prefaces
- No comments
"""


class Variater:
    def __init__(self):
        self.client = OpenAI(
            base_url=settings.gen_llm_base_url,
            api_key=settings.gen_llm_api_key,
        )
        self.model = settings.gen_llm_model
    
    def rewrite_text(self, text: str) -> list[str]:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": REWRITE_PROMPT + text},
        ]
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                n=4,
            )
            results = [choice.message.content for choice in response.choices]
            return [text] + results
        except Exception as e:
            logger.error(f"Error rewriting text: {e}")
            return []

import yaml
from functools import lru_cache
from pathlib import Path

class WritingStyleService:
    def __init__(self):
        self.config_path = Path(__file__).parent.parent.parent / "src" / "automate_linkedin_posts" / "config" / "writing_styles.yaml"
    
    @lru_cache(maxsize=None)  # Cache all styles indefinitely
    def get_writing_styles(self):
        with open(self.config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def get_style_text(self, style_id: str) -> str:
        styles = self.get_writing_styles()
        style = styles.get('styles', {}).get(style_id)
        if not style:
            raise ValueError(f"Writing style with id '{style_id}' not found")
        return style['text']
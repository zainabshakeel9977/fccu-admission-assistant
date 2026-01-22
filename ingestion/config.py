from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class DocumentChunk:
    text: str
    metadata: Dict

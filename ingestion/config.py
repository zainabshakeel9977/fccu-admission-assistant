# Import dataclass decorator to easily create data-holding classes
from dataclasses import dataclass
from typing import Dict

# Define a class to represent a chunk of a document
@dataclass
class DocumentChunk:
    text: str # The actual text content of this chunk
    metadata: Dict  # Additional information about the chunk

#Dataclasses make it quick and clean to define classes whose main purpose is to store data because of less boilerplate, readable and immutable option

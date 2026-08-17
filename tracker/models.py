# tracker/models.py
from dataclasses import dataclass, asdict

@dataclass
class Expense:
    id: int
    amount: float
    category: str
    description: str

    def to_dict(self) -> dict:
        """Converts object to dictionary format for JSON saving."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Expense":
        """Creates an Expense object from a JSON dictionary."""
        return cls(
            id=data["id"],
            amount=data["amount"],
            category=data["category"],
            description=data["description"]
        )
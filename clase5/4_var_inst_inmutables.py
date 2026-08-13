from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class User:
    sistema: ClassVar[str] = "Django"
    username: str
    email: str


lucy = User("admin", "admin@example.com")
print(lucy)

print(lucy.username)
print(User.sistema)

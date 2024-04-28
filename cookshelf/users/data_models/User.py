from dataclasses import dataclass

@dataclass
class User:
    email: str
    first_name: str
    last_name: str
    user_name: str

    @classmethod
    def from_db_row(cls, row):
        return cls(email=row.email, first_name=row.first_name, last_name=row.last_name, user_name=row.user_name)
from pathlib import Path
import sys
sys.path.append(Path(__file__).parents[1])
print(sys.path)

from firestore_orm.base import Base


class User(Base):
    _collection = "users"

    email: str = None
    phone_number = None
    display_name: str = None
    photo_url: str = None
    disabled: bool = False
    first_name: str = None
    last_name: str = None
    date_account_created: str = None
    listings: list = None

    def __init__(self, id=None):
        if id != None:
            self.id = id
            self.get()
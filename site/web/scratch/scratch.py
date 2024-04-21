from typing import Callable


def add_admin_user(
    username: str, add_user_db: Callable[[str, bool], None]
) -> None:
    add_user_db(username, True)



from typing import Protocol


class AddUserDb(Protocol):
    def __call__(self, username: str, is_admin: bool) -> None:
        ...


def add_admin_user(
    username: str, add_user_db: AddUserDb
) -> None:
    add_user_db(username, True)
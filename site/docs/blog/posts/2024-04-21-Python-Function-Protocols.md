---
title: Python Function Protocols
date: 2024-04-21
description: Use function protocols to inject functions.
categories:
    - Python
---

In TypeScript, it's common to pass a function directly as a parameter with the type information.


```typescript
const addAdminUser = (
    username: string,
    addUserDB: (username: string, is_admin: boolean) => boolean): boolean => {
    return addUserDB(username, true);
}
```

The TypeScript implementation is rather straightforward.  You could imagine there there is an expensive function with IO to the db that you would like to test.  By writing a function in this style, you can stub the `addUserDB` in your tests.  Then, you're testing library doesn't have to worry about maintaining connections to a live database.


But, what would be the corollary for Python?  The most straightforward approach would be to use the `Callable` from the `typing` module:


```python
from typing import Callable


def add_admin_user(
    username: str, add_user_db: Callable[[str, bool], None]
) -> None:
    add_user_db(username, True)
```

But, did you notice one critical difference with this annotation and the TypeScript version?  The arguments aren't named!  The `Callable` supports a list of argument types (`[str, bool]` in this case).  But, how what if you wanted to name the arguments?

Enter `__call__`:

```python
from typing import Protocol


class AddUserDb(Protocol):
    def __call__(self, username: str, is_admin: bool) -> None:
        ...


def add_admin_user(
    username: str, add_user_db: AddUserDb
) -> None:
    add_user_db(username, True)

```

Obviously, the Python syntax is a little bit more verbose than the TypeScript, but at least with this implementation you get the same benefits for test isolation.
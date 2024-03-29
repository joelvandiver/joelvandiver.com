---
layout: post
title: Result Type
date: 2021-06-08
description: "Handling Errors with the F# Result Type"
---

Handling errors can be one of the most difficult aspects of any language.  Typically, languages provide a mechanism for handling *exceptional* situations.  

In F#, exceptions can be raised, such as:

```fsharp
let isGreaterThan40 x : int = 
    if x < 40
    then raise (System.Exception("The value must be greater than 5."))
    else x
```

Though *exceptional* situations do occur (such as loosing connections to a database), normal **errors** should not be treated as *exceptions*.  

> Generally speaking, if you know the rule then it is not *exceptional*.

Let's try the logic above by *capturing* the error state.

```fsharp
let isGreaterThan40 x : Result<int, string> = 
    if x < 40
    then Error "The value must be greater than 5."
    else Ok x
```

The difference in this code from the code earlier is nuanced.  The first returns a `int` while the second returns `Result<int, string>`.  

However, the key difference is that the caller of the first cannot easily access the error while the second **requires** the caller to handle the error.  

The caller can now easily aggregate errors:

```fsharp
let isOverTheHill(age: int) : Result<string, string> =
    age
    |> function
    | Ok age -> 
        age
        |> sprintf "Yeah!  You are mature at %i years old!"
        |> Ok
    | Error message -> Error [
        message
        "You still have a ways to go."
    ]
```

F# Result types are awesome because they return errors *or* successful results.  

> More generally, values in F# that can return *or*-values are called **discriminated unions**.

Capturing error state allows for greater composability and flexibility higher up the stack.  And, handling error state through the stack leads to more consistent systems with less coding *errors*!

Happy coding!


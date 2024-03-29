---
layout: post
title: Use F# Lazy Evaluation for Integration Testing
date: 2019-12-06
description: "F#'s `lazy` keyword is incredibly powerful at encapsulating expensive operations in integration testing."
---

F#'s `lazy` keyword is incredibly powerful at encapsulating expensive operations in integration testing.  If you need to make a web request, run a database query, or the like, you can wrap your call with a `lazy ()` to shield the environment from this work.  

Often in integration testing, you may need one of these expensive operations.  Each of the tests may be run independently or in parallel.  

## Simply `lazy`

First, let's explore the keyword.

```fsharp
let x = lazy (5 + 4)    // val x : Lazy<int> = Value is not created.
let y = x.Force()       // val y : int = 9
```

So, to get the value `9` out of `x`, you have to apply force to get the lazy value.  

> Just as with a `lazy` person, you have to `Force` them to do some work.

## Actually `lazy`

What's actually going on behind the scenes with the `Force`? 

Let's set up an example that includes a print in the worker so that we can see the what's happening in the work.

```fsharp
let mutable count = 0                // val mutable count : int = 1
let work () =                        // val work : unit -> int
    printfn "Starting Num %i" count
    count <- count + 1
    count                                            
let num = lazy (work())              // val num : Lazy<int> = 1
let nums =
    [
        num
        num
        num
        num
    ]
    |> List.map(fun num -> num.Force())
// Output:  Starting Num 0
// val nums : int list = [1; 1; 1; 1;]
```

Note, the "Starting Num _" was only printed once, and the successive `Force` of the `lazy` value did not increment the counter.

## Being `lazy` can be a good thing.

Now, let's setup a more typical scenario for integration testing.

```fsharp
let workHard =
    lazy (
        // Do this
        ...

        // Do that
        ...

        // Return a value.
        let hardWork = ...

        hardWork
    )

let test1 () = 
    // Arrange: Work
    let hardWork = workHard.Force()
    // Act: Use hardWork
    ...

    // Assert
    ...

let test2 () = 
    // Arrange: Work
    let hardWork = workHard.Force()
    // Act: Use hardWork
    ...

    // Assert
    ...

```

The two tests above (`test1` and `test2`) can be run independently, in series, or in parallel, and the `workHard` value will only be computed once.  Very nice!

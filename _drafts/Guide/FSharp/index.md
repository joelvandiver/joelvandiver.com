---
layout: page
title: Intro to F#
date: 2019-12-06
permalink: /guides/fsharp/intro/
---

I became a .NET developer after I taught high school Math for several years.  I also spent sometime as a Physics major in college.  I've always gravitated towards the simplicity of Mathematics.

## Imperative Code 

After gaining some level of competence in C#, I began to explore the more Math-*like* qualities of .NET programming.  In fact, the hardest time I had with C# was with the non-Math-*like* aspects.  

I remember coming across a method that returned nothing.  

What purpose could a function have if it didn't return anything?  To make matters more confusing, the method's side effect was to mutate the object in memory only.  

> This felt like magic to me, but not the delightful kind of magic...more like the magic that brought terror.  

How could I predict what was going on in the system that changed itself through the call stack?  

Well, I would have to read the code to fully understand the command line after line.  That's my informal definition of "Imperative Code".  **There has to be a better way.**

## What the `void`?

First, what is `void`?

- How can you use `void`?
- What does it mean to call a function that does not return something?

In Math, we write functions such as:

`f(x) = x + 3`

This function takes a value, `x`, and returns a value, `f(x)`.

So, I did come to understand that `void` methods only have value if they have a side effect.  The function may issue a command against a database, send a `POST` request to another api, or mutate the one of the object parameters, etc.

## What about ambiguity?

That's great that you can call a function to do this *work*, but *by definition* this is **non-deterministic**.  You cannot precisely define the remote resource being used, or the state of the object before and after mutation, etc.

On the other hand, you can't have a very helpful application if it did not have side effects some where.  

- How would the user interact with the application without some form of side effects to convey the application state?  
- How can the outside world be changed by the application without changing state as side effects?  

## Enter clarity.

Though side effects are necessary, can we at least shield a majority of our codebase to the **boundary** of our application?  This will aide us tremendously in reasoning about predictable functions.  `UNIT` testing becomes a simple answer of *input this and verify this output.*  

## Enter F#.

F# provides immutability of functions by default.  Functions by default simply take inputs and return outputs.  

You can then write simple, easily testable functions.  You can compose them up the stack into more complex structures.  

So, here's a short list of the many reasons that I made the switch to F#:

1. Immutability by Default - Mutabilty by Choice
2. Code Succinctness & Brevity
3. Function-First (rather than Class-First)
4. Function Composition
5. Function Chaining
6. Higher Order Functions
7. Simple Functional Data Structures (Records, Options, etc.)

- [Let's dive in!](/guides/fsharp/intro/setup/)
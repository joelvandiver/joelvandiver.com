---
layout: post
title: F# vs TS vs JS
date: 2021-09-06
description: "Considerations for my next stage in UI development"
---

At first glance, you may wonder how F# relates to the TS vs JS debate, but the idea of transpiling from one language to another extends much further than TS to JS.  

**TL;DR** - TS doesn't go far enough in providing tooling to a pre-transpiled JS language.  F# with the [Fable](https://fable.io/) compiler goes the necessary distance with type safety, minimal boilerplate, and awesome type inference to boot!  (imo)

For frontend development, JS *is* the runtime language.  There isn't really a debate about this because of its ubiquity.  JS is certainly not a *perfect* language (whatever that means) since it has its quirks and its own boilerplate just like most other languages.  

## Quirkiness and Boilerplate

Sure, F# has some of its own quirks, but its boilerplate is significantly reduced.  Also, I've found my thought-experience in F# is much more even and metrical with a step-by-step flow through development.  The mechanics of both TS and JS, on the other hand, consistently feel like an interruption to my thinking.

My thinking in F# is "I'd like this, and this, and ..." while with TS its "do this, oops, *I forgot*..also do this...and oh ya...do this."

It appears to me that TS added significant overhead in boilerplate as compared to JS.  Some of the features of TS have become down-right quirky in trying to strongly type a dynamic language.  For example, inferring the keys of an object literal in a switch statement is just straight-up bizarre!

## Type Inference

In TS, I find that I am spending more time explicitly telling the compiler what I want rather than thinking at the higher, more abstract level.  The true goal of abstraction is to improve the *semantics* of code.  I'm not interested in a language that keeps me from true abstractions.  With improved semantics our language shifts from *telling* the computer what we want to *describing* what we want.

My F# experience has clouded my perspective with TS here.  The F# type inference is absolutely amazing.  F# will most of the time just figure things out without you having to specifically tell it.  My attention in F# is on the *semantic* abstraction.

Of course, there's nothing quite like *type inference* in JS other than your IDE trying to provide some suggestions.  Or, there is the more aggressive type **coercion**!

## Type Safety

TS is nice to enforce **type safety**.  But, the longer I've developed the more that I realize that this idea has come to be quite elusive.  Sure, you get some assurances by the compiler telling you when you've made a syntactic error or when the types don't line up in some way. But, I have to admit that I have rarely (if ever) let a syntactic or type error escape development in JS (or T-SQL ... if that counts 🙂).  

My gravitation towards **type safety** has honestly been to support any developer who may be put on my team regardless of their skill level and attention to detail.  I now realize that this is flawed thinking.  If a developer doesn't have the attention to detail or isn't skilled enough, then I don't want them on my team.  And, that's that.

**Type safety** is not inherently bad, but it should not come at the cost of verbosity.  

Again, here's where F# wins.  The compiler is even stricter than TS in that it enforces immutability by **default** and through type inference it doesn't come with the extra penalty of verbosity.  

## The Best!

By taking quirkiness, boilerplate, type inference, and type safety into account, F# is the clear winner in my mind.  

---

But the story doesn't end there.  There's more to consider with software engineering than the simplicity and expressiveness of the development language.  I have to consider how others will maintain and contribute to the code that I write.  I have to ask larger questions about team dynamics, skill, and openness to change.

I've recently found myself surrounded by Python developers.  I'm coming from a full-stack .NET team to a tech stack built upon Python.  Python is an interesting language to me with its foundation in academia and its start in Mathematics.  And, it's dynamic (enter 😱)!  

Taking this into consideration, which language should I use to code the frontend?  

Honestly, I think I'll just drop down to plain-old JavaScript.  If I can't go the extra step to get the type inference and expressivity of F#, then I'd prefer to avoid TS altogether.  I'm not completely against TS ─ I'll just wait for the *right* project to come along before I use it.
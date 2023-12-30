---
layout: post
title: SELECT
date: 2021-12-13
---

Probably the most basic `T-SQL` statement you could possibly write is a `SELECT` statement.  

```tsql
SELECT 'Hello', 'World'
```

![](assets/2021-12-13-17-06-12.png)

Note that at this point we haven't even begun selecting against a table in the database.  We're simply selecting data as is.  

Next, let's add some column headers (a.k.a. aliases).  

```tsql
SELECT 'Peter' AS [FirstName], 'Pan' AS [LastName]
```

![](assets/2021-12-13-17-09-29.png)

The aliases can come 3 formats.  Aliases without the wrapping brackets or quotes will fail if you use a keyword for the alias.

```tsql
SELECT 'Peter' AS FirstName, 'Pan' AS LastName
SELECT 'Peter' AS [FirstName], 'Pan' AS [LastName]
SELECT 'Peter' AS 'FirstName', 'Pan' AS 'LastName'
```

I prefer the bracket syntax (`[FirstName]`) because it is more clearly differentiated from the rest of the query.
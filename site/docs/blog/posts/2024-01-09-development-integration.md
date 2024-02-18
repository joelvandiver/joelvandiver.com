---
title: Development Integration
date: 2024-01-08
description: Design a development workflow that takes different levels of integration into account.
categories:
    - DevOps
---

# Development Integration

## Problem

When developing microservices, we often run into the problem of needing other services to be available to test our application.  Our development flow should have different levels of integration.

## Levels of Integration

1. **Isolate:** Develop the service in isolation from other services.
2. **Relate:** Develop the service alongside other, highly related services.
3. **Complete:** Deploy the service to a test environment with the full suite of services available.

### Complete

It is tempting to develop with the **complete** suite of services, but this doesn't scale well.  Developer systems cannot handle the full scope of distributed systems in a cloud native environment.  We should only strive to have remote test environments include the full suite of services available.

### Relate

It is critical that we develop the related services together.  For instance, we may have the following services closely related to a business domain:

1. Nginx Static File Server
2. Python REST API
3. NodeJS Templating Engine
4. MongoDB Service

Developer systems can easily manage this workload for development.  And, it is useful to see a fully working application with data, frontend UIs, and backend services working together to solve a particular business problem.  

At this level of integration, we'll also need to isolate dependencies on other services.  I usually create stub services that provide the full interface of the dependency while at the same time providing simulations of how the actual service will behave.

### Isolate

At the first level, we should develop our service in complete isolation from all other services.  This gives us the freedom to prototype and to iterate on our service more rapidly.  We can use our standard tooling for development a service in a given framework.

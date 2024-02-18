---
title: Feature Flags
date: 2024-02-18
description: Use feature flags to separate feature deployment from code deployment.
categories:
    - DevOps
---

One of the most foundational shifts I have implemented in the software development lifecycle is feature flags.  

Traditionally, we would follow a process similar to:

1. Design a feature.
2. Develop a feature.
3. Build the code for the feature.
4. Deploy the feature to a QA environment for testing.
5. Deploy the feature to production.

But, that's a simplistic perspective of feature development.  Realistically, features follow a much more chaotic life cycle.  For example, a few iterations may look like:

1. Design feature 1.
2. Design feature 2 and develop feature 1.
3. Design feature 3 and deploy feature 1 to QA.
4. Develop feature 2 and feature 3, and fix feature 1.
5. Fix feature 2 and deploy feature 1 and feature 3 to QA.
6. Deploy feature 2 to QA.
7. Deploy features 1, 2, and 3 to production.

You can probably see how this can get unwieldy very quickly.  And, even in this complicated scenario, we haven't taken into account the need to change the final feature set at deployment.  Once a team experiences one deployment rollback, I'm sure they'll be looking to make code deployments more stable.

## Enter Flags

The concept of feature flags is really simple.  Just provide a simple data structure at runtime to enable or disable features.

```json
{
    "ff_sample_feature": true,
    "ff_another_feature": true
}
```

With this new data set, we can disable new features *by default* at deployment, and then at a later date, we can turn on the feature.  

We have now separated `code` deployment from `feature` deployment.  

## Other benefits

Feature flags open the door to many other benefits.

1. **Technical Debt Management**: You can wrap existing features scoped for deprecation in feature flags. You can leave them on by default and then schedule a time to turn them off.  At a later date, you can safely remove the code for the deprecated feature.
2. **Multi-Variate Flags**: You can configure features with multi-variate flags.  For example, you could implement a color code feature flag to change the color of the navbar based on an environment.
3. **Feature Short Circuiting**: With feature flags, the development team can take more risks by putting the riskier code behind feature flags.  For example, two code paths could provide the same business requirements, but the new code could have huge performance implications and pitfalls.  With a feature flag to toggle them, the team can schedule a time to turn switch the flag to gather some more data in production.

And, the list goes on!
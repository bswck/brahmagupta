# brahmagupta

Coding @ birthday.

This project is an attempt to re-design my previous try at solving the "high school math deduction" problem.
Given a set of known facts and a well-described goal, we need to find all the possible scenarios of coming to the solution, which we usually don't know much about.

That kind of deduction is what we are taught at school, but still happen to have problems with.
This project aims to answer why, and, more importantly, consider the question:

> Can high school math be entirely solved without heuristics?

## Examples

For instance, imagine this exam problem:

> Let's consider all natural numbers in which no digit repeats, exactly three digits are odd, and exactly two digits are even. Find the number of such numbers.

Here, we have a precisely described outcome: a natural integer that represents the number of all natural numbers matching the constraints of . 

Trying to solve this problem 100% by machine, we need to serialize it in a machine-understandable way.
How about:

```py
op.len(
    sets.natural.where(
        op.set(ctx.digits, preserve_order=True) == op.list(ctx.digits),
        op.len(ctx.digits.filter(2 .__rmod__)) == 3,
        op.len(ctx.digits.filterfalse(2 .__rmod__)) == 2,
    )
)
```

More to come in this description later.

# brahmagupta

Coding @ birthday.

This project is an attempt to re-design my previous try at solving the "high school math deduction" problem.
Given a set of known facts and a well-described goal, we need to find all the possible scenarios of coming to the solution, which we usually don't know much about.

That kind of deduction is what we are taught at school, but still happen to have problems with.
This project aims to answer why, and, more importantly, consider the question:

> Can high school math be entirely solved without heuristics?

## Examples

### Query 1. Combinatorics.

For instance, imagine this exam problem:

> Let's consider all natural numbers in which no digit repeats, exactly three digits are odd, and exactly two digits are even. Find the number of such numbers.

Here, we have a precisely described outcome: a natural integer that represents the number of all natural numbers matching the constraints that are:
- no digit in the number repeats,
- 3 digits ONLY are odd,
- 2 digits ONLY are even.

Trying to solve this problem 100% by machine, we need to serialize it in a machine-understandable way.
How about:

```py
op.len(
    sets.natural.where.all(
        op.set(digits, preserve_order=True) == op.list(digits),
        op.len(digits.filter("% 2")) == 3,
        op.len(digits.filterfalse("% 2")) == 2,
    ),
)
```

This description of the problem arises from the following assumptions:
- Digits of the number are finite.
- To check if numbers don't repeat, we convert them to a set, preserving order, and check if they equal
their list form. That would mean no digit ever repeats.
- All odd numbers fulfill the `k % 2` constraint, where `k` is the number in question.
- All even numbers fulfill the `not (k % 2)` constraint, where `k` is the number in question.

More to come in this description later.

#### Machine Digestion of the Query

The machine can simply identify the nature of the problem.

- The first conclusion it should draw is that all the numbers are computable,
they are finite, and we can fit all of them in memory.

- The number of digits is always 5 because sets `filter("% 2")` and `filterfalse("% 2")` make up the whole number and their expected lengths add up to 5.

Similar conclusions could also be drawn from more complex set of constraints, for instance

```py
op.len(
    sets.natural.where.all(
        op.any(
            op.all(
                op.len(digits.filter("% 2")) == 3,
                op.len(digits.filterfalse("% 2")) == 3,
            ),
            op.all(
                op.len(digits.filter("% 2")) == 6,
                op.len(digits.filterfalse("% 2")) == 6,
            ),
        ),
    )
)
```

absolutely implies that the number of digits must be either 6 (3 odd + 3 even) or 12 (6 odd + 6 even).

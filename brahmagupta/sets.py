from __future__ import annotations

from abc import ABCMeta
from numbers import Real
from typing import Generic, TypeVar


NumberType_co = TypeVar("NumberType_co", covariant=True, bound=Real)


class NumberSet(Generic[NumberType_co], metaclass=ABCMeta):
    pass


class Real(NumberSet[Real]):
    pass


real = Real()


@Real.register
class Rational(NumberSet[Real]):
    pass


rational = Rational()


@Real.register
class Irrational(NumberSet[Real]):
    pass


irrational = Irrational()


@Rational.register
class Integers(NumberSet[int]):
    pass


integers = Integers()


@Integers.register
class Natural(NumberSet[int]):
    pass


natural = Natural()

import math


class Experiment_data:
    # define new value class
    def __init__(self, value, abs_err=0.0, rel_err=0.0):
        self._value = value
        self._abs_err = abs_err
        self._rel_err = rel_err

    # reload x + y operation
    def __add__(self, other):
        sum = self._value + other._value
        new_abs_err = math.sqrt(self._abs_err ** 2 + other._abs_err ** 2)
        # new_rel_err =
        return Experiment_data(sum, new_abs_err)

    # reload x - y operation
    def __sub__(self, other):
        sub = self._value - other._value
        new_abs_err = math.sqrt(self._abs_err ** 2 + other._abs_err ** 2)
        # new_rel_err =
        return Experiment_data(sub, new_abs_err)

    # reload x * y operation
    def __mul__(self, other):
        mul = self._value * other._value
        # new_rel_err =
        new_rel_err = math.sqrt(self._rel_err ** 2 + other._rel_err ** 2)
        return Experiment_data(mul, rel_err=new_rel_err)

    # reload x / y operation
    def __truediv__(self, other):
        truediv = self._value / other._value
        # new_abs_err =
        new_rel_err = math.sqrt(self._rel_err ** 2 + other._rel_err ** 2)
        return Experiment_data(truediv, rel_err=new_rel_err)

    # reload x ** b operation
    def __pow__(self, power, modulo=None):
        pow = self._value ** power
        # new_abs_err =
        new_rel_err = self._rel_err ** power
        return Experiment_data(pow, rel_err=new_rel_err)

    # reload x
    def __pos__(self):
        return Experiment_data(self._value, abs_err=self._abs_err, rel_err=self._rel_err)

    # reload -(x)
    def __neg__(self):
        return Experiment_data(-self._value, abs_err=self._abs_err, rel_err=self._rel_err)

    # reload absolute values of x
    def __abs__(self):
        return Experiment_data(abs(self._value), abs_err=self._abs_err, rel_err=self._rel_err)

    # reload str(x)


    # reload sqrt(x)
    def sqrt(self):
        num = math.sqrt(self._value)
        new_rel_err = 0.5 * self._rel_err
        return Experiment_data(num, rel_err=new_rel_err)

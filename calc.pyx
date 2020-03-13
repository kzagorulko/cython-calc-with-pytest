from cPython cimport int as c_int, float as c_float

cdef class Calc:
    cpdef c_int factorial(self, int value):
        if value < 0:
            raise ValueError('Invalid argument, value less then 0')
        if value <= 1:
            return 1
        return value * self.factorial(value - 1)

    cpdef double subtract(self, float minuend, float subtrahend):
        return minuend - subtrahend

    def sum(self, *nums):
        cdef c_float result = 0.0

        for num in nums:
            result += num
            print(result)

        return result

    def multiply(self, *nums):
        cdef float result = 1

        for num in nums:
            result *= num

        return result

    def divide(self, float dividend, float divider):
        return dividend / divider

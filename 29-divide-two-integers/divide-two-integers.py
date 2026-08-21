class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend

        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1

        sign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)

        a = abs(dividend)
        b = abs(divisor)
        ans = 0

        while a >= b:
            x = b
            cnt = 1

            while x << 1 <= a:
                x <<= 1
                cnt <<= 1

            a -= x
            ans += cnt

        return ans if sign else -ans
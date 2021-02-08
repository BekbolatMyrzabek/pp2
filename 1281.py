class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Pro = 1
        Sum = 0
        while n >= 10:
            t = n % 10
            Pro = Pro * t
            Sum = Sum + t
            n = n // 10
        if n<10:
            Pro*=n
            Sum+=n
                
        return Pro - Sum
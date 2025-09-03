class Factorial:
    def factorial(self, n):
        fact = 1
        if n < 0:
            return "Factorial of a negative number is not defined."
        elif n == 0 or n == 1:
            return fact
        else:
            for i  in range(2, n+1):
                fact = fact * i
            return fact
    def factrec(self, n):
        if n < 0:
            return "Factorial of negative number is not defined."
        elif n == 0 or n == 1:
            return 1
        else:
            return n * self.factrec(n-1)

num = int(input("Enter a number: "))

f = Factorial()
print(f"The factorial of {num} using Iterative method is {f.factorial(num)}")
print(f"The factorial of {num} using recursion is {f.factrec(num)}")
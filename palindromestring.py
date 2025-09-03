class Palindrome:
    def is_palindrome(self, s):
        return s == s[::-1]
input_str = input("Enter a string: ")
string = input_str.lower()
p = Palindrome()
if p.is_palindrome(string):
    print(f'"{input_str}" is a palindrome.')
else:
    print(f'"{input_str}" is not a palindrome.')
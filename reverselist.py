class Reverse:
    def reverse_List(self, lst):
        start = 0
        end = len(lst) - 1
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start+= 1
            end-= 1
        return lst
    def reverseString(self, s):
        return s[::-1]
    def reverse_each_word(self, s):
        word_lst = s.split(" ")

        for word in word_lst:
            word_lst[word_lst.index(word)] = self.reverseString(word)
        
        return " ".join(word_lst)

import samplesort as ss

# lst = []
# length = int(input("Enter number of elements: "))
# ss.Sorting().take_input(lst, length)
input_str = input("Enter the String to be reversed: ")

rev = Reverse()
# print(rev.reverse_List(lst))

print(rev.reverseString(input_str))
print(rev.reverse_each_word(input_str))
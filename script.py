class Solution:
    def count_print_digits(self,n):
        count = 0 
        new_num_list = []
        while n!=0:
            last_digit = n%10
            new_num_list.append(last_digit)
            count += 1
            n = n//10
        new_num_list.reverse()
        for i in new_num_list:
            print(i)
        return count
            
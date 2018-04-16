#Problem here : https://leetcode.com/problems/reverse-integer/description/
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        
        """
        given = str(x)
        if(given[0]=='-'):
            return self.is_valid(-1*int(given[1:][::-1]))
        else:
            return self.is_valid(int(given[::-1]))
    
    def is_valid(self,given_number):
        if((given_number>2**31 - 1) or (given_number<-2**31)):
            return 0
        else:
            return given_number
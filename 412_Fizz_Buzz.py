
class Solution(object):
    def fizzBuzz(s):
        output =[]
        for i in range(1,s+1):
            if i% 3 ==0 and not i%5 == 0:
                a = "Fizz"
            elif i%5 == 0 and not i% 3 ==0:
                a = "Buzz"
            elif i%3 ==0 and i%5 == 0:
                a = "FizzBuzz"
            else:
                a = str(i)
            output.append(a)
        
        return output


       


s = 15
print(Solution.fizzBuzz(s))
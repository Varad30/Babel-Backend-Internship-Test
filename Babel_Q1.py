# to reverse a 3 digit number-

#Method-1 - By converting given number to string and then reversing it.
num=int(input()) #Take input from user.
str_num=str(num) #Convert given number to a string.
rev_str_num=str_num[::-1] #Reverse the String.
print("Reversed integer is: ",int(rev_str_num)) #Convert back to integer.

#Method-2 - Iterative.

num = int(input()) # Taking input from the user.
rev = 0 # Result i.e Reversed num.
while(num > 0):
    temp = num % 10
    rev = rev * 10 + temp
    num = num // 10
print(rev)
# Example-
# if num=123
# rev=0

# first iteration-
# temp=123%10=3
# rev=0*10+3=3
# num=num//10=12 [Floor division]

# Second Iteration-
# temp=12%10=2
# rev=3*10+2=32
# num=num//10=1

# Third Iteration-
# temp=1%10=1
# rev=32*10+1=321
# num=num//10=0
# as num==0, exit loop 
# rev=321 which is our result.
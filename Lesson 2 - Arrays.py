"""
The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times
Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
"""

A = [3, 8, 9, 7, 6]
K = 2

def solution(A, K):
    Z = [None] * len(A) #this creates an empty array the same length as the current Array
    for i in range(0,len(A)): #here we are looping in the range from 0 to the length of the array
         #this code puts the element into the new index position shifted across K times
            """
            The modulus len(A) is there to keep the sum values between 0 and N.
            OUR EXAMPLE WITH K=2 and length = 5:
            if we had Z[(i+k)] = A[i] and it got to length 4. It would put 4 + 2 = 6 into an index position of 6 that doesn't exist (remember the array is only of length 5) 
            whereas with modulus Z[(i+K) % len(A)] = A[i]  , at position 4(i)+2(k)= 6 % 5, it would return '1' which is now in a position in the array
            """
            Z[(i+K) % len(A)] = A[i] 
    return(Z)

print(solution(A,K))



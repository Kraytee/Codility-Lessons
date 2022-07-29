"""
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.
SO what you could do is appened the number you're looking at then have the for loop check it against all the numbers and see if they match any
"""
A = [9, 3, 9, 3, 9, 7, 9]
"""
def solution(A):
    A.sort()
    A.append(-1)
    print(A)
    for i in range(0, len(A), 2):
        if A[i] != A[i+1]:
            return(A(i))
pass

def solution(A):
  A.sort()
  for i in range(0, len(A)):
    x = A(i)
    A.insert(0,x)
    while True:
      for i in range(0,len(A)):
        if A[i] != A[i+1]:
          return(A(i))
          print(A(i))
pass

A = [9, 3, 9, 3, 9, 7, 9]

def solution(A):
  for i in range(0, len(A)):
    x = A[i]
    A.remove(A[i])
    A.insert(0,x)
    set([x for x in xs if xs.count(x) > 1])
    if A[0] != A[2]:
      return(A[0])
    elif A[0] != A[1]
pass
print(solution(A))
"""
A = [9, 3, 9, 3, 9, 7, 9]
"""
def solution(A):
  for i in range(0, len(A)):
    if len(A) == len(set(A):):
      return(A[i])
pass
print(solution(A))
"""
def solution(A):
  for i in range(0, len(A)):
    if A.count(A[i]) % 2: 
      return(A[i])
pass
print(solution(A))
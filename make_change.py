def make_change(coins, amount):

  matrix = [[0 for _ in range(amount+1)] for _ in range(len(coins))]

  for i in range(len(coins)): # base case, amount = 0
    matrix[i][0] = 1

  for row in range(len(coins)):
    for col in range(1, amount+1):
      if(coins[row] <= col):
        matrix[row][col] = (matrix[row - 1][col] + matrix[row][col - coins[row]])
      else:
        matrix[row][col] = matrix[row - 1][col]

  return matrix[-1][-1] # the last element in the matrix

print(make_change([2,3,5,10], 15))
print(make_change([1,2,5], 5))
print(make_change([1,5], 6))

"""
Time Comp.: O(m*n), where m is the amount and n is the # of coins
Space Comp.: O(m*n)
"""

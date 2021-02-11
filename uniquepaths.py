'''class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
ob1 = Solution()
print(ob1.uniquePaths(5,9))'''






'''class Solution(object):
   def uniquePaths(self, m, n):
      row = n
          column = m
          dp = [[-1 for i in range(m)] for j in range(n)]
          dp[row-2][column-1] = 1
          for i in range(column):
             dp[n-1][i] = 1
          for i in range(row):
             dp[i][column-1]=1
      for i in range(row-2,-1,-1):
         for j in range(column-2,-1,-1):
            dp[i][j] = dp[i+1][j] + dp[i][j+1]
      return dp[0][0]
ob1 = Solution()
print(ob1.uniquePaths(10,3))'''


'''class Solution(object):
    def uniquepaths(m,n):
        row = n
        column = m
        for i in range(row):
            i+=i
         for j in range(column):
            j+=j          4
            if(i=0,j=0):
                dp[i][j] = 1
            else:
                 dp[i][j] = dp[i-1][j]+dp[i][j-1]
    return dp[m-1][n-1]
ob1 = Solution()
print(ob1.uniquepaths(3,3))'''


'''class Solution(object):
    def uniquePaths(m, n):
    # Initialize m x n list with 1
        myList = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
            
            # Number of ways for current cell =
            # Number of ways for cell on the left +
            # Number of ways for cell above            
            
                myList[i][j] = myList[i-1][j] + myList[i][j-1]
    # Return result for last cell
        return myList[-1][-1]
ob1 = Solution()
print(ob1.uniquePaths(3,3))'''
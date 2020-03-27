'''
Given an array, coins, and an integer, amount, return the least amount of coins
required that adds up to amount. (Using bfs.) Return -1 if it is not possible.

Ex: coins = [1,2,5] amount = 13
Ans: 4

(This is brute force-ey. Ideally I would use DP principles and memoization to
speed the algorithm up.
'''

def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """

    queue = []
    queue.append(amount)
    depth = 1 #The depth of the tree is the amount of coins used so far

    while (len(queue) > 0):
        upper = len(coins)**(depth-1)
        
        for i in range(0, upper):
            for coin in coins:
                if queue[i] > 0:
                    newAmount = queue[i] - coin                    
                    queue.append(newAmount)
                    if newAmount == 0:
                        return depth

        for i in range(0, upper):
            queue.pop(0)

        depth += 1

    return -1

amount = 2
coins = [3]
print(coinChange(coins, amount))

amount = 13
coins = [1,2,5]
print(coinChange(coins, amount))

amount = 11
coins = [1,2,5]
print(coinChange(coins, amount))


class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
#         l = len(costs)
#         print(l)
#         c = [costs[i][0] for i in range(l)]
#         d = [costs[i][1] for i in range(l)]

#         print(c,d)
#         a=b=0
#         for i in range(l/2):
#             a+=min(c)
#             b+=min(d)
#             c.remove(min(c))
#             d.remove(min(d))
#         print(a,b)
#         return a+b
        total_cost=0
        costs.sort(key = lambda x : x[0] - x[1])
        n = len(costs) // 2
        for i in range(n):
            total_cost += costs[i][0] + costs[i + n][1]
        return total_cost

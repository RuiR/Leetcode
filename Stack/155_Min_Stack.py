# Too young too simple solution
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)


    def pop(self):
        """
        :rtype: void
        """
        self.data.pop(len(self.data)-1)


    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.data)


class MinStackBest(object):
"""
This solution is based on the solution posted in https://leetcode.com/problems/min-stack/discuss/49022/My-Python-solution/202040
It keeps track of the minimum value in the stack and save time for getting minimum value.
"""
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.data.append((x, curMin))

    def pop(self):
        """
        :rtype: void
        """
        self.data.pop()


    def top(self):
        """
        :rtype: int
        """
        if len(self.data) == 0:
            return None
        else:
            return self.data[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.data) == 0:
            return None
        else:
            return self.data[-1][1]

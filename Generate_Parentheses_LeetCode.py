class Solution(object):
    def generateParenthesis(self, n):
        result = [] 
        self.generate(result, "", 0, 0, n)
        return result
    def generate(self, result, current, open, close, n):
        if len(current) == 2 * n:
            result.append(current)
            return

        if open < n:
            self.generate(result, current + "(", open + 1, close, n)

        if close < open:
            self.generate(result, current + ")", open, close + 1, n)

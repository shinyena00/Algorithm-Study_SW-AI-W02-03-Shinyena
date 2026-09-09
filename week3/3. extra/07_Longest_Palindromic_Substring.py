class Solution:
    def longestPalindrome(self, s: str) -> str:
        current = {}
        result = (0, 0, -1) #(start, end, length)
        delete = []

        n = len(s)

        if n == 1:
            return s[0]


        if s[1] == s[0]:
            result = (0,1,0)

        def real_len(start, end, num):
            return end - start + 1 + 2 * num
        
        for i in range(2, n):
            if s[i] == s[i-1]:
                current[(i-1, i)] = 0
            if s[i] == s[i-2]:
                current[(i-2, i)] = 0
            for idx, num in current.items():
                start, end = idx[0], idx[1]
                if start - num - 1 <0 or end + num + 1 >= n:
                    if real_len(*result) < real_len(start, end, num):
                        result = (start,end,num)
                    delete.append(idx)
                else:
                    if s[start - num -1] == s[end+num + 1]:
                        current[idx] += 1
                    else:
                        if real_len(*result) < real_len(start, end, num):
                            result = (start,end,num)
                        delete.append(idx)
            for j in delete:
                del current[j]
            delete.clear()

        if result == (0,0,-1):
            return s[0]
        
        return s[result[0] - result[2] : result[1] + result[2] + 1]


        
        

        


        
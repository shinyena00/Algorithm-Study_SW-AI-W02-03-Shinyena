class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        level = 2
        step = {beginWord}
        next_step = set()
        n = len(beginWord)
        search = set(wordList)

        if endWord not in search:
            return 0

        while(step):
            for turn in step:
                for i in range(n):
                    original = turn[i]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c== original:
                            continue
                        diff = turn[:i] + c + turn[i+1:]
                        if diff in search:
                            next_step.add(diff)
            if endWord in next_step:
                return level
            level += 1
            step = next_step.copy()
            search -= next_step
            next_step.clear()
        return 0
                
                        
                    



        
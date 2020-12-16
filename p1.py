from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        level = 1
        q = deque([beginWord])
        visit = set([beginWord]) #to avoid duplicate intermediate words
        wordList = set(wordList)
        
        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                
                if curr == endWord:
                    return level
                
                for j in range(len(curr)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        
                        new = curr[:j] + c + curr[j+1:]
                        
                        if new not in visit and new in wordList:
                            q.append(new)
                            visit.add(new)
                
            level += 1
        
        return 0

#first attempt, didn't realize order mattered
def isSubsequence(self, s: str, t: str) -> bool:
    tFreq = {}
    for char in t:
        if tFreq.get(char) == None:
            tFreq.update({char:1})
        else:
            tFreq.update({char:tFreq.get(char) + 1})
            
    for char in s:
        if tFreq.get(char) == None:
            return False
        tFreq.update({char:tFreq.get(char) - 1})
        if tFreq.get(char) < -1:
            return False
    return True

#second attempt. stumped by s = "ab" and t = "baab"
def isSubsequence(self, s: str, t: str) -> bool:
    tFreq = {}
    for char in t:
        if tFreq.get(char) == None:
            tFreq.update({char:1})
        else:
            tFreq.update({char:tFreq.get(char) + 1})
            
    for char in s:
        if tFreq.get(char) == None:
            return False
        tFreq.update({char:tFreq.get(char) - 1})
        if tFreq.get(char) < 0:
            return False
                
    inorder = []
    for char in s:
        inorder.append(t.index(char))
    
    for i in range(len(inorder) - 1):
        if inorder[i] > inorder[i + 1]:
            return False
        
    return True

#after looking on leetcode, simplest solution
#he looks for the char in s (small) in t and once it finds it, it cuts t so that it only sees past the index of the char
# ex:
# s = abc
# t = haebrc

# i = a
# t = ebrc

# i = b
# t = rc

# i = c
# t = 
# return True
def isSubsequence(self, s: str, t: str) -> bool:
    for i in s:
        if i not in t:
            return False
        else:
            x = t.index(i)
            t = t[x+1:]
    return True


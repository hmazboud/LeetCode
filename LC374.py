#my first solution, had the right idea, but realized that i wasn't checking numbers inside the range
import math
def guessNumber(self, n: int) -> int:
    pick = math.ceil(n)
    while guess(pick) != 0:
        if guess(pick) == -1:
            pick = pick / 2
        elif guess(pick) == 1:
            pick = (pick + n) / 2
    return pick        

#second attempt, worked but super slow
def guessNumber(self, n: int) -> int:
    low = 1
    high = n
    pick = (low + high)/2
    
    while guess(pick) != 0:
        if guess(pick) == -1:
            high = pick
            pick = (low + high)/2
        elif guess(pick) == 1:
            low = pick
            pick = (low + high)/2
    return int(pick)

#last attempt, the problem was that i did the calculation for pick too many times and the condition being guess(pick)
# meant that it had to execute the function again to exit, waste of time
#20 ms 99.10%
#this literally doesn't matter, second solution was great
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            pick = (low + high)/2
            if guess(pick) == -1:
                high = pick
            elif guess(pick) == 1:
                low = pick
            else:
                return int(pick)
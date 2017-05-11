'''
Two tortoises named A and B must run a race. A starts with an average speed of 720 feet per hour. Young B knows she runs faster than A and furthermore has not finished her cabbage.

When she starts, at last, she can see that A has a 70 feet lead but B speed is 850 feet per hour. How long will it take B to catch A?

More generally: given two speeds v1 (A speed, integer > 0) and v2 (B speed, integer > 0) and a lead g (integer > 0) how long will it take B to catch A?

The result will be an array [h, mn, s] where h, mn, s is the time needed in hours, minutes and seconds (don't worry for fractions of second). If v1 >= v2 then return nil, nothing, null, None or {-1, -1, -1} for C++, C, Go.

Examples:

race(720, 850, 70) => [0, 32, 18]
race(80, 91, 37) => [3, 21, 49]
'''


################
def race(v1, v2, g):
    if v1>v2: return None
    res = g*3600/(v2-v1)
    return [res/3600,res%3600/60,res%60]


################
from datetime import datetime, timedelta

def race(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        sec = timedelta(seconds=int((g*3600/(v2-v1))))
        d = datetime(1,1,1) + sec

        return [d.hour, d.minute, d.second]


#################
def race(v1, v2, g):
    if v2 > v1: return [g//(v2-v1), int((g/(v2-v1)*60)%60), int((((g/(v2-v1)*60)%60)*60)%60)]




#################
from fractions import Fraction
def race(v1, v2, g):
    if v1 >= v2:
        return None
    r = Fraction(g, v2 - v1)
    h = r.__floor__()
    r = (r - h)*60
    m = r.__floor__()
    s = ((r - m)*60).__floor__()
    return [h, m, s]



###################
def race(v1, v2, g):
    if v2<v1: return None
    else:
        a=float(g/(v2-v1))
        seconds=int(a*3600)
        m,s=divmod(seconds,60)
        h,m=divmod(m,60)
        return [h,m,s]





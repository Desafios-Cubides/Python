# Link (https://www.codewars.com/kata/6376bbc66f2ae900343b7010)

def movie_times(open, close, length):
    open, close = open*60, close*60 if close > open else (close+24)*60
    return close

print(movie_times(13,11,60))
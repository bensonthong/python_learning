
#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. 
#Return True if we sleep in.
#sleep_in(False, False) → True
#sleep_in(True, False) → False
#sleep_in(False, True) → True

def sleep_in(weekday,vacation):
  if not weekday or vacation:
    return True
  else:
    return False
    
#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
#diff21(19) → 2
#diff21(10) → 11
#diff21(21) → 0

def diff21(n):
  if n>21:
    return 2*abs(2-n)
  else:
    return 21-n


#Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
#near_hundred(93) → True
#near_hundred(90) → True
#near_hundred(89) → False

  def near_hundred(n):
  withinHundred = 100-n
  withinTwoHundred = 200-n
  
  if abs(withinHundred) > 10 and abs(withinTwoHundred) > 10:
    return False
  return True

def near_hundred(n):
  if abs(100-n)<=10 or abs(200-n)<=10:
    return True
  return False

#Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
#The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
#missing_char('kitten', 1) → 'ktten'
#missing_char('kitten', 0) → 'itten'
#missing_char('kitten', 4) → 'kittn'

def missing_char(str, n):
  return str.replace(str[n],"")

def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back

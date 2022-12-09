def get_count(string):
    #Return the number (count) of vowels in the given string.
    vowels = ['a','e','i','o','u']
    vowelsCount = 0
    
    for letter in string:
      for n in vowels:
          if letter == n:
              vowelsCount += 1
    print(vowelsCount)
    return vowelsCount

get_count("abracadabra")
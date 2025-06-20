# construct a list with only prime numbers
def is_prime(x):
for i in range(2,int(x**0.5)):
  if x % i == 0 :
  return False
return Ture
n = int(input("enter list size : "))
li = []
for i in range(0,n):
   x = int(input("Enter a value : ))
   while not is_prime(x):
       x = int(input("not a prime number , enter a new value))
   li.append(x)
print(li)

## construct a matrix with only prime numbers
def is_prime(x):
    for i in range(2,int(x**0.5)):
        if x % i == 0:
          return False
    return True

r = int(input("enter row size : ))
c = int(input("enter column size : ))
li = []
for i in range(0,r):
  row = []
  for j in range(0,c):
  x = int(input())
  while not is_prime(x):
     x = int(input("not a prime, give new value : ))
  row.append(x)
li.append(row)
print(li)

# Counting the words in a string
def count_word_frequencies(paragraph):
    freq = {}

    for row in paragraph:
        for word in row:
            word_lower = word.lower()

            if word_lower == "stop":
                return freq  

            if len(word) < 3:
                continue  

            if word_lower in freq:
                freq[word_lower] += 1
            else:
                freq[word_lower] = 1

    return freq
paragraph = [
    ["Hello", "world", "hello"],
    ["this", "is", "a", "test"],
    ["STOP", "ignore", "this", "line"],
    ["should", "not", "be", "processed"]
]
print(count_word_frequencies(paragraph))



#program 2
 def check_winner(board):
    x = []
    o = []
    for i in range(3):
    for j in range(3):
        if board[i][j] == 'x':
            x.append(i * 3 + j + 1)
        elif board[i][j] == 'o':
            o.append(i *3+j+1)
        else:
            continue
    for win in winner:
        if set(win).issubset(set(x)):
              return "X wins"
        elif set(win).issubset(set(o)):
              return "O wins"
        else:
              return "Draw"       
board = [
    ["X", "O", "X"],
    ["O", "X", ""],
    ["O", "", "X"]
]

res=check_winner(board)
print(res)

      
























import random
def estimate_pi (n):
  n_in = 0
  for i in range(n):

    x = random.random()
    y = random.random()

    if x**2 + y**2 <= 1: 
      n_in += 1
    
  
  pi = 4 * n_in/ n
  return pi

print(estimate_pi(10000000))

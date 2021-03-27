def my_func(N):
  for i in range(N):
    print((lambda i: i**2)(i))
my_func(5)
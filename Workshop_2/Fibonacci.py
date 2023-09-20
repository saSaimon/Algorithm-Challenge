def fibonacci(n):
    fibonacci_series = []
    a,b =0,1
    for i in range(n):
        fibonacci_series.append(a)
        a,b = b, a+b,

    print(fibonacci_series)

fibonacci(10)
from timeit import default_timer as timer

def logarithms(n):
    i = 1
    while i <= n:
        i = i * 2
        print(i)

n = 10**3

start = timer()
logarithms(n)
end = timer()

proc_time = end - start
print(f"Processing time -> {proc_time}")
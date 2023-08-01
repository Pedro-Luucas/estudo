#sum all non negative integers up to Num     https://www.youtube.com/watch?v=ngCos392W4w

def sum(num):
    if num == 1:
        return 1
    return num + sum(num-1)

print(sum(200))
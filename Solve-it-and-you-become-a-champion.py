# https://codeforces.com/gym/406854/problem/K
# The problem was to find the sum from F(n) to F(m). which can defined by: the sum(1->m) - the sum(1 -> n-1).
# the solution is by finding the F(n) using fibonacci matrices algorithm with log(n) time complexity.
# and then to find the sum of F(1) ....F(N) is : F(n+2)-1. So, all what we need is to find the sum of F(n-1)
# by finding the F(n+1)-1 and find the sum of F(m) by F(m+2)-1. and the subtract F(n) from F(m).

# So, the time complexity of this solution is : Log(n)


from sys import stdin, stdout

MOD = 1000000007


def multi_matrix(a, b):
    if a is int:
        return b
    result = [[0, 0], [0, 0]]
    result[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % MOD
    result[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % MOD
    result[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % MOD
    result[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % MOD
    return result


def binary_expo(base, exponent):
    if exponent == 1:
        return base
    t = binary_expo(base, exponent >> 1)
    if exponent % 2 == 1:
        return multi_matrix(multi_matrix(t, t), base)
    return multi_matrix(t, t)


def multiplication(b, a):
    return [[(b[0][0] * a[0][0] + b[0][1] * a[1][0]) % MOD], [(b[1][0] * a[0][0] + b[1][1] * a[1][0]) % MOD]]


def find_fibo(n):
    a = [[0], [1]]
    b = [[0, 1], [1, 1]]
    b = binary_expo(b, n)
    return multiplication(b, a)[0][0] % MOD


for x in range(int(input())):
    a, b = map(int, stdin.readline().split())
    ans = ((find_fibo(b + 2) - 1) - (find_fibo(a + 1) - 1)) % MOD
    stdout.write(str(ans) + '\n')

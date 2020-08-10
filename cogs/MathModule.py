import discord 
from discord.ext import commands

N = 1001
f = [1] * N
g = [1] * N

for i in range (1, N):
    f[i] = i * f[i - 1]
    if(i > 2):
        g[i] = g[i - 1] + g[i - 2]

def factorial(x):
    return f[x]

def nCr(n, r):
    if(r > n):
        return -1
    ans = f[n] // (f[r] * f[n - r])
    return ans

def power(x, y):
    res = 1
    while y > 0:
        if y % 2 == 1:
            res *= x
        x = x * x
        y //= 2
    return res

def gcd(x, y):
    if(x == 0):
        return y
    return gcd(y % x, x)

def check_prime(p):
    i = 2
    while i * i <= p:
        if(p % i == 0):
            return False
        i = i + 1
    return True


class Math_Module(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.command()
    async def pow(self, ctx, x : int, y : int):
        val = power(x, y)
        await ctx.send('Your answer is: {}'.format(val))

    @commands.command()
    async def fac(self, ctx, x : int):
        await ctx.send('Value of {}! is: {}'.format(x, f[x]))
    
    @commands.command()
    async def ncr(self, ctx, n : int, r : int):
        ans = nCr(n, r)
        if(ans == -1):
            await ctx.send('Second value is greater than first value!, please try again.')
        else:
            await ctx.send('Value of C({}, {}) is: {}'.format(n, r, ans))
    
    @commands.command()
    async def gcd(self, ctx, x : int, y : int):
        await ctx.send('GCD of {} and {} is: {}'.format(x, y, gcd(x, y)))
    
    @commands.command()
    async def lcm(self, ctx, x : int, y : int):
        await ctx.send('LCM of {} and {} is: {}'.format(x, y, (x * y) // gcd(x, y)))

    @commands.command()
    async def prime(self, ctx, x : int):
        ans = check_prime(x)
        if(ans == True):
            await ctx.send('Yes, {} is a prime number'.format(x))
        else:
            await ctx.send('No, {} is not a prime number'.format(x))

    @commands.command()
    async def fibonacci(self, ctx, n : int):
        await ctx.send('{} no. Fibonacci Number is: {}'.format(n, g[n]))
    


def setup(client):
    client.add_cog(Math_Module(client))
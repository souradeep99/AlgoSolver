import discord 
from discord.ext import commands
from sys import maxsize

def get_median(a):
    a.sort()
    n = len(a)
    if(n % 2 == 0):
        return (a[n // 2] + a[n // 2 - 1]) / 2
    return a[n // 2]

def MaxSubArrSum(a): 
    size = len(a)
    dp = - maxsize - 1
    cur = 0
    start = 0
    end = 0
    s = 0
    for i in range(0,size): 
        cur += a[i] 
        if dp < cur: 
            dp = cur 
            start = s 
            end = i 
        if cur < 0: 
            cur = 0
            s = i + 1
    ans = []
    for i in range(start, end + 1):
        ans.append(a[i])
    return ans

def getPos(arr, T, l, r, key): 
    while (r - l > 1): 
        m = l + (r - l)//2
        if (arr[T[m]] >= key): 
            r = m 
        else: 
            l = m 
    return r 
   
def LongIncSubseq(arr, n): 
    tailIndices =[0 for i in range(n + 1)]   
    prevIndices =[-1 for i in range(n + 1)]   
    len = 1 
    for i in range(1, n): 
        if (arr[i] <= arr[tailIndices[0]]): 
            tailIndices[0] = i 
        elif (arr[i] > arr[tailIndices[len-1]]): 
            prevIndices[i] = tailIndices[len-1] 
            tailIndices[len] = i 
            len += 1
        else:  
            pos = getPos(arr, tailIndices, -1, len-1, arr[i]) 
            prevIndices[i] = tailIndices[pos-1] 
            tailIndices[pos] = i 
    i = tailIndices[len-1]
    ans = [] 
    while(i >= 0): 
        ans.append(arr[i]) 
        i = prevIndices[i] 
    ans.reverse()
    return ans

class List_Module(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.command()
    async def sort(self, ctx, *args):
        a = []
        for i in range(len(args)):
            x = int(args[i])
            a.append(x)
        a.sort()
        await ctx.send('Sorted List is: {}'.format(a))

    @commands.command()
    async def lis(self, ctx, *args):
        a = []
        for i in range(len(args)):
            x = int(args[i])
            a.append(x)
        await ctx.send('Longest Increasing Subsequence is: {}'.format(LongIncSubseq(a, len(a))))
    
    @commands.command()
    async def maxsum(self, ctx, *args):
        a = []
        for i in range(len(args)):
            x = int(args[i])
            a.append(x)
        ans = MaxSubArrSum(a)
        sum = 0
        for i in range(len(ans)):
            sum += ans[i]
        await ctx.send('Maximum Subarray Sum is: {}'.format(sum))
        await ctx.send('The Subarray is: {}'.format(ans))
    
    @commands.command()
    async def median(self, ctx, *args):
        a = []
        for i in range(len(args)):
            x = int(args[i])
            a.append(x)
        ans = get_median(a)
        await ctx.send('Median of the List is: {}'.format(ans))
    

def setup(client):
    client.add_cog(List_Module(client))
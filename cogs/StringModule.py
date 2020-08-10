import discord 
from discord.ext import commands

def isVowel(ch): 
    return ch.upper() in ['A', 'E', 'I', 'O', 'U'] 

def lcs_get(X, Y): 
    m = int(len(X))
    n = int(len(Y))
    L = [[0 for i in range(0, n + 1)] for j in range(0, m + 1)]
    for i in range(0, m+1): 
        for j in range(0, n+1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
    index = L[m][n] 
    Lcs = [""] * (index+1) 
    Lcs[index] = "" 
    i = m 
    j = n 
    while i > 0 and j > 0: 
        if X[i-1] == Y[j-1]: 
            Lcs[index-1] = X[i-1] 
            i-=1
            j-=1
            index-=1
        elif L[i-1][j] > L[i][j-1]: 
            i-=1
        else: 
            j-=1
    ans = ''
    for i in range(len(Lcs) - 1):
        ans = ans + Lcs[i]
    return ans

def check_palin(s):
    l = int(len(s)) // 2
    for i in range(l):
        if(s[i] != s[int(len(s)) - i - 1]):
            return False
    return True

def vowel_count(s):
    cnt = 0
    for i in range(len(s)):
        if(isVowel(s[i])):
            cnt += 1
    return cnt

def longestPalSubstr(string): 
    maxLength = 1
  
    start = 0
    length = len(string) 
    low = 0
    high = 0
    for i in range(1, length): 
        low = i - 1
        high = i 
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low 
                maxLength = high - low + 1
            low -= 1
            high += 1
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low 
                maxLength = high - low + 1
            low -= 1
            high += 1
    ans = str(string[start:start + maxLength])
    return ans

class String_Module(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def lcs(self, ctx, s : str, r : str):
        ans = lcs_get(s, r)
        if(len(ans) == 0):
            ans = 'NULL'
        await ctx.send('Longest Common Subsequence of {} and {} is: {}'.format(s, r, ans))
    
    @commands.command()
    async def palindrome(self, ctx, s : str):
        ok = check_palin(s)
        if(ok == True):
            await ctx.send('Yes!, {} is a Palindrome.'.format(s))
        else:
            await ctx.send('No!, {} is not a Palindrome.'.format(s))

    @commands.command()
    async def vowel(self, ctx, *, s : str):
        await ctx.send('Number of vowels in {} is: {}'.format(s, vowel_count(s)))

    @commands.command()
    async def longpalin(self, ctx, s : str):
        await ctx.send('Longest Palindromic substring of {} is : {}'.format(s, longestPalSubstr(s)))


def setup(client):
    client.add_cog(String_Module(client))
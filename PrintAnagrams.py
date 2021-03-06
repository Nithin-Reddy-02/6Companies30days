class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        dict = {}
        for i in range(n):
            try:
                dict[''.join(sorted(words[i]))].append(words[i])
            except:
                dict[''.join(sorted(words[i]))] = [words[i]]
            
        return dict.values()
        
        #code here

if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

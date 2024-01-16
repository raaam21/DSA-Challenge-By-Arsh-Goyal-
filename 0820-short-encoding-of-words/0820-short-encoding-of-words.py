class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        indices=[]
        words.sort(reverse=True,key=lambda x:len(x))
        print('words')
        s=''
        for i in range(len(words)):
            t=words[i]+'#'
            if t in s:
                indices.append(s.index(t)-len(t))
            else:
                s+=t
        return len(s)
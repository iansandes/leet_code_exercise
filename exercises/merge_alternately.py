def mergeAlternately(word1: str, word2: str) -> str:
        a=0
        word = ""
        for i in range(min(len(word1),len(word2))):
            word = word + word1[i] + word2[i]
        
        if len(word1) < len(word2):
            word = word + word2[len(word1):]
        else:
            word = word + word1[len(word2):]

        return word  


mergeAlternately("abcddd", "prdss")
def reverseVowels(s: str) -> str:
        result = ''
        VOWELS = ['a', 'e', 'i', 'o', 'u']
        pointer = len(s)

        for i in range(len(s)):
            if s[i].lower() in VOWELS:
                pointer -= 1
                while s[pointer].lower() not in VOWELS:
                    pointer -=1
                result += s[pointer]

            else: 
                result+= s[i]

        return result


reverseVowels("Otorrinolaringologista")



        
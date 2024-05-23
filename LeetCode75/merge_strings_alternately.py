## Following is the solution that I wrote
## Find the max of length of word1 or word2. Iterate till the longest string.
## Iterate over it and keep appending to result string
def mergeAlternately(self, word1: str, word2: str) -> str:
    word1 = "abcd"
    word2 = "pq"

    len_word1 = len(word1)
    len_word2 = len(word2)
    concat_string = ""

    iterationCounter = max(len_word1, len_word2)
    #print(iterationCounter)
    #print(concat_string)

    for i in range(iterationCounter):
        if i < len_word1:
            concat_string += word1[i]
        if i < len_word2:
            concat_string += word2[i]    

    return concat_string

## Improvement over this is to iterate till the lowest length string
## and to append the rest of the string outside the iteration

def mergeAlternately_improved(word1: str, word2: str) -> str:
    i,j = 0,0

    res = []
    while i < len(word1) and j < len(word2):
        res.append(word1[i])
        res.append(word2[j])
        i, j = i+1, j+1

    res.append(word1[i:])
    res.append(word2[j:])

    return "".join(res)

result = mergeAlternately_improved("abc","pqr")
print(result)
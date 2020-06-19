'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    print("count_th", word)
    count = 0

    # basecase
    if len(word) <= 0:
        return len(word)
       
    if word[0:2] == 'th':
        print('this word', word[0:2])
        print(word[1:3])
        count = 1

    count += count_th(word[1:len(word)])
    return count
    
    

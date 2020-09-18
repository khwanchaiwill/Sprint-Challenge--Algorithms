'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # check base case if lenght is 0 
    if len(word) == 0:
        return 0
    if word[0:2] == 'th':
        return 1+ count_th(word[2:])
    else:
        return count_th(word[1:])
if __name__ == '__main__':
    # Use the main function here to test out your implementation
    word = 'thdlaljdlthjfhth'
    print(f"th couning {count_th(word)} ")
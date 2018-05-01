def eg2_for(sentence):
    vowels = 'aeiou'
    filtered_list = []
    for l in sentence:
        if l not in vowels:
            filtered_list.append(l)
    return ''.join(filtered_list)

def eg2_lc(sentence):
    vowels = 'aeiou'
    return ''.join([ l for l in sentence if l not in vowels])

sentence = 'My name is Aarshay Jain!'
print ("FOR-loop result: " + eg2_for(sentence))
print ("LC result      : " + eg2_lc(sentence))

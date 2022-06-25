import random
import json
ample_data = { "foo": ["bar", "baz"], 
"orange": ["banana", "mango"], 
"bar": ["qux", "quux"], 
"monkey": ["cow", "parrot"], 
"banana": ["mango", "monkey"], 
"baz": ["baz"], 
"quux": ["bar", "banana"],
 "cow": ["orange"] 
 }

words = ['foo','bar','baz','banana',
'mango','parrot','monkey','quux','orange',
'purple','cow','cat','dog','yellow','green','red','mice','paprika','apple']

def add_word_to_list(words_list,words,k):
    if len(words)> 0:
        v = int(random.randint(0,len(words)-1))
        word = words[v]
        if word not in words_list and word != k:
            words_list.append(word)

        else:
            words.remove(word)
            add_word_to_list(words_list,words,k)

words_sample = {}
for i in range(100):
    k = int(random.randint(0,len(words)-1))
    words_sample[words[k]] = []
    words_c = words.copy()
    for i in range(0,6):
        add_word_to_list(words_sample[words[k]],words_c,k)
        
        
with(open('sample2.json','w')) as f:
    json.dump(words_sample,f,indent=3)
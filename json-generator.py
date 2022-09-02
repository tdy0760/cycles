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


'''
sample2.json - 100
sample3.json - 1000
sample4.json - 10000
'''
files = [{'sample2':100},{'sample3':1000},{'sample4':10000}]
for f in files:
    words_sample = {}
    for filename,v in f.items():
    
  
        for i in range(0,v):
            print(i)
            k = int(random.randint(0,len(words)-1))
            words_sample[words[k]] = []
            words_c = words.copy()
            for i in range(0,random.randint(0,7)):
                add_word_to_list(words_sample[words[k]],words_c,k)
            
        with(open(f"{filename}.json",'w')) as f:
            json.dump(words_sample,f,indent=3)

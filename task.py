import json

data = { "foo": ["bar", "baz"], 
"orange": ["banana", "mango"], 
"bar": ["qux", "quux"], 
"monkey": ["cow", "parrot"], 
"banana": ["mango", "monkey"], 
"baz": ["baz"], 
"quux": ["bar", "banana"],
 "cow": ["orange"] 
 }

cycle = []
def test():
    for k,d in data.keys():
        print(k)
        for e in d:
            if e in data.keys():
                cycle.append(k)
                cycle.append(e)
                for n in data[e]:
                    pass

def walk_cycle(key,values,data):
    if key in data.keys():
        print(key)
        values=data[key]
        for v in values:
            if v in data.keys():
                walk_cycle(v,data[v],data[:])
            else:
                continue

walk_cycle("foo",data["foo"],data)


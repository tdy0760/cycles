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

cycle = []
last_key = None
def walk_cycle(key,values,data,last_key,cycle = []):
    #print(data)
    if key in data.keys():
        values=data[key]
        for v in values:
            if v in data.keys():
                print(v)
                cycle.append(v)
                data.pop(key)    
                walk_cycle(v,data[v],data,key,cycle)

            elif last_key == v:
                print(v)
                cycle.append(v)
                print(cycle)
                print("end cycle")
                return cycle
            else:
                continue

last_key = "foo"
walk_cycle("foo",data["foo"],data,"foo")


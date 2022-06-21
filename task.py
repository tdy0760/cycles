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
def walk_cycle(key,values,data,last_key,cycle = [],cycles = []):

    if key in data.keys(): #foo
        values=data[key] #bar, baz
        for v in values: #bar
            if v in data.keys():
                print(v)
                cycle.append(v) #bar   
                walk_cycle(v,data[v],data,key,cycle,cycles)#bar,[qux,quux],data,last_key = foo,
            elif last_key == v:
                print(v)
                cycle.append(v)
                print(cycle)
                print("end cycle")
                cycles.append(cycle)
                cycle = []
                break
                
            else:
                continue
        #data.pop(last_key)
        print(data.keys())
        head = list(data.keys())[0]
        walk_cycle(head,data[head],data,head,cycle,cycles)

def walk_cycle_2(v,data,values,counter = 0,cycle = []):
        if v in data.keys() and v in cycle:
            #add to cycle, cycle could exist
            cycle.append(v)
            return cycle

        elif v in data.keys():
            cycle.append(v)
            values = data[v]
            
            print(cycle)
            walk_cycle_2(values[0],data,values,counter,cycle)
        else:
            counter+=1
            if counter < len(values):
                walk_cycle_2(values[counter],data,values,counter,cycle)
    
        return cycle


        




         
print(walk_cycle_2("foo",data,data["foo"],counter = 0,cycle = []))

#walk_cycle("foo",data["foo"],data,"foo",cycle = [],cycles = [])


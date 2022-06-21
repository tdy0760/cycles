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


def walk_cycle_2(v,data,values,counter = 0,cycle = []):

        if v in data.keys() and v in cycle:
            #add to cycle, cycle could exist
            cycle.append(v)
            return cycle

        elif v in data.keys():        
            values = data[v]
            cycle.append(v)
            #print(cycle)
            walk_cycle_2(values[0],data,values,counter,cycle)
        else:
            counter+=1
            if counter < len(values):
                walk_cycle_2(values[counter],data,values,counter,cycle)


        return cycle



minimal_cycles = {}
for k in data.keys():
    cycle = walk_cycle_2(k,data,data[k],counter = 0,cycle = [])
    #check cycle
    if cycle[0] == cycle[len(cycle)-1]:
        if k in cycle:
            minimal_cycles[k]=cycle

print(minimal_cycles)


#walk_cycle("foo",data["foo"],data,"foo",cycle = [],cycles = [])


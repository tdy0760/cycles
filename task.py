
from queue import Empty


data = { "foo": ["bar", "baz"], 
"orange": ["banana", "mango"], 
"bar": ["qux", "quux"], 
"monkey": ["cow", "parrot"], 
"banana": ["mango", "monkey"], 
"baz": ["baz"], 
"quux": ["bar", "banana"],
 "cow": ["orange"] 
 }

def remove_head(head,tail,cycle):
    if head != tail:
        cycle.remove(head)
        head=cycle[0]
        remove_head(head,tail,cycle)
    else:
        return cycle


def walk_cycle(v,data,values,start,cycle = [],cycles = []):

        if v in data.keys() and v in cycle:
            
            cycle.append(v)
            #check if cycle
            head = cycle[0]
            tail = cycle[len(cycle)-1]
            if head !=tail:
                remove_head(head,tail,cycle)
            start.remove(v)
            if len(start) > 0 :
                #checking next value from the list for cycle
                #new cycle
                cycles.append(cycle)
                walk_cycle(start[0],data,values,start,cycle=[],cycles=cycles) 
            #if no more values in start list, return cycles, proceed with next key in json
            return cycles

        elif v in data.keys():        
            values = data[v]
            #add to cycle, cycle migh exist, value in keys
            cycle.append(v)
            value = data[v][0]
            
            #data[v][0] = None
            #data[v].remove(value)
            #print(cycle)
           
            walk_cycle(value,data,values,start,cycle,cycles)
        else:
            #if not in keys, no cycle
            values.remove(v)
            #counter+=1
            #if counter < len(values):

            walk_cycle(values[0],data,values,start,cycle,cycles)


        return cycles

def filter_cycle(cycle):
    if cycle[0] == cycle[len(cycle)-1]:

        return cycle

if __name__=='__main__':
    minimal_cycles = []

    for k in data.keys():
        cycles = walk_cycle(k,data,data[k],data[k],cycle = [],cycles = [])
        print(cycle)
        cycle = filter_cycle(cycle)
        minimal_cycles.append(cycle)


    for c in minimal_cycles:
        print(c)


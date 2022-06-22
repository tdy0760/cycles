
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
            #removing v from start if in the list
            #if not in the list that means v is somwhere at the end of the cycle
            if v in start:
                start.remove(v)
            else:
                #remove v from the end, we will not be chasing twice the same
                values.remove(v)

            cycles.append(cycle)
            
            #if something left in the list go ahead with searching for new cycle
            if len(start) > 0 :
                walk_cycle(start[0],data,values,start,cycle=[],cycles=cycles) 
            #if no more values in start list, return cycles, proceed with next key in json
            return cycles

        elif v in data.keys():        
            values = data[v]
            #add to cycle, cycle migh exist, value in keys
            cycle.append(v)
            value = data[v][0]
            if v in start:
                start.remove(v)
            
           
            walk_cycle(value,data,values,start,cycle,cycles)
        else:
            #if not in keys, no cycle, remove from the list
            values.remove(v)
            

            walk_cycle(values[0],data,values,start,cycle,cycles)


        return cycles

def filter_cycle(cycle):
    if cycle[0] == cycle[len(cycle)-1]:

        return cycle

if __name__=='__main__':
    minimal_cycles = []

    for k in data.keys():
        cycles = walk_cycle(k,data,data[k],data[k],cycle = [],cycles = [])
        print(cycles)
        #cycle = filter_cycle(cycle)
        minimal_cycles+=cycles


    for c in minimal_cycles:
        print(c)


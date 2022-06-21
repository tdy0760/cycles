
data = { "foo": ["bar", "baz"], 
"orange": ["banana", "mango"], 
"bar": ["qux", "quux"], 
"monkey": ["cow", "parrot"], 
"banana": ["mango", "monkey"], 
"baz": ["baz"], 
"quux": ["bar", "banana"],
 "cow": ["orange"] 
 }


def walk_cycle(v,data,values,counter = 0,cycle = []):

        if v in data.keys() and v in cycle:
            
            cycle.append(v)
            return cycle

        elif v in data.keys():        
            values = data[v]
            #add to cycle, cycle could exist
            cycle.append(v)
            value = data[v][0]
            data[v][0] = None
            #print(cycle)
            walk_cycle(value,data,values,counter,cycle)
        else:
            counter+=1
            if counter < len(values):

                walk_cycle(values[counter],data,values,counter,cycle)


        return cycle

def filter_cycle(cycle):
    if cycle[0] == cycle[len(cycle)-1]:

        return cycle

if __name__=='__main__':
    minimal_cycles = []
    for k in data.keys():
        cycle = walk_cycle(k,data,data[k],counter = 0,cycle = [])
        print(cycle)
    #cycle = filter_cycle(cycle)
    #minimal_cycles.append(cycle)


    for c in minimal_cycles:
        print(c)


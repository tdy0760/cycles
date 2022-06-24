
import unittest
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

def remove_head(head,tail,cycle):
    '''
        if not cycle returns empty list
    '''
    if head != tail:
        cycle.remove(head)
        head=cycle[0]
        remove_head(head,tail,cycle)
    else:
        return cycle


def walk_cycle(v,data,values,start,cycle = [],cycles = []):
    '''
        v - current search value, cycle begining value
        data - json data
        values - list assigned to the key
        start - cycle begining list
        cycle - accumulator for cycle elements
        cycles - accumulator for cycles
    '''

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
            try:
                values.remove(v)
            except:
                pass

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
        value = None
        if len(data[v]) > 0:
            value = data[v][0]

        #when we add value to the cycle we remove it from the start and data
        if v in start:
            start.remove(v)
        
        try:
            if v in data[value]:
                data[value].remove(v)
        except KeyError:
            pass
        
        walk_cycle(value,data,values,start,cycle,cycles)
    else:
        #if not in keys, no cycle, remove from the list of the values and from the start of the cycle
        if v in values:
            values.remove(v)

        if v in start:
            start.remove(v)
        
        if len(values) > 0:
            walk_cycle(values[0],data,values,start,cycle,cycles)


    return cycles

def test_results(formatted_cycle):
    cycles = ['bar -> quux -> bar',
            'baz -> baz',
            'orange -> banana -> monkey -> cow -> orange']

    
    assert formatted_cycle in cycles

def format_cycle(cycle):
    i = 0
    s = ''
    separator = " -> "
    for e in cycle:
        if i % 2 != 0:
            s+=separator
            s+=e
        else:
            s+=e
            i+=1
    return s


def read_json_data(filename):
    '''
    filename - path to filename
    return dict
    '''
    json_data = None
    with open(filename,"r") as f:
        json_data  = json.load(f)
    
    return json_data


if __name__=='__main__':


    minimal_cycles = []
    for k in data.keys():
        cycles = walk_cycle(k,data,data[k],data[k],cycle = [],cycles = [])
        #print(cycles)
        
        minimal_cycles+=cycles
    
    class TestCycle(unittest.TestCase):
        def test_cycle(self,formatted_cycle, sample_cycle):
            self.asserEqual(formatted_cycle,sample_cycle)



    #for c in minimal_cycles:
    #    print(*c,sep=" -> ")
    
        


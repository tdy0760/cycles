
import json
import cycles
import timeit

sample_data = { "foo": ["bar", "baz"], 
"orange": ["banana", "mango"], 
"bar": ["qux", "quux"], 
"monkey": ["cow", "parrot"], 
"banana": ["mango", "monkey"], 
"baz": ["baz"], 
"quux": ["bar", "banana"],
 "cow": ["orange"] 
 }
def measure_time_method1():
    testcode = '''
def test():
    sample_data = { "foo": ["bar", "baz"], 
                "orange": ["banana", "mango"], 
                "bar": ["qux", "quux"], 
                "monkey": ["cow", "parrot"], 
                "banana": ["mango", "monkey"], 
                "baz": ["baz"], 
                "quux": ["bar", "banana"],
                "cow": ["orange"] 
    }
    find_cycles(**sample_data)
    '''
    et = timeit.timeit(stmt = testcode )
    print("Time execution: ",et)

def measure_time_method2():
    testcode = f"{cycles.find_cycles(sample_data)}"
    et = timeit.timeit(stmt = testcode )
    print("Time execution: ",et) 



def measure_time_method3():
    for i in ['sample.json','sample2.json']:
        with(open(i)) as f:
            sample_data = json.load(f)
            testcode = f"{cycles.find_cycles(sample_data)}"
            et = timeit.timeit(stmt = testcode )
            print("Time execution: ",et) 
        

if __name__ == '__main__':

    #measure_time_method1()
    #measure_time_method2()
    measure_time_method3()

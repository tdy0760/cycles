import cycles
import unittest

'''
sample_cycles - cycles found by hand adequate to provided rules in sample_data delivered by the client
the result of the function should be the same
'''
sample_cycles = ['bar -> quux -> bar',
            'baz -> baz',
            'orange -> banana -> monkey -> cow -> orange']

class TestCycle(unittest.TestCase):
        def test_cycle1(self):
            self.assertEqual(cycles.format_cycle(found_cycles[0]),sample_cycles[0])
        def test_cycle2(self):
            self.assertEqual(cycles.format_cycle(found_cycles[1]),sample_cycles[1])
        def test_cycle3(self):
            self.assertEqual(cycles.format_cycle(found_cycles[2]),sample_cycles[2])

 
  
if __name__ == '__main__':
    filename = 'sample.json'
   
    sample_data = cycles.read_json_data(filename)
    found_cycles = cycles.find_cycles(**sample_data)
    print("Found cycles:",found_cycles)
    unittest.main()


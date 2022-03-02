import q1
import q2
import q3
import unittest

def f(x: int, y: float, z):
    return x + y + z

def f1(course: str, year: str):
    return "Course: " + course + ", Year: " + year

class safe_call_test(unittest.TestCase):
    def test(self):
        #Good examples
        self.assertEqual(15.0,q1.safe_call(f, x=5, y=7.0, z=3))
        self.assertEqual(12.0,q1.safe_call(f, x=5, y=7.0, z=False))
        self.assertEqual('Course: Research algorithms, Year: 2022',q1.safe_call(f1, "Research algorithms", "2022"))

        #Incompatible types
        with self.assertRaises(TypeError):
            q1.safe_call(f1, course='Research algorithms', year=2022)
        with self.assertRaises(TypeError):
            q1.safe_call(f, x="abc", y=7.0,z=3)
            
class print_sorted_test(unittest.TestCase):
    def test(self):
        self.assertEqual({'a': 5, 'b': [1, 2, 3, 4], 'c': 6},q2.print_sorted({"a": 5, "c": 6, "b": [1, 3, 2, 4]})) 
        self.assertEqual([0, 1, 2, 4, 5, 9, [5, 6], [3, 6, 7, 8]],q2.print_sorted([2, 1, 9, 0, [7, 6, 3, 8], 5, [6, 5], 4])) 
        self.assertEqual(('a', 'b', 'c', 'd', [0, 2, 5, 10]),q2.print_sorted(('a', 'c', 'd', (5, 0, 10,2), 'b')))
        

class find_root_test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(2.0, round(q3.find_root(lambda x: x ** 2 - 4, 1, 3)))
        self.assertAlmostEqual(9.0, round(q3.find_root(lambda x: x ** 2 - 81, 5, 10)))
        self.assertAlmostEqual(1.0, round(q3.find_root(lambda x: x ** 3 - 1, 0, 2)))



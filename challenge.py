def make_division_by(n):
    """This closure returns a function that returns the division
       of an x number by n 
    """
    def division(x):
        assert x != 0, 'Denominator can\'t be zero'
        return x / n
    return division


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # The expected output is 3


if __name__ == '__main__':
    import unittest
    run()
    class ClosureSuite(unittest.TestCase):

        def setUp(self):
            self.tests = {
                6: [18,3],
                20: [100,5],
                3: [54,18],
            }


        def test_closure_make_division_by(self):
            for result, test in self.tests.items():
                division_n = make_division_by(test[1])
                self.assertEqual(result, division_n(test[0]))
                del(division_n)
                

        def tearDown(self):
            del(self.tests)
 

    unittest.main()
    

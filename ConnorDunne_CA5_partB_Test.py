#Name: Connor Dunne
#Student Number: 10361551
#Calculator Function Testing
#This programme tests the Calculator module to ensure expected values are returned

import numpy
from ConnorDunne_CA5_partB import Calculator #import Calculator module from file
import unittest   #import unit test to run self assertion tests to ensure exact value is calculated
import numpy.testing as npt   #import numpy testing module to run tests where approximation will do. Assigned name npt


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()   #assign Calculator() function to self.calc
	
	#Test add() function using self assert
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add([2,3,4])
        self.assertEqual(9, result)
        result = self.calc.add([10])
        self.assertEqual(10, result)
        result = self.calc.add([2,-2])
        self.assertEqual(0, result)
	
	#Test subtract() function using self assert
    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.calc.subtract([2,2])
        self.assertEqual(0, result)
        result = self.calc.subtract([2,2,2])
        self.assertEqual(-2, result)
        result = self.calc.subtract([2,-4])
        self.assertEqual(6, result)
	
	#Test multiply() function using self assert
    def test_calculator_multiply_method_returns_correct_result(self):
        result = self.calc.multiply([2,3],[1,1,1])
        self.assertEqual([2,2,2,3,3,3], result)
        result = self.calc.multiply([2,2,2],[1,1,-1])
        self.assertEqual([2,2,-2,2,2,-2,2,2,-2], result)
        result = self.calc.multiply([2,-4],[1])
        self.assertEqual([2,-4], result)
	
	#Test divide() function using self assert
    def test_calculator_divide_method_returns_correct_result(self):
        result = self.calc.divide([2,2],[2,2,2])
        self.assertEqual([1,1,1,1,1,1], result)
        result = self.calc.divide([4,4],[4,2])
        self.assertEqual([1,2,1,2], result)
        result = self.calc.divide([2,4,2],[1,1])
        self.assertEqual([2,2,4,4,2,2], result)
        result = self.calc.divide([-4,2],[4,-4])
        self.assertEqual([-1,1,0,-1], result)
		
	#Test squareroot() function using assert_almost_equal. Tests result to 12 decimal places. Anything else is ignored
    def test_calculator_squareroot_method_returns_correct_result(self):
        result = self.calc.squareroot([2,2])
        npt.assert_almost_equal([1.4142135623730951,1.4142135623730951], result, decimal = 12)
        result = self.calc.squareroot([4,4])
        npt.assert_almost_equal([2.0,2.0], result, decimal = 12)
        result = self.calc.squareroot([4.0,4])
        npt.assert_almost_equal([2.0,2.0], result, decimal = 12)
        
    #Test sine() function using assert_almost_equal
    def test_calculator_sine_method_returns_correct_result(self):
        result = self.calc.sine([2,2])
        npt.assert_almost_equal([0.9092974268256817,0.9092974268256817], result, decimal = 12)
        result = self.calc.sine([4,4])
        npt.assert_almost_equal([-0.7568024953079282,-0.7568024953079282], result, decimal = 12)
        result = self.calc.sine([-4,-4])
        npt.assert_almost_equal([0.7568024953079282,0.7568024953079282], result, decimal = 12)
        
    #Test cosine() function using assert_almost_equal
    def test_calculator_cosine_method_returns_correct_result(self):
        result = self.calc.cosine([2,2])
        npt.assert_almost_equal([-0.4161468365471424,-0.4161468365471424], result, decimal = 12)
        result = self.calc.cosine([4,4])
        npt.assert_almost_equal([-0.6536436208636119,-0.6536436208636119], result, decimal = 12)
        result = self.calc.cosine([-4,-4])
        npt.assert_almost_equal([-0.6536436208636119,-0.6536436208636119], result, decimal = 12)
        
    #Test tangent() function using assert_almost_equal
    def test_calculator_tangent_method_returns_correct_result(self):
        result = self.calc.tangent([2,2])
        npt.assert_almost_equal([-2.185039863261519,-2.185039863261519], result, decimal = 12)
        result = self.calc.tangent([4,4])
        npt.assert_almost_equal([1.1578212823495775,1.1578212823495775], result, decimal = 12)
        result = self.calc.tangent([-4,-4])
        npt.assert_almost_equal([-1.1578212823495775,-1.1578212823495775], result, decimal = 12)
        
    #Test b10log() function using assert_almost_equal
    def test_calculator_b10log_method_returns_correct_result(self):
        result = self.calc.b10log([2,2])
        npt.assert_almost_equal([0.3010299956639812,0.3010299956639812], result, decimal = 12)
        result = self.calc.b10log([4,4])
        npt.assert_almost_equal([0.6020599913279624,0.6020599913279624], result, decimal = 12)
        result = self.calc.b10log([4.0,4.0])
        npt.assert_almost_equal([0.6020599913279624,0.6020599913279624], result, decimal = 12)
        
    #Test exponent() function using self assert
    def test_calculator_exponent_method_returns_correct_result(self):
        result = self.calc.exponent([2,2],2)
        self.assertEqual([4,4], result)
        result = self.calc.exponent([2,2],4)
        self.assertEqual([16,16], result)
        result = self.calc.exponent([2,2],-4)
        self.assertEqual([0.0625,0.0625], result)
		
    #test for negative results to ensure ValueError is raised
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, ['two',1],)
        self.assertRaises(ValueError, self.calc.subtract, ['three',2])
        self.assertRaises(ValueError, self.calc.multiply, ['one','two'], [1,1])
        self.assertRaises(ValueError, self.calc.divide, [1,1], [1,'three'])
        self.assertRaises(ValueError, self.calc.squareroot, ['two','three'])
        self.assertRaises(ValueError, self.calc.sine, ['two',1])
        self.assertRaises(ValueError, self.calc.cosine, [1,'two'])
        self.assertRaises(ValueError, self.calc.tangent, [1,1,'two'])
        self.assertRaises(ValueError, self.calc.b10log, ['two',1,1])
        self.assertRaises(ValueError, self.calc.exponent, [2,2,2], 'three')
     
    #test for negative results in math domain error
    def test_calculator_returns_error_message_if_argument_outside_domain(self):
        self.assertRaises(ValueError, self.calc.squareroot, [-1,2,3])
        self.assertRaises(ValueError, self.calc.b10log, [0,2,3])
         
if __name__ == '__main__':
    unittest.main()
from django.test import SimpleTestCase
from app import calc 

class CalcTests(SimpleTestCase):
    '''Test the calc module.'''
          
    def test_add_numbers(self):
        res = calc.add(5,6)
        self.assertEqual(res,11)

    def test_subtract_numbers(self):
        res = calc.subtract(10,15)
        self.assertEqual(res,5) 
     
    def test_topla(self):
        sonuc = calc.add(5,6)
        self.assertEqual(sonuc,11)
    
    def test_topla(self):
        sonuc=calc.topla(9,15)
        self.assertEqual(sonuc,24)    
              
                                  
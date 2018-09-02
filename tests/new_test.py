import unittest
from .models import New
Headlines = news.Headlines

class NewsTest(unitest,TestCase):
    '''
    test class to test the behaviour of the headlines class
    '''

    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_news = Headlines(1234,'mist','nick','today there was alot of mist','')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ =='__main__':
    unittest.main()
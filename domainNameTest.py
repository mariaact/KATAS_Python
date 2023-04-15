import unittest
from domainName import domain_name

class TestMiPrograma(unittest.TestCase):
    def test1(self):
        self.assertEqual(domain_name('j6pi5nmtgrkcik9lmg8.pro/default.html'), 'j6pi5nmtgrkcik9lmg8')
    def test2(self):
        self.assertEqual(domain_name("http://google.com"), 'google')

    def test3(self):
        self.assertEqual(domain_name("http://google.co.jp"), 'google')

    def test4(self):
        self.assertEqual(domain_name("www.xakep.ru"), 'xakep')

    def test5(self):
         self.assertEqual(domain_name("https://youtube.com"), 'youtube')
        

  

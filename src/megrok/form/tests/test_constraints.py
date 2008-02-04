import unittest
from megrok.form import constraints

class TestConstraints(unittest.TestCase):

    def test_isSSN(self):
        v = constraints.isSSN
        self.failUnlessEqual(v('111223333'), True)
        self.failUnlessEqual(v('111-22-3333', ignore=r'-'), True)

    def test_isUSPhoneNumber(self):
        v = constraints.isUSPhoneNumber
        self.failUnlessEqual(v('(212) 555-1212',
                               ignore=r'[\s\(\)\-]'), True)
        self.failUnlessEqual(v('2125551212',
                               ignore=r'[\s\(\)\-]'), True)

        self.failUnlessEqual(v('(212) 555-1212'), True)
        
    def test_isInternationalPhoneNumber(self):
        v = constraints.isInternationalPhoneNumber
        self.failUnlessEqual(v('+1 713 942 2377'), True)
        self.failUnlessEqual(v('+1 832 201 8856'), True)

    def test_isZipCode(self):
        v = constraints.isZipCode
        self.failUnlessEqual(v('03750'), True)
        self.failUnlessEqual(v('33701-4313', ignore=r'-'), True)

    def test_isURL(self):
        v = constraints.isURL
        self.failUnlessEqual(v('http://foo.bar:8080/manage'), True)
        self.failUnlessEqual(v('https://foo.bar:8080/manage'), True)
        self.failUnlessEqual(v('irc://tiran@irc.freenode.net:6667/#plone'), True)
        self.failUnlessEqual(v('fish://tiran:password@myserver/~/'), True)
        self.failIfEqual(v('http://\n'), True)
        self.failIfEqual(v('../foo/bar'), True)

    def test_isEmail(self):
        v = constraints.isEmail
        self.failUnlessEqual(v('test@test.com'), True)
        self.failIfEqual(v('@foo.bar'), True)
        self.failIfEqual(v('me'), True)

def test_suite():
    tests = ('test_isSSN', 'test_isUSPhoneNumber', 'test_isInternationalPhoneNumber', 
             'test_isZipCode', 'test_isURL', 'test_isEmail')
    return unittest.TestSuite(map(TestConstraints, tests))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
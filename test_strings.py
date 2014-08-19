import timeit
from UserString import MutableString
from array import array
from cStringIO import StringIO


def test_methods(n, count):
    def method1():
        s = ''
        for i in strings:
            s += i
        return s

    def method2():
        s = ''
        for i in strings:
            s = s + i
        return s

    def method3():
        return ''.join(strings)

    def method4():
        s = ''
        for i in strings:
            s = '%s%s' % (s, i)
        return s

    def method5():
        s = MutableString()
        for i in strings:
            s += i
        return s

    def method6():
        s = array('c')
        for i in strings:
            s.fromstring(i)
        return s.tostring()

    def method7():
        s = StringIO()
        for i in strings:
            s.write(i)
        return s.getvalue()

    methods_list = [method5,
                    method6, method7]
    strings = ['*'*n for i in xrange(count)]
    timers = []
    for method in methods_list:
        t = timeit.timeit(method)
        print '%s ==> %s' % (method.__name__, t)
        timers.append((method.__name__, t))
    best = min(timers, key=lambda item: item[1])
    print '\nThe best way is: %s (%s)' % (best[0], best[1])

little_size = 1
big_zise = 10000
test_params = dict(
    two_little_strings=[little_size, 2],
    two_big_strings=[big_zise, 2],
    hundred_little_strings=[little_size, 100],
    hundred_big_strings=[big_zise, 100],
    )

# for name, params in test_params.iteritems():
#     print '='*80
#     print name
#     test_methods(*params)
test_methods(big_zise, 100)
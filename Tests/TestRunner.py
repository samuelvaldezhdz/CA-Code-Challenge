import sys
sys.path.append(sys.path[0] + "/...")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())
 
from unittest import TestLoader, TestSuite, TextTestRunner
from Tests.test_All import LM_NewsPage
 
import testtools as testtools
 
if __name__ == "__main__":
 
    test_loader = TestLoader()
    # Test Suite is used for scalability when adding new test cases
    test_suite = TestSuite(
        test_loader.loadTestsFromTestCase(LM_NewsPage)
        )
 
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
 
    parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    parallel_suite.run(testtools.StreamResult())
    
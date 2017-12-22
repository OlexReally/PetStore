from junit_xml import TestSuite, TestCase

test_cases = [TestCase(r'delete\test_delete')]
ts = TestSuite("my test suite", test_cases)
# pretty printing is on by default but can be disabled using prettyprint=False
print(TestSuite.to_xml_string([ts]))

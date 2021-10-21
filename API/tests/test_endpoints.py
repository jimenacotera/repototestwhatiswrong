
from unittest import TestCase, skip 

import API.endpoints as ep


class EndpointTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello(self):
        hello = ep.HelloWorld(Resource)
        get = hello.get()
        self.assertIsInstance(ret, dict)
        self.assertIn(ep.HELLO, ret)

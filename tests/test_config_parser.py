import unittest, ConfigParser, os
from mock import Mock
from Hoggy2.utils import get_config

class TestConfig(unittest.TestCase):
    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_inner_exception_raised_on_no_file_parameter(self):
        parser = Mock(ConfigParser.RawConfigParser)
        config = get_config(parser)
        assert parser.read.called

    def test_config_reads_from_file_parameter(self):
        parser = Mock(ConfigParser.RawConfigParser)
        config = get_config(parser, "testing.ini")
        parser.read.assert_called_with("testing.ini") 


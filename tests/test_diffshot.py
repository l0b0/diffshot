from __future__ import print_function
import unittest
import mock

from diffshot import diffshot
from tests.utilities import module_function_name


class TestPythonSkeleton(unittest.TestCase):
    @mock.patch(module_function_name(print))
    def test_should_print_hello_world(self, mock_print):
        skeleton = diffshot.ScreenshotDiffer()
        skeleton.hello()
        mock_print.assert_called_once_with('Hello world!')

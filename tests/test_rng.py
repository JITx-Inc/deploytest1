import jitx
import jitx.test

from jitxlib.CHANGEME.sample_1 import get_random_number


class TestRandomNumberGenerator(jitx.test.TestCase):
    def test_221(self):
        self.assertEqual(get_random_number(), 4)

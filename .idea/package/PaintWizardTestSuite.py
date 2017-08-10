import unittest
from Paintwizard import *

class PaintWizardTestSuite(unittest.TestCase):
    cheapoMax = Paint("cheapoMax", 20, 19.99, 10)
    def test_paintObject(self):
        self.assertEquals("cheapoMax", cheapoMax.name)
        self.assertEquals(20, cheapoMax.litresCan)
        self.assertEquals(19.99, cheapoMax.priceCan)
        self.assertEquals(10, cheapoMax.coveragePerLitre)
    def test_paintPrice(self):
        self.assertEqual(39.98, cheapoMax.pricePerRoom(300))
    def test_paintCoverage(self):
        self.assertEqual(200, cheapoMax.getCoveragePerCan())
if __name__ == '__main__':
    unittest.main()
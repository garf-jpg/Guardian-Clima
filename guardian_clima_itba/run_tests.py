# -*- coding: utf-8 -*-
import unittest
import sys
from tests import TestGuardianClima

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGuardianClima)
    with open("results.txt", "w", encoding="utf-8") as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        result = runner.run(suite)
        f.write(f"\nWas successful: {result.wasSuccessful()}\n")
        f.write(f"Errors: {len(result.errors)}\n")
        f.write(f"Failures: {len(result.failures)}\n")
    sys.exit(0 if result.wasSuccessful() else 1)

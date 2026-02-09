# test_echobridge.py
"""
Tests for EchoBridge module.
"""

import unittest
from echobridge import EchoBridge

class TestEchoBridge(unittest.TestCase):
    """Test cases for EchoBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EchoBridge()
        self.assertIsInstance(instance, EchoBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EchoBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

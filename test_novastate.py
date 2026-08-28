# test_novastate.py
"""
Tests for NovaState module.
"""

import unittest
from novastate import NovaState

class TestNovaState(unittest.TestCase):
    """Test cases for NovaState class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NovaState()
        self.assertIsInstance(instance, NovaState)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NovaState()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

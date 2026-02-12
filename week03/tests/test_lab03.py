import sys
import os

# --- THE FORCE FIX ---
# This forces Python to look in the folder above (week03) to find your code
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
# ---------------------

import random
from unittest.mock import patch
from lab03 import generate_mad_lib, guessing_game

def test_generate_mad_lib():
    """Tests the generate_mad_lib function to ensure it uses the inputs correctly."""
    # Test case 1: Basic functionality
    adj = "silly"
    noun = "cat" 
    verb = "jumped"
    
    story = generate_mad_lib(adj, noun, verb)
    
    # Verify function returns a string
    assert isinstance(story, str), "Function should return a string"
    
    # Verify all words are used in the story
    assert adj in story, f"Adjective '{adj}' not found in story"
    assert noun in story, f"Noun '{noun}' not found in story"
    assert verb in story, f"Verb '{verb}' not found in story"
    
    # Test case 2: Different inputs
    adj2 = "brave"
    noun2 = "knight"
    verb2 = "battled"
    
    story2 = generate_mad_lib(adj2, noun2, verb2)
    
    assert isinstance(story2, str), "Function should return a string"
    assert adj2 in story2, f"Adjective '{adj2}' not found in story"
    assert noun2 in story2, f"Noun '{noun2}' not found in story"  
    assert verb2 in story2, f"Verb '{verb2}' not found in story"

def test_guessing_game():
    """Tests the guessing_game function logic using mocking."""
    # Mock random.randint to return 50
    with patch('lab03.random.randint', return_value=50):
        # Mock input to simulate: 75 (High), 25 (Low), 50 (Correct)
        with patch('builtins.input', side_effect=['75', '25', '50']):
            # Mock print to capture output
            with patch('builtins.print') as mock_print:
                guessing_game()
                
                assert mock_print.called, "Game should produce output"
                
                # Check output content
                printed_output = [str(call) for call in mock_print.call_args_list]
                
                # Verify feedback logic
                has_high = any('high' in s.lower() for s in printed_output)
                has_low = any('low' in s.lower() for s in printed_output)
                has_success = any('congratulations' in s.lower() or 'guessed it' in s.lower() for s in printed_output)
                
                assert has_high, "Should warn when guess is too high"
                assert has_low, "Should warn when guess is too low"
                assert has_success, "Should congratulate upon success"
from logic_utils import check_guess, parse_guess

#FIX: Edited pre-existing tests to match new check_guess behavior

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

#FIX: Added a test for a valid guess

def test_parse_guess_valid():
    ok, guess, err = parse_guess("42", 1, 100)
    assert ok is True
    assert guess == 42
    assert err is None

def test_parse_guess_boundary_low():
    ok, guess, err = parse_guess("1", 1, 100)
    assert ok is True
    assert guess == 1
    assert err is None

def test_parse_guess_boundary_high():
    ok, guess, err = parse_guess("100", 1, 100)
    assert ok is True
    assert guess == 100
    assert err is None

def test_parse_guess_below_range():
    ok, guess, err = parse_guess("0", 1, 100)
    assert ok is False
    assert guess is None
    assert err == "Guess must be between 1 and 100."

def test_parse_guess_above_range():
    ok, guess, err = parse_guess("101", 1, 100)
    assert ok is False
    assert guess is None
    assert err == "Guess must be between 1 and 100."

def test_parse_guess_decimal_rejected():
    ok, guess, err = parse_guess("5.5", 1, 100)
    assert ok is False
    assert guess is None
    assert err == "Enter a whole number (no decimals)."

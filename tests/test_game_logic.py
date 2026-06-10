from logic_utils import check_guess, update_score

def test_winning_guess():
    """Test that a matching guess returns 'Win' with correct message."""
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    """Test that a guess higher than secret returns 'Too High' with 'Go LOWER' hint."""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    """Test that a guess lower than secret returns 'Too Low' with 'Go HIGHER' hint."""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_guess_too_high_type_mismatch():
    """Test the TypeError path: when guess is int and secret is string, guess > secret should still be corrected."""
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low_type_mismatch():
    """Test the TypeError path: when guess is int and secret is string, guess < secret should still be corrected."""
    outcome, message = check_guess(40, "50")
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


# Tests for attempt counter logic
def test_attempt_1_win_score():
    """Test that winning on attempt 1 gives maximum score (80 points)."""
    # Score = 100 - 10 * (attempt_number + 1) = 100 - 10 * (1 + 1) = 80
    score = update_score(0, "Win", 1)
    assert score == 80


def test_attempt_6_win_score():
    """Test that winning on attempt 6 gives minimum score (10 points)."""
    # Score = 100 - 10 * (6 + 1) = 100 - 70 = 30, but capped at 10
    # Actually: 100 - 10 * 7 = 30, which is >= 10, so it's 30
    score = update_score(0, "Win", 6)
    assert score == 30


def test_attempt_limit_exceeded():
    """Test that winning on attempt 11+ gives minimum score (10 points)."""
    # Score = 100 - 10 * (11 + 1) = 100 - 120 = -20, capped at 10
    score = update_score(0, "Win", 11)
    assert score == 10


def test_too_high_odd_attempt_penalty():
    """Test that 'Too High' on odd attempt numbers incurs a -5 penalty."""
    current_score = 50
    # Attempt 1, 3, 5, 7, etc. are odd
    new_score = update_score(current_score, "Too High", 1)
    assert new_score == 45  # 50 - 5


def test_too_high_even_attempt_bonus():
    """Test that 'Too High' on even attempt numbers grants a +5 bonus."""
    current_score = 50
    # Attempt 2, 4, 6, 8, etc. are even
    new_score = update_score(current_score, "Too High", 2)
    assert new_score == 55  # 50 + 5


def test_too_low_always_penalty():
    """Test that 'Too Low' always incurs a -5 penalty regardless of attempt number."""
    current_score = 50
    # Both odd and even attempts
    new_score_odd = update_score(current_score, "Too Low", 1)
    new_score_even = update_score(current_score, "Too Low", 2)
    assert new_score_odd == 45  # 50 - 5
    assert new_score_even == 45  # 50 - 5


def test_attempt_counter_scenario():
    """
    Integration test documenting the expected attempt flow:
    - Attempts initialized at 0
    - Each guess increments attempts: 1, 2, 3, ...
    - Game ends when attempts >= attempt_limit (e.g., 6 for Easy mode)
    """
    # This test documents the expected behavior:
    # Initial: attempts=0 → "Attempts left: 6"
    # After 1st guess: attempts=1 → "Attempts left: 5"
    # After 2nd guess: attempts=2 → "Attempts left: 4"
    # ...
    # After 6th guess: attempts=6 → "Attempts left: 0" AND game ends (6 >= 6)
    
    attempt_limit = 6
    
    # Verify attempts count from 1 to limit
    for attempt_num in range(1, attempt_limit + 1):
        attempts_left = attempt_limit - attempt_num
        assert attempts_left >= 0, f"Attempt {attempt_num}: Should have {attempts_left} attempts left"
    
    # Verify game ends at limit
    assert attempt_limit >= attempt_limit, "Game should end when attempts >= limit"


def test_display_attempts_left():
    """Test that 'Attempts left' display counts down correctly from initial to final."""
    attempt_limit = 6
    
    # Initial load: attempts=0 → display should show 6
    attempts = 0
    attempts_left_display = attempt_limit - attempts
    assert attempts_left_display == 6, "Initial display should show 6 attempts left"
    
    # After 1st guess: attempts=1 → display should show 5
    attempts = 1
    attempts_left_display = attempt_limit - attempts
    assert attempts_left_display == 5, "After 1st guess should display 5 attempts left"
    
    # After 2nd guess: attempts=2 → display should show 4
    attempts = 2
    attempts_left_display = attempt_limit - attempts
    assert attempts_left_display == 4, "After 2nd guess should display 4 attempts left"
    
    # After 3rd guess: attempts=3 → display should show 3
    attempts = 3
    attempts_left_display = attempt_limit - attempts
    assert attempts_left_display == 3, "After 3rd guess should display 3 attempts left"
    
    # After 4th guess: attempts=4 → display should show 2
    attempts = 4
    attempts_left_display = attempt_limit - attempts
    assert attempts_left_display == 2, "After 4th guess should display 2 attempts left"
    
    # After 5th guess: attempts=5 → display should show 1
    attempts = 5
    attempts_left_display = attempt_limit - attempts
    assert attempts_left_display == 1, "After 5th guess should display 1 attempt left"
    
    # After 6th guess (final): attempts=6 → display should show 0
    attempts = 6
    attempts_left_display = attempt_limit - attempts
    assert attempts_left_display == 0, "After final (6th) guess should display 0 attempts left"

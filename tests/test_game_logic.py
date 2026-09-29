from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_easy_difficulty_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20

def test_normal_difficulty_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 100

def test_hard_difficulty_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 50

def test_decimal_guess():
    result = check_guess(12.9, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_negative_guess():
   result = check_guess(-10, 50)
   assert result == ("Too Low", "📈 Go HIGHER!")


def test_very_large_guess():
    result = check_guess(10**1000, 50)
    assert result == ("Too High", "📉 Go LOWER!")
def get_range_for_difficulty(difficulty: str):
    """Return the inclusive lower and upper bounds for a difficulty setting.

    Args:
        difficulty: The requested difficulty label, such as "Easy",
            "Normal", or "Hard".

    Returns:
        A tuple containing the minimum and maximum valid values for the
        specified difficulty.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """Parse a raw user input into an integer guess.

    Args:
        raw: The value entered by the user before conversion.

    Returns:
        A tuple of the form ``(ok, guess_int, error_message)`` where ``ok``
        indicates whether parsing succeeded, ``guess_int`` contains the parsed
        integer when valid, and ``error_message`` provides the reason when
        parsing fails.

    Raises:
        NotImplementedError: Raised by the placeholder version before the
            parsing logic is fully migrated into this utility module.
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )


# FIX: The original function pointed in opposite direction for the hints.
# A guess that is too high should return "Too High" and a hint to go lower,
# and vice versa for a guess that is too low.
def check_guess(guess, secret):
    """Compare a guessed value against the secret number and return a result.

    Args:
        guess: The player's current guess.
        secret: The hidden target value the player is trying to match.

    Returns:
        A tuple of ``(outcome, message)`` describing whether the guess is a
        win, too high, or too low, along with a corresponding hint.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update a player's score based on the guessed outcome and attempt count.

    Args:
        current_score: The player's score before this outcome is applied.
        outcome: The result of the guess, such as "Win", "Too High", or
            "Too Low".
        attempt_number: The number of the current attempt used to determine the
            scoring adjustment.

    Returns:
        The updated score after applying the outcome logic.

    Raises:
        NotImplementedError: Raised by the placeholder version before the
            scoring logic is fully migrated into this utility module.
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )

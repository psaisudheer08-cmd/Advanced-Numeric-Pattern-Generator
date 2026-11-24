"""
settings.py - Project Configuration and Constants

This file holds all the central settings for our pattern generator.
Keeping limits, pattern names, and menu labels here ensures that our
program logic never relies on hard-coded values.
"""

# Minimum allowed pattern size
MIN_SIZE = 1

# Maximum allowed pattern size
MAX_SIZE = 20

# Display names for the available patterns
PATTERN_DIAMOND_NAME = "Hollow Numeric Diamond"
PATTERN_PYRAMID_NAME = "Symmetric Numeric Pyramid"

# Menu choices mapped to display labels
MENU_CHOICE_DIAMOND = "1"
MENU_CHOICE_PYRAMID = "2"
MENU_CHOICE_EXIT = "3"

MENU_OPTIONS = {
    MENU_CHOICE_DIAMOND: PATTERN_DIAMOND_NAME,
    MENU_CHOICE_PYRAMID: PATTERN_PYRAMID_NAME,
    MENU_CHOICE_EXIT: "Exit",
}

# Standard user prompts
PROMPT_MENU_CHOICE = "Enter your choice (1-3): "
PROMPT_RUN_AGAIN = "Generate another pattern? (y/n): "


def get_size_prompt() -> str:
    """
    Return the dynamic input prompt string for pattern size.

    This ensures that if MIN_SIZE or MAX_SIZE is modified in settings,
    the user prompt updates automatically.

    Returns:
        str: Prompt text showing the current allowed size range.
    """
    # Build prompt string using current MIN_SIZE and MAX_SIZE
    return f"Enter pattern size ({MIN_SIZE} to {MAX_SIZE}): "

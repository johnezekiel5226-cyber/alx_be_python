def safe_divide(numerator, denominator):
    try:
        # Try converting inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Try performing division
        try:
            result = num / den
            return f"Result: {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."

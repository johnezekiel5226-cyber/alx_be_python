# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion Functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

# User Interaction
def main():
    try:
        temperature_input = input("Enter the temperature value: ").strip()
        measurement = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Try to convert the temperature to float
        temperature = float(temperature_input)

        if measurement == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {round(converted, 2)}°F")
        elif measurement == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {round(converted, 2)}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        if "could not convert string to float" in str(e):
            print("Invalid temperature. Please enter a numeric value.")
        else:
            print(e)

if __name__ == "__main__":
    main()

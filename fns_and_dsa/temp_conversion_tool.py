# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_ADJUSTMENT = 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FAHRENHEIT_TO_CELSIUS_ADJUSTMENT
    celsius = (fahrenheit - FAHRENHEIT_TO_CELSIUS_ADJUSTMENT) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    global CELSIUS_TO_FAHRENHEIT_FACTOR, FAHRENHEIT_TO_CELSIUS_ADJUSTMENT
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + FAHRENHEIT_TO_CELSIUS_ADJUSTMENT
    return fahrenheit

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()


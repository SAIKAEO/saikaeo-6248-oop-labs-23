def convert_celsius_to_fahrenheit(temp_cel):
    temp_fah = (9/5) * temp_cel + 32
    return temp_fah

def main():
    while True:
        try:
            temp_cel = float(input("Enter a temperature in Celsius:"))
            temp_fah = convert_celsius_to_fahrenheit(temp_cel)
            print(f"{temp_cel:.2f} celsius is in {temp_fah:.2f}")
            break
        except ValueError:
            print("Please enter a valid floating point for the temperture.")

if __name__ == "__main__":
    main()

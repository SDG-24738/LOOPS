class RomanConverter:
    def int_to_roman(self, num):
        if not (1 <= num <= 3999):
            return "Input integer must be between 1 and 3999"
        val = [
            1000, 900, 500, 400, 
            100, 90, 50, 40, 
            10, 9, 5, 4, 
            1
        ]
        syb = [
            "M", "CM", "D", "CD", 
            "C", "XC", "L", "XL", 
            "X", "IX", "V", "IV", 
            "I"
        ]
        roman_numeral = ""
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_numeral += syb[i]
                num -= val[i]
            i += 1
        return roman_numeral
converter = RomanConverter()
try:
    user_input = int(input("Enter an integer (1 - 3999): "))
    roman_value = converter.int_to_roman(user_input)
    print(f"The Roman numeral equivalent is: {roman_value}")
except ValueError:
    print("Invalid input. Please enter an integer.")
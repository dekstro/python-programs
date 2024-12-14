def number_to_words(num):
    if num == 0:
        return "zero"

    def one(num):
        switcher = {
            1: "one", 2: "two", 3: "three", 4: "four",
            5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
        }
        return switcher.get(num, "")

    def two_less_20(num):
        switcher = {
            10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
            15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
        }
        return switcher.get(num, "")

    def ten(num):
        switcher = {
            2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
            6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
        }
        return switcher.get(num, "")

    def two(num):
        if not num:
            return ""
        elif num < 10:
            return one(num)
        elif num < 20:
            return two_less_20(num)
        else:
            tens = num // 10
            rest = num % 10
            return ten(tens) + (" " + one(rest) if rest else "")

    def three(num):
        hundred = num // 100
        rest = num % 100
        if hundred and rest:
            return one(hundred) + " hundred " + two(rest)
        elif not hundred and rest:
            return two(rest)
        elif hundred and not rest:
            return one(hundred) + " hundred"

    billion = num // 1000000000
    million = (num - billion * 1000000000) // 1000000
    thousand = (num - billion * 1000000000 - million * 1000000) // 1000
    remainder = num - billion * 1000000000 - million * 1000000 - thousand * 1000

    result = ""
    if billion:
        result += three(billion) + " billion "
    if million:
        result += three(million) + " million "
    if thousand:
        result += three(thousand) + " thousand "
    if remainder:
        result += three(remainder)

    return result.strip()

# Example usage
number = int(input('Enter number: '))
print(number_to_words(number))  # Output: "five thousand one hundred twenty four"

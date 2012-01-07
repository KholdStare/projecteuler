#!/usr/bin/python
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../utils")

import bigops

englishDigits = [ "",
                  "one",
                  "two",
                  "three",
                  "four",
                  "five",
                  "six",
                  "seven",
                  "eight",
                  "nine",
                  "ten",
                  "eleven",
                  "twelve",
                  "thirteen",
                  "fourteen",
                  "fifteen",
                  "sixteen",
                  "seventeen",
                  "eighteen",
                  "nineteen"]

englishTens = [ "",
                "ten",
                "twenty",
                "thirty",
                "forty",
                "fifty",
                "sixty",
                "seventy",
                "eighty",
                "ninety" ]

englishPowers = [ "",
                  "thousand",
                  "million",
                  "billion" ]

def thousand_int_to_english(num):
    "Given a number mod 1000, converts to English representation."""
    num %= 1000
    
    tensOutput = ""
    tens = num%100
    if tens < 20:
        tensOutput = englishDigits[tens]
    elif tens >= 20:
        tensOutput = englishTens[tens//10] + " " + englishDigits[tens%10] + " "


    hundredsOutput = ""
    hundredDigit = num//100
    if hundredDigit:
        hundredsOutput = englishDigits[num//100] + " hundred "
        if tens:
            hundredsOutput += "and "

    return hundredsOutput + tensOutput

def int_to_english(num):
    # take number in chunks of thousands
    if num == 0:
        return "zero"

    output = ""
    thousandPower = 0
    while num > 0:
        chunk = num % 1000
        num = num // 1000
        if chunk > 0:
            output = thousand_int_to_english(chunk) + englishPowers[thousandPower] + " " + output
            if chunk < 100 and num > 0:
                output = "and " + output

        thousandPower += 1

    return output.strip(' ')


def main (maxNum):
    totalLength = 0
    for num in xrange(1, maxNum+1):
        totalLength += len(int_to_english(num).replace(" ", ""))

    return totalLength


if __name__ == "__main__":
    print main(1000)

# Program to find the Maximum & Minimum Numbers From the Specified Decimal Numbers

import decimal
data=list(map(decimal,'2.25,3.78,5.25,7.03,9.07,11.72'.split()))
print("Maximum Is : ",max(data))
print("Minimum Is : ",min(data))
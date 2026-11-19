# MODULE 2 - MINI PROJECT
# OTP Generator

import secrets

digits = int(input("Enter OTP length (4 to 8): "))

if 4 <= digits <= 8:
    lower = 10 ** (digits - 1)
    upper = (10 ** digits) - 1
    otp = secrets.randbelow(upper - lower + 1) + lower

    print("Your One-Time Password (OTP) is:", otp)
    print("Do not share your OTP with anyone.")
else:
    print("Please enter a length between 4 and 8.")


# SAMPLE INPUT
# Enter OTP length (4 to 8): 6
#
# SAMPLE OUTPUT (example only)
# Your One-Time Password (OTP) is: 583104
# Do not share your OTP with anyone.
#
# Note: OTP is generated securely and will be different each run.

def validate_cnp(func):
    def wrapper(cnp):
        try:

            if len(cnp) != 13:
                raise ValueError("Invalid CNP format. It should contain 13 digits.")
        except ValueError as error:
                print(error)

        return func(cnp)

    return wrapper

def validate_cnp_constant(func):
    def wrapper(cnp):
        numeric_code = [int(x) for x in cnp]
        constant = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
        total = sum(numeric_code * constant for numeric_code, constant in zip(numeric_code[:12], constant)) % 11
        expected_sum = 1 if total == 10 else total
        try:
            if numeric_code [12] != expected_sum:
                raise ValueError("CNP sum invalid")
        except ValueError as error:
                print(error)

        return func(cnp)
    return wrapper

@validate_cnp
@validate_cnp_constant
def interpret_cnp(cnp):
    gender_digit = int(cnp[0])
    year = int(cnp[1:3])
    month = int(cnp[3:5])
    day = int(cnp[5:7])
    country_code = int(cnp[7:9])

    gender = "Male" if gender_digit in [1, 3, 5, 7] else "Female"

    country = {34: "SB", 12: "B", 56: "SV"}

    def get_country(country_code, country):
        country_keys = country.keys()

        if country_code in country_keys:
            return (country[country_code])


    if gender_digit in [1, 2, 7, 8]:
        year += 1900
    elif gender_digit in [3, 4, 5, 6]:
        year += 1800
    elif gender_digit in [9]:
        year += 2000



    interpretation = {
        "Gender": gender,
        "Birthdate": f"{year}-{month:02d}-{day:02d}",
        "Country Code": get_country(country_code, country),
    }

    return interpretation

try:
    ro_cnp = "1980318347834"
    result = interpret_cnp(ro_cnp)
    print(result)
except Exception:
    print("Error CNP")


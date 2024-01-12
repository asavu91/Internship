def validate_cnp(func):
    def wrapper(cnp):
        if len(cnp) != 13:
            return ("Invalid CNP format. It should contain 13 digits.")

        return func(cnp)

    return wrapper


@validate_cnp
def interpret_cnp(cnp):
    gender_digit = int(cnp[0])
    year = int(cnp[1:3])
    month = int(cnp[3:5])
    day = int(cnp[5:7])
    country_code = int(cnp[7:9])

    gender = "Male" if gender_digit in [1, 3, 5, 7] else "Female"

    country = {23: "SB", 12: "B", 56: "SV"}

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


ro_cnp = "1890101234567"
result = interpret_cnp(ro_cnp)
print(result)

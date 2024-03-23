from datetime import datetime, timedelta

# Functie om een lijst van datums in datetime formaat te genereren
def generate_dates(start_date, end_date):
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += timedelta(days=1)
    return dates

# Startdatum en einddatum voor januari 2024
start_date_januari = datetime(2024, 1, 1)
end_date_januari = datetime(2024, 1, 31)

# Startdatum en einddatum voor februari 2024
start_date_februari = datetime(2024, 2, 1)
end_date_februari = datetime(2024, 2, 29)

# Startdatum en einddatum voor maart 2024
start_date_maart = datetime(2024, 3, 1)
end_date_maart = datetime(2024, 3, 31)

# Genereer lijsten van datums in datetime formaat
januari_2024_dates = generate_dates(start_date_januari, end_date_januari)
februari_2024_dates = generate_dates(start_date_februari, end_date_februari)
maart_2024_dates = generate_dates(start_date_maart, end_date_maart)

print("Januari 2024:", januari_2024_dates)
print("Februari 2024:", februari_2024_dates)
print("Maart 2024:", maart_2024_dates)
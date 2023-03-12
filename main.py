import ru_local as ru
V_gallon = float(input())

V_liter = V_gallon * 3.785

barrel = int(V_gallon/19.5) + 1

CO2 = V_gallon * 20

energygl = V_gallon * 115000
ethanol = energygl / 75700

price = V_gallon * 3

print(V_liter, ru.liters)
print(barrel, ru.barrels)
print(CO2, ru.pounds, ru.carbon_dioxide)
print(ethanol, ru.gallons, ru.ethanol)
print(price, ru.dollars)

V_liter_people_day = 3.3
nsk_population = 1567000
V_liter_nsk_day = nsk_population * V_liter_people_day
price_nsk = (V_liter_nsk_day/0.26) * 3
print(int(price_nsk), ru.dollars, ru.per_day)

ru_population = 143000000
V_liter_ru_day = ru_population * V_liter_people_day
V_liter_ru_year = V_liter_ru_day * 365
price_ru = (V_liter_ru_year/0.26) * 3
print(int(price_ru), ru.dollars, ru.per_year)

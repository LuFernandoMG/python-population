import csv
import matplotlib.pyplot as plt


def loadCountriesPie():
  with open("./data.csv", 'r') as file:
    next(file)
    csvreaded = csv.reader(file)
    countries = dict()
    for row in csvreaded:
      country = {
        row[2]: int(float(row[16]) * 100)
      }
      countries.update(country)
    return countries


def loadCountries():
  with open("./data.csv", 'r') as file:
    next(file)
    csvreaded = csv.reader(file)
    countries = dict()
    for row in csvreaded:
      country = {
        row[2]: {
          "2022": int(row[5]),
          "2020": int(row[6]),
          "2015": int(row[7]),
          "2010": int(row[8]),
          "2000": int(row[9]),
          "1990": int(row[10]),
          "1980": int(row[11])
        }
      }
      countries.update(country)
    return countries


def getCountry():
  countrySelected = input('Please, type a country ').capitalize()
  return countrySelected


def generate_pie_chart(labels, values):
  print(labels)
  print(values)
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  plt.show()


def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()


def runChart(countrySelected, countries):
  if countrySelected in countries:
    countryDict = countries[countrySelected]
    generate_bar_chart(countryDict.keys(), countryDict.values())
  else:
    print('This country does not exist')
    getCountry()


if __name__ == '__main__':
  countries = loadCountriesPie()
  generate_pie_chart(countries.keys(), countries.values())
  # countries = loadCountries()
  # countrySelected = getCountry()
  # runChart(countrySelected, countries)

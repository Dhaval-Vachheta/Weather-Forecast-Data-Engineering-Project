##################################################################
# Libraries
##################################################################
import random
import json
from datetime import datetime, timedelta

##################################################################
# Data Dictionary of state & citites
##################################################################
states_cities = {
    # States & Capitals
    'Andhra Pradesh':'Amaravati',
    'Arunachal Pradesh':'Itanagar',
    'Assam':'Dispur',
    'Bihar':'Patna',
    'Chhattisgarh':'Raipur',
    'Goa':'Panaji',
    'Gujarat':'Gandhinagar',
    'Haryana':'Chandigarh',
    'Himachal Pradesh':'Shimla',
    'Jharkhand':'Ranchi',
    'Karnataka':'Bengaluru',
    'Kerala':'Thiruvananthapuram',
    'Madhya Pradesh':'Bhopal',
    'Maharashtra':'Mumbai',
    'Manipur':'Imphal',
    'Meghalaya':'Shillong',
    'Mizoram':'Aizawl',
    'Nagaland':'Kohima',
    'Odisha':'Bhubaneswar',
    'Punjab':'Chandigarh',
    'Rajasthan':'Jaipur',
    'Sikkim':'Gangtok',
    'Tamil Nadu':'Chennai',
    'Telangana':'Hyderabad',
    'Tripura':'Agartala',
    'Uttar Pradesh':'Lucknow',
    'Uttarakhand':'Dehradun (Winter), Gairsain (Summer)',
    'West Bengal':'Kolkata',
    # Union Territory & Capitals
    'Andaman and Nicobar Islands':'Port Blair',
    'Dadra and Nagar Haveli and Daman and Diu':'Daman',
    'Delhi (National Capital Territory)':'New Delhi',
    'Jammu and Kashmir':'Srinagar (Summer), Jammu (Winter)',
    'Ladakh':'Leh',
    'Lakshadweep':'Kavaratti',
    'Puducherry':'Puducherry'
}

# Display Data
# print(states_cities)

##################################################################
# Random Date Generation
##################################################################
# One-liner function to generate a random date
generate_random_date = lambda start_str, end_str: (datetime.strptime(start_str, "%d-%m-%Y").date() + timedelta(days=random.randrange((datetime.strptime(end_str, "%d-%m-%Y").date() - datetime.strptime(start_str, "%d-%m-%Y").date()).days + 1))).strftime("%d-%m-%Y")

# Winter Dates
winter_start_date = "01-11-2023"
winter_end_date = "29-02-2024"

# Summer Dates
summer_start_date = "01-03-2024"
summer_end_date = "30-06-2024"

# Monsoon Dates
monsoon_start_date = "01-07-2024"
monsoon_end_date = "31-10-2024"

##################################################################
# Weather Data Creation Function
##################################################################
def WeatherData(states_cities):
    # Wind Direction
    wind_direction = ['N','E','S','W','NE','NW','SE','SW']

    # Precipitation
    winter_precipitation = ['Rain: 0 mm']
    summer_precipitation = ['Rain: 0 mm']
    monsoon_precipitation = ['Rain: 0 mm','Rain: 2 mm','Rain: 5 mm','Rain: 20 mm','Rain: 200 mm','Rain: 250 mm','Rain: 300']

    # Weather Condition
    winter_weather_condition = ['Clear','Sunny','Partly Cloudy']
    summer_weather_condition = ['Clear','Sunny','Partly Cloudy']
    monsoon_weather_condition = ['Cloudy','Heavy Rain','Overcast Rain','Partly Cloudy','Rainy']

    # Fog or Haze
    fog_haze = ['Yes','No']

    # Generating Weather Dataset
    for state in states_cities:
        if state == 'Andhra Pradesh':
            # Andhra Pradesh Temperatures
            winter_temperature = random.randint(19,24)
            summer_temperature = random.randint(36,41)
            monsoon_temperature = random.randint(25,35)

            # Andhra Pradesh all 3 seasons data dictionary
            AndhraPradesh = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(10,20),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1010,1020),
                    'Visibility':random.randint(10,20),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Andhra Pradesh',
                    'City':'Amaravati',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(10,20),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1005,1010),
                    'Visibility':random.randint(10,20),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(8,10),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Andhra Pradesh',
                    'City':'Amaravati',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(60,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(10,20),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1001,1005),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(70,90),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Andhra Pradesh',
                    'City':'Amaravati',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(80,100)
                }
            }
    
    # Display City Data
    print(AndhraPradesh)

# Calling WeatherData Function
WeatherData(states_cities)
##################################################################
# Libraries
##################################################################
import random
import json
from datetime import datetime, timedelta

##################################################################
# Data Dictionary of state & citites
##################################################################
states_cities = {
    # States & Capitals
    'Andhra Pradesh':'Amaravati',
    'Arunachal Pradesh':'Itanagar',
    'Assam':'Dispur',
    'Bihar':'Patna',
    'Chhattisgarh':'Raipur',
    'Goa':'Panaji',
    'Gujarat':'Gandhinagar',
    'Haryana':'Chandigarh',
    'Himachal Pradesh':'Shimla',
    'Jharkhand':'Ranchi',
    'Karnataka':'Bengaluru',
    'Kerala':'Thiruvananthapuram',
    'Madhya Pradesh':'Bhopal',
    'Maharashtra':'Mumbai',
    'Manipur':'Imphal',
    'Meghalaya':'Shillong',
    'Mizoram':'Aizawl',
    'Nagaland':'Kohima',
    'Odisha':'Bhubaneswar',
    'Punjab':'Chandigarh',
    'Rajasthan':'Jaipur',
    'Sikkim':'Gangtok',
    'Tamil Nadu':'Chennai',
    'Telangana':'Hyderabad',
    'Tripura':'Agartala',
    'Uttar Pradesh':'Lucknow',
    'Uttarakhand':'Dehradun (Winter), Gairsain (Summer)',
    'West Bengal':'Kolkata',
    # Union Territory & Capitals
    'Andaman and Nicobar Islands':'Port Blair',
    'Dadra and Nagar Haveli and Daman and Diu':'Daman',
    'Delhi (National Capital Territory)':'New Delhi',
    'Jammu and Kashmir':'Srinagar (Summer), Jammu (Winter)',
    'Ladakh':'Leh',
    'Lakshadweep':'Kavaratti',
    'Puducherry':'Puducherry'
}

# Display Data
# print(states_cities)

##################################################################
# Random Date Generation
##################################################################
# One-liner function to generate a random date
generate_random_date = lambda start_str, end_str: (datetime.strptime(start_str, "%d-%m-%Y").date() + timedelta(days=random.randrange((datetime.strptime(end_str, "%d-%m-%Y").date() - datetime.strptime(start_str, "%d-%m-%Y").date()).days + 1))).strftime("%d-%m-%Y")

# Winter Dates
winter_start_date = "01-11-2023"
winter_end_date = "29-02-2024"

# Summer Dates
summer_start_date = "01-03-2024"
summer_end_date = "30-06-2024"

# Monsoon Dates
monsoon_start_date = "01-07-2024"
monsoon_end_date = "31-10-2024"

##################################################################
# Weather Data Creation Function
##################################################################
def WeatherData(states_cities):
    # Wind Direction
    wind_direction = ['N','E','S','W','NE','NW','SE','SW']

    # Precipitation
    winter_precipitation = ['Rain: 0 mm']
    summer_precipitation = ['Rain: 0 mm']
    monsoon_precipitation = ['Rain: 0 mm','Rain: 2 mm','Rain: 5 mm','Rain: 20 mm','Rain: 200 mm','Rain: 250 mm','Rain: 300']

    # Weather Condition
    winter_weather_condition = ['Clear','Sunny','Partly Cloudy']
    summer_weather_condition = ['Clear','Sunny','Partly Cloudy']
    monsoon_weather_condition = ['Cloudy','Heavy Rain','Overcast Rain','Partly Cloudy','Rainy']

    # Fog or Haze
    fog_haze = ['Yes','No']

    # Generating Weather Dataset
    for state in states_cities:
        if state == 'Andhra Pradesh':
            # Andhra Pradesh Temperatures
            winter_temperature = random.randint(19,24)
            summer_temperature = random.randint(36,41)
            monsoon_temperature = random.randint(25,35)

            # Andhra Pradesh all 3 seasons data dictionary
            AndhraPradesh = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(10,20),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1010,1020),
                    'Visibility':random.randint(10,20),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Andhra Pradesh',
                    'City':'Amaravati',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(10,20),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1005,1010),
                    'Visibility':random.randint(10,20),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(8,10),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Andhra Pradesh',
                    'City':'Amaravati',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(60,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(10,20),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1001,1005),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(70,90),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Andhra Pradesh',
                    'City':'Amaravati',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(80,100)
                }
            }
    
    # Display City Data
    print(AndhraPradesh)

# Calling WeatherData Function
WeatherData(states_cities)
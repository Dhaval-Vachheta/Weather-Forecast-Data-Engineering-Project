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
        elif state == 'Arunachal Pradesh':
			# Arunachal Pradesh Temperatures
            winter_temperature = random.randint(13,18)
            summer_temperature = random.randint(28,33)
            monsoon_temperature = random.randint(19,29)

            # Arunachal Pradesh all 3 seasons data dictionary
            ArunachalPradesh = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(2,10),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(12,18),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(300,500),
                    'State':'Arunachal Pradesh',
                    'City':'Itanagar',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(60,80)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(70,80),
                    'WindSpeed':random.randint(2,10),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,10),
                    'CloudCover':random.randint(50,70),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(400,600),
                    'State':'Arunachal Pradesh',
                    'City':'Itanagar',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,90)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(90,100),
                    'WindSpeed':random.randint(2,10),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,10),
                    'CloudCover':random.randint(50,70),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(50,150),
                    'State':'Arunachal Pradesh',
                    'City':'Itanagar',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(100,120)
                }
            }
        elif state == 'Assam':
                    # Assam Temperatures
                winter_temperature = random.randint(15,20)
                summer_temperature = random.randint(33,38)
                monsoon_temperature = random.randint(23,33)
        
                # Assam all 3 seasons data dictionary
                Assam = {
                    'Winter': {
                        'Datetime':generate_random_date(winter_start_date, winter_end_date),
                        'Temperature':winter_temperature,
                        'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                        'Humidity':random.randint(65,75),
                        'WindSpeed':random.randint(5,15),
                        'WindDirection':random.choice(wind_direction),
                        'Precipitation':random.choice(winter_precipitation),
                        'Pressure':random.randint(1005,1015),
                        'Visibility':random.randint(12,18),
                        'CloudCover':random.randint(5,15),
                        'UVIndex':random.randint(3,5),
                        'WeatherCondition':random.choice(winter_weather_condition),
                        'SnowDepth':random.randint(0,0),
                        'SolarRadiation':random.randint(350,550),
                        'State':'Assam',
                        'City':'Dispur',
                        'FogorHaze':random.choice(fog_haze),
                        'AirQuality':random.randint(40,60)
                    },
                    'Summer': {
                        'Datetime':generate_random_date(summer_start_date, summer_end_date),
                        'Temperature':summer_temperature,
                        'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                        'Humidity':random.randint(70,90),
                        'WindSpeed':random.randint(5,15),
                        'WindDirection':random.choice(wind_direction),
                        'Precipitation':random.choice(summer_precipitation),
                        'Pressure':random.randint(1005,1015),
                        'Visibility':random.randint(5,10),
                        'CloudCover':random.randint(25,35),
                        'UVIndex':random.randint(8,10),
                        'WeatherCondition':random.choice(summer_weather_condition),
                        'SnowDepth':random.randint(0,0),
                        'SolarRadiation':random.randint(550,750),
                        'State':'Assam',
                        'City':'Dispur',
                        'FogorHaze':random.choice(fog_haze),
                        'AirQuality':random.randint(50,70)
                    },
                    'Monsoon': {
                        'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                        'Temperature':monsoon_temperature,
                        'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                        'Humidity':random.randint(80,100),
                        'WindSpeed':random.randint(5,15),
                        'WindDirection':random.choice(wind_direction),
                        'Precipitation':random.choice(monsoon_precipitation),
                        'Pressure':random.randint(1005,1015),
                        'Visibility':random.randint(2,8),
                        'CloudCover':random.randint(80,90),
                        'UVIndex':random.randint(3,5),
                        'WeatherCondition':random.choice(monsoon_weather_condition),
                        'SnowDepth':random.randint(0,0),
                        'SolarRadiation':random.randint(100,300),
                        'State':'Assam',
                        'City':'Dispur',
                        'FogorHaze':random.choice(fog_haze),
                        'AirQuality':random.randint(90,110)
                    }
                }
        elif state == 'Bihar':
            # Bihar Temperatures
            winter_temperature = random.randint(13,18)
            summer_temperature = random.randint(38,43)
            monsoon_temperature = random.randint(25,25)

            # Bihar all 3 seasons data dictionary
            Bihar = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1010,1020),
                    'Visibility':random.randint(10,20),
                    'CloudCover':random.randint(5,15),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(400,600),
                    'State':'Bihar',
                    'City':'Patna',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(50,70)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(10,20),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1001,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(25,35),
                    'UVIndex':random.randint(8,10),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(650,850),
                    'State':'Bihar',
                    'City':'Patna',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(80,90)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(85,95),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(250,450),
                    'State':'Bihar',
                    'City':'Patna',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Chhattisgarh':
            # Chhattisgarh Temperatures
            winter_temperature = random.randint(17,22)
            summer_temperature = random.randint(40,45)
            monsoon_temperature = random.randint(25,35)

            # Chhattisgarh all 3 seasons data dictionary
            Chhattisgarh = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(60,70),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1010,1020),
                    'Visibility':random.randint(10,20),
                    'CloudCover':random.randint(10,20),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(450,650),
                    'State':'Chhattisgarh',
                    'City':'Raipur',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(60,80)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(50,60),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1001,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(8,10),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(700,900),
                    'State':'Chhattisgarh',
                    'City':'Raipur',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(80,100)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(90,100),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,10),
                    'CloudCover':random.randint(85,95),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(50,250),
                    'State':'Chhattisgarh',
                    'City':'Raipur',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(110,130)
                }
            }
        elif state == 'Goa':
            # Goa Temperatures
            winter_temperature = random.randint(21,26)
            summer_temperature = random.randint(34,39)
            monsoon_temperature = random.randint(23,33)

            # Goa all 3 seasons data dictionary
            Goa = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(10,20),
                    'CloudCover':random.randint(5,15),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Goa',
                    'City':'Panaji',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(50,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(75,85),
                    'WindSpeed':random.randint(15,25),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(55,65),
                    'UVIndex':random.randint(8,10),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(550,750),
                    'State':'Goa',
                    'City':'Panaji',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(60,70)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(90,100),
                    'WindSpeed':random.randint(10,20),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,10),
                    'CloudCover':random.randint(90,100),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(50,250),
                    'State':'Goa',
                    'City':'Panaji',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(100,120)
                }
            }
        elif state == 'Gujarat':
            # Gujarat Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Gujarat all 3 seasons data dictionary
            Gujarat = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,10),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Gujarat',
                    'City':'Gandhinagar',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(8,10),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Gujarat',
                    'City':'Gandhinagar',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(70,90),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Gujarat',
                    'City':'Gandhinagar',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Haryana':
            # Haryana Temperatures
            winter_temperature = random.randint(13,18)
            summer_temperature = random.randint(33,40)
            monsoon_temperature = random.randint(27,40)

            # Haryana all 3 seasons data dictionary
            Haryana = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(70,80),
                    'WindSpeed':random.randint(15,25),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1020,1035),
                    'Visibility':random.randint(5,10),
                    'CloudCover':random.randint(5,15),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(100,200),
                    'State':'Haryana',
                    'City':'Chandigarh',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(60,70)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(15,25),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1005),
                    'Visibility':random.randint(15,25),
                    'CloudCover':random.randint(45,55),
                    'UVIndex':random.randint(8,10),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(550,750),
                    'State':'Haryana',
                    'City':'Chandigarh',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(50,70)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(20,30),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1010,1025),
                    'Visibility':random.randint(5,10),
                    'CloudCover':random.randint(80,90),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(100,200),
                    'State':'Haryana',
                    'City':'Chandigarh',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(80,100)
                }
            }
        elif state == 'Himachal Pradesh':
            # Himachal Pradesh Temperatures
            winter_temperature = random.randint(12,18)
            summer_temperature = random.randint(34,42)
            monsoon_temperature = random.randint(15,35)

            # Himachal Pradesh all 3 seasons data dictionary
            HimachalPradesh = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(75,85),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1015,1025),
                    'Visibility':random.randint(5,10),
                    'CloudCover':random.randint(5,15),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(150,250),
                    'State':'Himachal Pradesh',
                    'City':'Shimla',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(60,75)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(25,45),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1010,1015),
                    'Visibility':random.randint(15,25),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(8,10),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Himachal Pradesh',
                    'City':'Shimla',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(60,70)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(25,35),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1000,1015),
                    'Visibility':random.randint(10,15),
                    'CloudCover':random.randint(85,90),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(250,350),
                    'State':'Himachal Pradesh',
                    'City':'Shimla',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(85,110)
                }
            }
        elif state == 'Jharkhand':
            # Jharkhand Temperatures
            winter_temperature = random.randint(16,24)
            summer_temperature = random.randint(36,45)
            monsoon_temperature = random.randint(25,35)

            # Jharkhand all 3 seasons data dictionary
            Jharkhand = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Jharkhand',
                    'City':'Ranchi',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(30,50),
                    'UVIndex':random.randint(8,10),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Jharkhand',
                    'City':'Ranchi',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,10),
                    'CloudCover':random.randint(70,90),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Jharkhand',
                    'City':'Ranchi',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Karnataka':
            # Karnataka Temperatures
            winter_temperature = random.randint(18,30)
            summer_temperature = random.randint(35,45)
            monsoon_temperature = random.randint(25,35)

            # Karnataka all 3 seasons data dictionary
            Karnataka = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(60,70),
                    'WindSpeed':random.randint(15,25),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1015,1025),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,30),
                    'UVIndex':random.randint(3,8),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(400,600),
                    'State':'Karnataka',
                    'City':'Bengaluru',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(30,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(45,65),
                    'WindSpeed':random.randint(15,25),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1020,1040),
                    'Visibility':random.randint(7,14),
                    'CloudCover':random.randint(30,45),
                    'UVIndex':random.randint(8,10),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(350,550),
                    'State':'Karnataka',
                    'City':'Bengaluru',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(75,85)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(75,90),
                    'WindSpeed':random.randint(4,21),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1010,1020),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(80,90),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(100,400),
                    'State':'Karnataka',
                    'City':'Bengaluru',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(80,110)
                }
            }
        elif state == 'Kerala':
            # Kerala Temperatures
            winter_temperature = random.randint(18,27)
            summer_temperature = random.randint(35,45)
            monsoon_temperature = random.randint(25,35)

            # Kerala all 3 seasons data dictionary
            Kerala = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(55,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1015,1025),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(4,6),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(400,600),
                    'State':'Kerala',
                    'City':'Thiruvananthapuram',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(50,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1015),
                    'Visibility':random.randint(5,25),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Kerala',
                    'City':'Thiruvananthapuram',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Kerala',
                    'City':'Thiruvananthapuram',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Madhya Pradesh':
            # Madhya Pradesh
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Madhya Pradesh all 3 seasons data dictionary
            MadhyaPradesh = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Madhya Pradesh',
                    'City':'Bhopal',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Madhya Pradesh',
                    'City':'Bhopal',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Madhya Pradesh',
                    'City':'Bhopal',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Maharashtra':
            # Kerala Temperatures
            winter_temperature = random.randint(18,28)
            summer_temperature = random.randint(37,47)
            monsoon_temperature = random.randint(25,45)

            # Maharashtra all 3 seasons data dictionary
            Maharashtra = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(75,85),
                    'WindSpeed':random.randint(15,25),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1015,1025),
                    'Visibility':random.randint(15,25),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Maharashtra',
                    'City':'Mumbai',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Maharashtra',
                    'City':'Mumbai',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(80,100)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Maharashtra',
                    'City':'Mumbai',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Manipur':
            # Manipur Temperatures
            winter_temperature = random.randint(13,25)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(24,35)

            # Manipur all 3 seasons data dictionary
            Manipur = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Manipur',
                    'City':'Imphal',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1020),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,8),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(100,200),
                    'State':'Manipur',
                    'City':'Imphal',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(70,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Manipur',
                    'City':'Imphal',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(80,110)
                }
            }
        elif state == 'Meghalaya':
            # Meghalaya Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Meghalaya all 3 seasons data dictionary
            Meghalaya = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(60,70),
                    'WindSpeed':random.randint(15,25),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1000,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(25,35),
                    'UVIndex':random.randint(3,8),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Meghalaya',
                    'City':'Shillong',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,70)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Meghalaya',
                    'City':'Shillong',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Meghalaya',
                    'City':'Shillong',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Mizoram':
            # Mizoram Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Mizoram all 3 seasons data dictionary
            Mizoram = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Mizoram',
                    'City':'Aizawl',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Mizoram',
                    'City':'Aizawl',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Mizoram',
                    'City':'Aizawl',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Nagaland':
            # Nagaland Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Nagaland all 3 seasons data dictionary
            Nagaland = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Nagaland',
                    'City':'Kohima',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Nagaland',
                    'City':'Kohima',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Nagaland',
                    'City':'Kohima',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Odisha':
            # Odisha Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Odisha all 3 seasons data dictionary
            Odisha = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Odisha',
                    'City':'Bhubaneswar',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Odisha',
                    'City':'Bhubaneswar',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Odisha',
                    'City':'Bhubaneswar',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Punjab':
            # Punjab Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Punjab all 3 seasons data dictionary
            Punjab = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Punjab',
                    'City':'Chandigarh',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Punjab',
                    'City':'Chandigarh',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Punjab',
                    'City':'Chandigarh',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Rajasthan':
            # Rajasthan Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Rajasthan all 3 seasons data dictionary
            Rajasthan = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Rajasthan',
                    'City':'Jaipur',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Rajasthan',
                    'City':'Jaipur',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Rajasthan',
                    'City':'Jaipur',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Sikkim':
            # Sikkim Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Sikkim all 3 seasons data dictionary
            Sikkim = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Sikkim',
                    'City':'Gangtok',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Sikkim',
                    'City':'Gangtok',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Sikkim',
                    'City':'Gangtok',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Tamil Nadu':
            # Tamil Nadu Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Tamil Nadu all 3 seasons data dictionary
            TamilNadu = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Tamil Nadu',
                    'City':'Chennai',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Tamil Nadu',
                    'City':'Chennai',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Tamil Nadu',
                    'City':'Chennai',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Telangana':
            # Telangana Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Telangana all 3 seasons data dictionary
            Telangana = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Telangana',
                    'City':'Hyderabad',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Telangana',
                    'City':'Hyderabad',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Telangana',
                    'City':'Hyderabad',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Tripura':
            # Tripura Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Tripura all 3 seasons data dictionary
            Tripura = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Tripura',
                    'City':'Agartala',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Tripura',
                    'City':'Agartala',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Tripura',
                    'City':'Agartala',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Uttar Pradesh':
            # Kerala Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Uttar Pradesh all 3 seasons data dictionary
            UttarPradesh = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Uttar Pradesh',
                    'City':'Lucknow',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Uttar Pradesh',
                    'City':'Lucknow',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Uttar Pradesh',
                    'City':'Lucknow',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Uttarakhand':
            # Uttarakhand Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Uttarakhand all 3 seasons data dictionary
            Uttarakhand = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Uttarakhand',
                    'City':'Dehradun (Winter), Gairsain (Summer)',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Uttarakhand',
                    'City':'Dehradun (Winter), Gairsain (Summer)',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Uttarakhand',
                    'City':'Dehradun (Winter), Gairsain (Summer)',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'West Bengal':
            # West Bengal Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # West Bengal all 3 seasons data dictionary
            WestBengal = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'West Bengal',
                    'City':'Kolkata',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'West Bengal',
                    'City':'Kolkata',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'West Bengal',
                    'City':'Kolkata',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Andaman and Nicobar Islands':
            # Andaman and Nicobar Islands Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Andaman and Nicobar Islands all 3 seasons data dictionary
            Kerala = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Andaman and Nicobar Islands',
                    'City':'Port Blair',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Andaman and Nicobar Islands',
                    'City':'Port Blair',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Andaman and Nicobar Islands',
                    'City':'Port Blair',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Dadra and Nagar Haveli and Daman and Diu':
            # Dadra and Nagar Haveli and Daman and Diu Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Dadra and Nagar Haveli and Daman and Diu all 3 seasons data dictionary
            DadraNagarHaveli_DamanDiu = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Dadra and Nagar Haveli and Daman and Diu',
                    'City':'Daman',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Dadra and Nagar Haveli and Daman and Diu',
                    'City':'Daman',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Dadra and Nagar Haveli and Daman and Diu',
                    'City':'Daman',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Delhi (National Capital Territory)':
            # Delhi (National Capital Territory) Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Delhi (National Capital Territory) all 3 seasons data dictionary
            Delhi = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Delhi (National Capital Territory)',
                    'City':'New Delhi',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Delhi (National Capital Territory)',
                    'City':'New Delhi',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Delhi (National Capital Territory)',
                    'City':'New Delhi',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Jammu and Kashmir':
            # Jammu and Kashmir Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Jammu and Kashmir all 3 seasons data dictionary
            JammuKashmir = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Jammu and Kashmir',
                    'City':'Srinagar (Summer), Jammu (Winter)',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Jammu and Kashmir',
                    'City':'Srinagar (Summer), Jammu (Winter)',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Jammu and Kashmir',
                    'City':'Srinagar (Summer), Jammu (Winter)',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Ladakh':
            # Ladakh Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Ladakh all 3 seasons data dictionary
            Ladakh = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Ladakh',
                    'City':'Leh',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Ladakh',
                    'City':'Leh',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Ladakh',
                    'City':'Leh',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Lakshadweep':
            # Lakshadweep Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Lakshadweep all 3 seasons data dictionary
            Lakshadweep = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Lakshadweep',
                    'City':'Kavaratti',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Lakshadweep',
                    'City':'Kavaratti',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Lakshadweep',
                    'City':'Kavaratti',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        elif state == 'Puducherry':
            # Puducherry Temperatures
            winter_temperature = random.randint(15,20)
            summer_temperature = random.randint(35,40)
            monsoon_temperature = random.randint(25,35)

            # Puducherry all 3 seasons data dictionary
            Puducherry = {
                'Winter': {
                    'Datetime':generate_random_date(winter_start_date, winter_end_date),
                    'Temperature':winter_temperature,
                    'DewPoint':random.randint(winter_temperature - 5, winter_temperature),
                    'Humidity':random.randint(65,75),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(winter_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(15,25),
                    'UVIndex':random.randint(3,5),
                    'WeatherCondition':random.choice(winter_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(500,700),
                    'State':'Puducherry',
                    'City':'Puducherry',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(40,60)
                },
                'Summer': {
                    'Datetime':generate_random_date(summer_start_date, summer_end_date),
                    'Temperature':summer_temperature,
                    'DewPoint':random.randint(summer_temperature - 5, summer_temperature),
                    'Humidity':random.randint(55,65),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(summer_precipitation),
                    'Pressure':random.randint(1000,1010),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(35,45),
                    'UVIndex':random.randint(5,15),
                    'WeatherCondition':random.choice(summer_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(600,800),
                    'State':'Puducherry',
                    'City':'Puducherry',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(70,80)
                },
                'Monsoon': {
                    'Datetime':generate_random_date(monsoon_start_date, monsoon_end_date),
                    'Temperature':monsoon_temperature,
                    'DewPoint':random.randint(monsoon_temperature - 5, monsoon_temperature),
                    'Humidity':random.randint(80,90),
                    'WindSpeed':random.randint(5,15),
                    'WindDirection':random.choice(wind_direction),
                    'Precipitation':random.choice(monsoon_precipitation),
                    'Pressure':random.randint(1005,1015),
                    'Visibility':random.randint(5,15),
                    'CloudCover':random.randint(75,85),
                    'UVIndex':random.randint(6,7),
                    'WeatherCondition':random.choice(monsoon_weather_condition),
                    'SnowDepth':random.randint(0,0),
                    'SolarRadiation':random.randint(200,400),
                    'State':'Puducherry',
                    'City':'Puducherry',
                    'FogorHaze':random.choice(fog_haze),
                    'AirQuality':random.randint(90,110)
                }
            }
        
        
    
    # Display City Data
    print(Gujarat)

# Calling WeatherData Function
WeatherData(states_cities)

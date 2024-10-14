from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np
from tqdm import tqdm
import os
import dotenv
import random
import time
import requests
from typing import List, Dict, Any
dotenv.load_dotenv()

foursquare_token = os.getenv("FOURSQUARE_TOKEN")

def get_city_coordinates_df(city_list: List[str]) -> pd.DataFrame:
    """
    Retrieve the latitude and longitude of cities using the Nominatim geocoding API.

    Args:
        city_list (List[str]): A list of city names.

    Returns:
        pd.DataFrame: A DataFrame with city names and their respective coordinates (latitude, longitude).
    """
    geolocator = Nominatim(user_agent="my_application_2")

    dict_city_coordenadas = {
        "city": list(),
        "latitude": list(),
        "longitude": list()
    }
    
    for city in tqdm(city_list):
        location = geolocator.geocode(city)
        dict_city_coordenadas["city"].append(city)
        dict_city_coordenadas["latitude"].append(location.latitude)
        dict_city_coordenadas["longitude"].append(location.longitude)

    return pd.DataFrame(dict_city_coordenadas)


def generate_nearby_places_df(coordinates_df: pd.DataFrame, categories_list: List[str], radius: int) -> pd.DataFrame:
    """
    Generate a DataFrame containing places near the provided cities based on specified categories and radius.

    Args:
        coordinates_df (pd.DataFrame): DataFrame with city names, latitudes, and longitudes.
        categories_list (List[str]): A list of place categories to search for (e.g., restaurants, parks).
        radius (int): The radius (in meters) within which to search for nearby places.

    Returns:
        pd.DataFrame: A concatenated DataFrame of nearby places for all cities in the coordinates DataFrame.
    """
    general_categories_df = pd.DataFrame()
    for idx, fila in tqdm(coordinates_df.iterrows()):
        time.sleep(random.randint(0, 3))
        city = fila["city"]
        latitude = fila["latitude"]
        longitude = fila["longitude"]
        city_categories_df = get_nearby_places(foursquare_token, city, latitude, longitude, categories_list, radius)
        general_categories_df = pd.concat([general_categories_df, city_categories_df])
    
    return general_categories_df


def get_nearby_places(token: str, city: str, latitude: float, longitude: float, 
                      category_list: List[str], radius: int) -> pd.DataFrame:
    """
    Retrieve nearby places from the Foursquare API based on the city's coordinates and category list.

    Args:
        token (str): Foursquare API token.
        city (str): Name of the city.
        latitude (float): Latitude of the city.
        longitude (float): Longitude of the city.
        category_list (List[str]): A list of categories to search for.
        radius (int): The radius (in meters) within which to search for nearby places.

    Returns:
        pd.DataFrame: A DataFrame containing the places found near the city based on the categories provided.
    """
    nearby_places_df = pd.DataFrame()
    for category in tqdm(category_list):
        response_dict = make_request(token, latitude, longitude, category, radius)
        response_df = format_results(response_dict, category)
        nearby_places_df = pd.concat([nearby_places_df, response_df])

    nearby_places_df["city"] = city
    
    return nearby_places_df


def make_request(token: str, latitude: float, longitude: float, categories: str, radius: int = 500) -> Dict[str, Any]:
    """
    Make a request to the Foursquare API to retrieve places within a certain radius of the provided coordinates.

    Args:
        token (str): Foursquare API token.
        latitude (float): Latitude for the location search.
        longitude (float): Longitude for the location search.
        categories (str): Categories of places to search for.
        radius (int, optional): Radius within which to search for places (default is 500 meters).

    Returns:
        Dict[str, Any]: The API response as a dictionary.
    """
    url = "https://api.foursquare.com/v3/places/search"

    params = {
        "categories": categories,
        "ll": f"{latitude},{longitude}",
        "sort": "DISTANCE",
        "radius": radius
    }

    headers = {
        "Accept": "application/json",
        "Authorization": token
    }

    response = requests.request("GET", url, params=params, headers=headers)
    return response.json()


def format_results(response_dict: Dict[str, Any], category: str) -> pd.DataFrame:
    """
    Format the results from the Foursquare API into a DataFrame with the desired output format.

    Args:
        response_dict (Dict[str, Any]): The response dictionary from the Foursquare API.
        category (str): The category used to search for the places.

    Returns:
        pd.DataFrame: A DataFrame with the relevant details about the places found.
    """
    dictionary = {
        "place_name": list(),
        "distance": list(),
        "main_latitude": list(),
        "main_longitude": list(),
        "address": list(),
        "searched_category": list(),
        "category_name": list()
    }
    
    try:
        for result in response_dict["results"]:
            dictionary["place_name"].append(result["name"])
            dictionary["distance"].append(result["distance"])
            try:
                dictionary["main_latitude"].append(result["geocodes"]["main"]["latitude"])
                dictionary["main_longitude"].append(result["geocodes"]["main"]["longitude"])
            except:
                dictionary["main_latitude"].append(np.nan)
                dictionary["main_longitude"].append(np.nan)
            dictionary["address"].append(result["location"]["formatted_address"])
            dictionary["searched_category"].append(category)
            dictionary["category_name"].append(result["name"])
    except:
        print("There's been a mistake.")

    return pd.DataFrame(dictionary)
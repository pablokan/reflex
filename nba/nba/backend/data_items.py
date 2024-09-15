from typing import Dict
from reflex.components.radix.themes.base import LiteralAccentColor

# Teams

teams_dict: Dict[str, LiteralAccentColor] = {
    "Boston Celtics": "green",
    "Brooklyn Nets": "gray",
    "New York Knicks": "blue",
    "Philadelphia 76ers": "blue",
    "Toronto Raptors": "red",
    "Chicago Bulls": "red",
    "Cleveland Cavaliers": "ruby",
    "Detroit Pistons": "red",
    "Indiana Pacers": "yellow",
    "Milwaukee Bucks": "green",
    "Atlanta Hawks": "red",
    "Charlotte Hornets": "purple",
    "Miami Heat": "red",
    "Orlando Magic": "blue",
    "Washington Wizards": "red",
    "Denver Nuggets": "gold",
    "Minnesota Timberwolves": "blue",
    "Oklahoma City Thunder": "blue",
    "Portland Trail Blazers": "red",
    "Utah Jazz": "green",
    "Los Angeles Lakers": "gold",
    "Golden State Warriors": "gold",
    "Los Angeles Clippers": "red",
    "Phoenix Suns": "orange",
    "Sacramento Kings": "purple",
    "Dallas Mavericks": "blue",
    "Houston Rockets": "red",
    "Memphis Grizzlies": "blue",
    "New Orleans Pelicans": "blue",
    "San Antonio Spurs": "gray",
}

teams_list = list(teams_dict.keys())

# Positions

position_dict: Dict[str, LiteralAccentColor] = {
    "PG": "blue",
    "SG": "green",
    "SF": "red",
    "PF": "yellow",
    "C": "purple",
}

positions_list = list(position_dict.keys())

# College

college_dict: Dict[str, LiteralAccentColor] = {
    "Texas": "orange",
    "Marquette": "blue",
    "Boston University": "red",
    "Georgia State": "blue",
    "LSU": "purple",
    "Gonzaga": "blue",
    "Louisville": "red",
    "Oklahoma State": "orange",
    "Ohio State": "red",
    "Washington": "purple",
    "Kentucky": "blue",
    "North Carolina": "blue",
    "Arizona": "blue",
    "Georgia Tech": "gold",
    "Cincinnati": "red",
    "Miami (FL)": "green",
    "Stanford": "red",
    "Syracuse": "orange",
    "Saint Louis": "blue",
    "Kansas": "blue",
    "Georgetown": "blue",
    "Texas A&M": "maroon",
    "UCLA": "blue",
    "UNLV": "red",
    "Wichita State": "black",
    "Saint Joseph's": "hawk blue",
    "Notre Dame": "gold",
    "Norfolk State": "green",
    "Duke": "blue",
    "Murray State": "blue",
    "Tennessee State": "blue",
    "Bowling Green": "orange",
    "Purdue": "gold",
    "Wake Forest": "gold",
    "Michigan": "maize",
    "Missouri": "gold",
    "USC": "gold",
    "Villanova": "blue",
    "Rider": "bronze",
    "Utah": "red",
    "Belmont": "blue",
    "Davidson": "wildcat blue",
    "Vanderbilt": "gold",
    "Michigan State": "green",
    "Florida": "orange",
    "Washington State": "crimson",
    "Arizona State": "maroon",
    "Oklahoma": "crimson",
    "Wyoming": "brown",
    "St. John's": "red",
    "Maryland": "red",
    "Wisconsin": "red",
    "Utah Valley": "blue",
    "North Carolina State": "red",
    "UC Santa Barbara": "blue",
    "Baylor": "green",
    "Connecticut": "blue",
    "Oregon State": "orange",
    "New Mexico": "lobos red",
    "Oregon": "green",
    "Creighton": "blue",
    "Arkansas": "red",
    "Memphis": "blue",
    "Saint Mary's": "gaels green",
    "Tennessee": "orange",
    "Alabama": "crimson",
    "Georgia": "red",
    "Colorado": "gold",
    "Boston College": "maroon",
    "Temple": "cherry",
    "Fresno State": "red",
    "IUPUI": "blue",
    "Eastern Washington": "red",
    "Western Michigan": "brown",
    "Virginia": "orange",
    "Northeastern": "red",
    "Western Kentucky": "red",
    "Nevada": "blue",
    "Illinois": "orange",
    "Kansas State": "purple",
    "Charleston": "purple",
    "Clemson": "orange",
    "Blinn College": "blue",
    "Providence": "blue",
    "Detroit": "red",
    "Rhode Island": "blue",
    "California": "gold",
    "Cleveland State": "green",
    "Iowa State": "cardinal",
    "Florida State": "gold",
    "Long Beach State": "gold",
    "Penn State": "blue",
    "Indiana": "crimson",
    "San Diego State": "red",
    "Western Carolina": "purple",
    "Houston": "red",
    "Xavier": "blue",
    "Old Dominion": "blue",
    "Minnesota": "gold",
    "Louisiana Tech": "blue",
    "Bucknell": "orange",
    "Pittsburgh": "gold",
    "Virginia Commonwealth": "black",
    "Harvard": "crimson",
    "Marshall": "green",
    "Iowa": "black",
    "St. Bonaventure": "brown",
    "Louisiana-Lafayette": "red",
    "Colorado State": "green",
    "Virginia Tech": "orange",
    "DePaul": "blue",
    "Morehead State": "blue",
    "Central Michigan": "maroon",
    "Weber State": "blue",
    "Lehigh": "brown",
    "Westchester CC": "blue",
    "Dayton": "red",
    "Butler": "blue"
}

college_list = list(college_dict.keys())

all_items = {
    "teams": teams_list,
    "positions": positions_list,
    "colleges": college_list
}
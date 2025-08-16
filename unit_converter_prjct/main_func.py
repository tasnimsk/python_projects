from welcome_page import WelcomePage
from converter_page import Converter
import tkinter as tk

def main():
    welcome = WelcomePage()

    unit_data = {
        "lb": ["Meters", "Feet", "Inches"],
        "para": {},
        "para1": {},
        "Meters": ["{}/3.28084", "{}*39.3701", 0],
        "Feet": ["{}/3.28084", "{}*12", 1],
        "Inches": ["{}/39.3701", "{}*12", 2]
    }
    converter = Converter(unit_data)

if __name__ == "__main__":
    main()
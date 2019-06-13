from enum import Enum, auto

class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

class Elements(AutoName):
    Calcium = auto() 
    Chromium = auto() 
    Copper = auto() 
    Fluoride = auto() 
    Iodine = auto() 
    Iron = auto() 
    Magnesium = auto() 
    Manganese = auto() 
    Molybdenum = auto() 
    Phosphorus = auto() 
    Selenium = auto() 
    Zinc = auto() 
    Potassium = auto() 
    Sodium = auto() 
    Chloride = auto()

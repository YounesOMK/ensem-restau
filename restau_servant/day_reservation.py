from typing import Optional

from datetime import datetime
from enum import Enum
from .validators import valid_date
from .config import DO_RESERVATION_URL

class Meal(Enum):
    BREAKFAST = 1
    LUNCH = 2
    DINNER = 3
    
class Choice(Enum):
    HOT_MEAL = 1
    COLD_MEAL = 2

class DayReservation:
    
    def __init__(self, date: datetime,
                meal: Meal,
                choice: Choice = Choice.HOT_MEAL) -> None:
        
        self._date = date
        self.meal = meal.value
        self.choice = choice.value
        
    @property
    def date(self):
        return datetime.strftime(self._date, "%Y-%m-%d")
    
        
    def do_using(self, session):
        session.post(DO_RESERVATION_URL, {
            "date": valid_date(self.date),
            "repas": str(self.meal),
            "composition": str(self.choice)
        })
        print(self.date)
        print(self.meal)
        print(self.choice)
        
    def __repr__(self):
        return f"{self.__class__.__name__}({self.date!r}, {self.meal!r}, {self.choice!r})"
    
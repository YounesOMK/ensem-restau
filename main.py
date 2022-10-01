from datetime import datetime
from restau_servant.auth.login_session import start_login_session 
from restau_servant.day_reservation import DayReservation, Meal, Choice

def main():
    session = start_login_session("XX99999", "30/05/2000")
    reservation = DayReservation(datetime(2022, 10, 1), Meal.DINNER, Choice.HOT_MEAL)
    reservation.do_using(session)

if __name__ == '__main__':
    main()
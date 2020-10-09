from typing import Optional, List


import datetime
import bson
from data.bookings import Booking
from data.cages import Cage
from data.owners import Owner
from data.snakes import Snake



def create_account(name: str, email: str) -> Owner:
    owner = Owner()
    owner.name = name
    owner.email = email
    owner.save()
    return owner

def find_account_by_email(email: str) -> Owner:
    owner = Owner.objects(email=email).first()
    return owner

def register_cage(active_account: Owner,name: str,cost: float,square_meters: float,is_carpented: bool,
                  has_toys: bool, allow_dangerous_snakes: bool) ->Cage:

    cage = Cage()
    cage.name = name
    cage.cost = cost
    cage.square_meters = square_meters
    cage.is_carpented = is_carpented
    cage.has_toys = has_toys
    cage.allow_dangerous_snakes = allow_dangerous_snakes

    cage.save()

    owner = find_account_by_email(active_account.email)
    owner.cage_ids.append(cage.id)
    owner.save()
    return cage

def find_cages_for_user(account: Owner) -> List[Cage]:
    cages = Cage.objects(id__in=account.id)
    return list(cages)


def add_available_date(cage: Cage, start_date: datetime.datetime, days: int) -> Cage:
    booking = Booking()
    booking.checkin_date = start_date
    booking.chckout_date = start_date + datetime.timedelta(days=days)

    cage = Cage.objects(id=cage.id).first()
    cage.bookings.append(booking)
    cage.save()
    return cage



def add_snake(account: Owner, name: str, length: float, species: str, is_venomous: bool) -> Snake:
    snake = Snake()
    snake.name = name
    snake.length = length
    snake.species = species
    snake.is_venomous = is_venomous

    snake.save()

    owner = find_account_by_email(account.email)
    owner.snake_ids.append(snake.id)
    owner.save()

    return snake

def get_snakes_for_user(user_id: bson.ObjectId) -> list[Snake]:
    owner = Owner.objects(id=user_id)
    snakes = Snake.objects(id__in=owner.snake_ids).all()
    return list(snakes)















class Error(Exception):
    """Base class for other exceptions"""
    pass

class WrongHourError(Error):
  """Raised when the hour input is larger than 24!"""
  pass

class WrongMinuteError(Error):
  """Raised when the minute input is larger than 60!"""
  pass

class HourWhenArrivedTooBigError(Error):
  """Raised when the hour you arrived is bigger than the time you left!"""
  pass

class MinuteWhenArrivedTooBigError(Error):
  """Raised when the hour you arrived and left is identical, but the minute you arrived
  is bigger then the minute you left!"""
  pass

def input_forTime():
  while True:
    try:
      timeInput = input("-> ")

      seperated = list(map(int, timeInput.split(":")))

      if seperated[0] < 0 and seperated[0] > 24:
        raise WrongHourError
      elif seperated[1] < 0 and seperated[1] > 60:
        raise WrongMinuteError
      break
    except ValueError:
      print("\nWrong Input type!\ntry format -> 7:21\n")
    except WrongHourError:
      print("\nThe Value is lower than 0 or larger than 24!\n")
    except WrongMinuteError:
      print("\nThe Value is lower thna 0 or larger than 60!\n")

  return seperated

while True:
  try:
    print("Format: 7:21")
    print("\nWhen did you arrive at work?\n")

    arrived = input_forTime()

    print("\nWhen did you leve work?\n")

    left = input_forTime()

    if left[0] < arrived[0]:
      raise HourWhenArrivedTooBigError
    elif left[0] == arrived[0] and left[1] < arrived[1]:
      raise MinuteWhenArrivedTooBigError
    break
  except HourWhenArrivedTooBigError:
    print("\nThe hour you arrived is bigger than the time you left!\n")
  except MinuteWhenArrivedTooBigError:
    print("\nThe hour you arrived and left is identical, but\n",
    "the minute you arrived is bigger than the minute you left!\n")

# time calculation ⏲
hours = left[0] - arrived[0]

if left[1] < arrived[1]:
  minutes = 60 - arrived[1] + left[1]
  hours = hours - 1
else:
  minutes = left[1] - arrived[1]

print("\nYou have worked for ", hours, " hours and ", minutes, " minutes ⏲")
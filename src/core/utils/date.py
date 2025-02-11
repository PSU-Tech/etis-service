from datetime import datetime


def get_current_education_year():
  now = datetime.today()
  month = now.month

  if month < 9:
    return now.year - 1
  return now.year
  
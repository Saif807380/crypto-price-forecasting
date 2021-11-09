from datetime import datetime

def hello():
    return "hello world"

def convert_str_to_date(str_date: str) -> datetime:
    return datetime.strptime(str_date, "%d/%m/%Y")

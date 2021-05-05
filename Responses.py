from datetime import datetime

def datetime():
    now = datetime.now()
    date_time = now.strftime("%d/%m/%y, %H:%M:%S")
    return str(date_time)

def responses(input_text):
    message = str(input_text).lower()

    if message in ("hello", "hi", "hey"):
        return "Hi em"

    if message in ("who are you?"):
        return "I am AmunnBot"

    if message in ("what time is it?"):
        datetime()

    return "I cannot understand it"

from datetime import datetime

def responses(input_text):
    message = str(input_text).lower()

    if message in ("hello", "hi", "hey"):
        return "Hey!"

    if message in ("who are you", "who are you?"):
        return "I am Amun Bot"

    if message in ("what time is it?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "I don't understand you"

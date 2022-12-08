def get_current_time():
    """Returns the current time as a string in the format 'YYYY-MM-DD HH:MM:SS'"""
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def log(message):
    """Prints the provided message along with the current time"""
    print(f'[{get_current_time()}] {message}')

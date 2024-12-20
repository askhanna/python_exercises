def getHoursMinutesSeconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return hours, minutes, seconds

if __name__ == "__main__":
    seconds = int(input("Enter the number of seconds: "))
    hours, minutes, seconds = getHoursMinutesSeconds(seconds)
    print(f"{hours} hours, {minutes} minutes, and {seconds} seconds")
    # Alternative way to print the result
    txt = ""
    if hours > 0:
        txt += f"{hours} hours "
    if minutes > 0:
        txt += f"{minutes} minutes "
    if seconds > 0:
        txt += f"{seconds} seconds"
    print(txt)
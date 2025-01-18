import datetime

# Get the current time in seconds since the epoch
current_time_seconds = int(datetime.datetime.now().timestamp())

# Calculate the number of days since the epoch
days_since_epoch = current_time_seconds // 86400

# Get the current time in hours, minutes, and seconds
current_time = datetime.datetime.now()
hours = current_time.hour
minutes = current_time.minute
seconds = current_time.second

# Print the results
print("Current time:")
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
print("Days since epoch:", days_since_epoch)
#Countdown Timer 
import time

def countdown(t):
    while t: 
        mins, secs = divmod(t, 60)  # Calculate minutes and seconds
        timer = '{:02d}:{:02d}'.format(mins, secs)  # Format timer
        print(timer, end="\r")  # Print timer on the same line
        time.sleep(1)  # Wait for 1 second (when I change to '2'it gets slower i.e it waits for 2 secs)
        t -= 1  # Decrease time by 1 second 

    print('Done!')  # Indicate the countdown has finished

# Prompt the user to enter time in seconds
try:
    t = int(input('Enter time in seconds: '))  # Convert input to integer
    countdown(t)  # Start the countdown
except ValueError:
    print("Please enter a valid number.")  # Handle invalid input
   
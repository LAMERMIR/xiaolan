import time

def focus_timer(duration):
    print("Focus Timer Started.")
    while duration > 0:
        mins, secs = divmod(duration, 60)
        timer_display = '{:02d}:{:02d}'.format(mins, secs)
        print(timer_display, end='\r')
        time.sleep(1)
        duration -= 1
    
    print("Time's up! Take a break.")

if __name__ == "__main__":
    try:
        minutes = int(input("Enter the duration of focus (in minutes): "))
        focus_timer(minutes * 60)
    except ValueError:
        print("Please enter a valid number of minutes.")

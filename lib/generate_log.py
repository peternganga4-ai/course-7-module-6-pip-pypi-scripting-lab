from datetime import datetime


def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Data must be a list")
    #creates  a filewith todays date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

# writes the log entries to a file
    with open(filename, "w") as file:
        #goes through every item in the list
        for entry in data:
            #writes each one on its own line
            file.write(f"{entry}\n")

#return the filename
    return filename
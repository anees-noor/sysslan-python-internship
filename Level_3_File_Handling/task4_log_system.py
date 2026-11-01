from datetime import datetime

while True:
    message = input("\nEnter log message (or type exit): ")

    if message.lower() == "exit":
        print("Logging stopped.")
        break

    current_time = datetime.now()

    with open("log.txt", "a") as file:
        file.write(str(current_time) + " - " + message + "\n")

    print("Log saved successfully!")
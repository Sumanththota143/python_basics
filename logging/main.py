import logging

#basic configuarion mandatory
logging.basicConfig(
    #set level as 1st logging level
    level=logging.INFO ,
    # by putting a file name all logs are recorded in a file instead of terminal
    filename="app.log" ,
    # to print the time of log created use:
    format="%(asctime)s - %(levelname)s - %(message)s"

    )

username = "sumanth"
password = "1234"

logging.info("Login process started")

if username == "sumanth" and password == "1234":
    logging.info("User logged in successfully")
else:
    logging.error("Invalid username or password")

logging.info("Login process finished")
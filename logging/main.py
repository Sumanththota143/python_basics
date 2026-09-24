import logging

logging.basicConfig(
    level=logging.INFO ,
    filename="app.log"
    )

username = "sumanth"
password = "1234"

logging.info("Login process started")

if username == "sumanth" and password == "1234":
    logging.info("User logged in successfully")
else:
    logging.error("Invalid username or password")

logging.info("Login process finished")
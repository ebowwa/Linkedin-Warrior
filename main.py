from linkedin import Linkedin
from utils import log
from constants import BOT_SPEED, PHONE_VERIFICATION_DELAY

# initialize the LinkedIn bot
bot = Linkedin()

# wait for the user to verify their phone number
time.sleep(PHONE_VERIFICATION

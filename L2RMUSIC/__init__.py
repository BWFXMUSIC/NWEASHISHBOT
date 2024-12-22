from VenomX.core.bot import Ashish
from VenomX.core.dir import dirr
from VenomX.core.git import git
from VenomX.core.userbot import Userbot
from VenomX.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Ashish()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

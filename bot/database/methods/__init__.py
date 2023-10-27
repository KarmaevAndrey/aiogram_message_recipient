from bot.database.main import *
from bot.database.methods.get import get_select, get_unique_code

script_dir = pathlib.Path(sys.argv[0]).parent
PATH_BAZE = script_dir / 'bot/database/data_baza.db'
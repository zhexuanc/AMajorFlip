from config import *

from flask import *

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def main_route():
	return 'welcome to eecs498!'
from flask import *
from disk_list import *
from disk_analisis import *

app = Flask(__name__)


@app.route('/')
def index():
    return f"Вот список ваших дисков: {disk_list()}"


# disk_list(), disk_analisis()
if __name__ == '__main__':
    app.run()

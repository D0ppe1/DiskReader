from flask import *
from disk_list import *
from disk_analisis import *

app = Flask(__name__)


@app.route('/')
def index():
    reply = ''
    for disk in disk_list():
        reply += f'Disk -- {disk}\
        stats:{disk_analisis(disk)}'
    return reply


# f"Вот список ваших дисков: {disk_list()}"
if __name__ == '__main__':
    app.run()

from flask import Flask
import disk_list
import disk_analisis

app = Flask(__name__)


@app.route('/')
def index():
    reply = ''
    for disk in disk_list.disk_list():
        reply += f'Disk -- {disk} -- <br> Stats: {disk_analisis.disk_analisis(disk)}<br>'
    return reply


if __name__ == '__main__':
    app.run(host='192.168.0.57', port=80)

import flask
from flask import request, jsonify
import pyautogui as g

app = flask.Flask(__name__)


prevcoords = [(0, 0)]

fmc = [(0, 0)]

@app.route('/eyedata', methods=['POST'])
def home():
    x = request.args.get('x') or 0
    x = float(x)

    y = request.args.get('y') or 0
    y = float(y)

    gx = request.args.get('gx') or 0
    gx = float(x)

    gy = request.args.get('gy') or 0
    gy = float(y)

    dx = request.args.get('dx') or 0
    dx = float(x)

    dy = request.args.get('dy') or 0
    dy = float(y)

    if (x, y) == (0, 0):
        return '0'

    prevcoords.append((x, y))

    if len(fmc) <= 300:

        print(x-dx, x-gx, dx-gx)

        if ((x-prevcoords[-1][0])**2 +  (y-prevcoords[-1][1])**2) **0.5 >= 0:

            g.moveTo(x+150, y+150)

        print(((x-prevcoords[-1][0])**2 +  (y-prevcoords[-1][1])**2) **0.5)

    fmc.append(0)
    prevcoords.append((x, y))

    print('\n\n'+str(len(fmc))+'\n\n' )

    return '0'

    #g.moveTo(x, y)
if __name__ == "__main__":
    app.run(debug=True)

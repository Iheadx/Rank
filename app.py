from flask import Flask, render_template, jsonify, request
from BService import userrank,teamrank,getteamans
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/table1')
def get_table1():
    table1_data = userrank()
    return jsonify(table1_data)

@app.route('/table2')
def get_table2():
    table2_data = teamrank('hs')
    return jsonify(table2_data)

@app.route('/table3')
def get_table3():
    table2_data = teamrank('zf')
    return jsonify(table2_data)

@app.route('/team_details')
def get_team_details():
    team_id = request.args.get('team_id')  # 获取团队id
    team_data = getteamans(team_id)
    return jsonify(team_data)

if __name__ == '__main__':
    app.run(port=80)

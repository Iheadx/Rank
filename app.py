from flask import Flask, render_template, jsonify, request
from BService import userrank,teamtot,getteamans,classrank
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('4_4.html')

@app.route('/table1')
def get_table1():
    table1_data = userrank()
    return jsonify(table1_data)

@app.route('/table2')
def get_table2():
    table2_data = teamtot()
    return jsonify(table2_data)

@app.route('/table3')
def get_table3():
    table3_data = classrank()
    return jsonify(table3_data)

@app.route('/team_details')
def get_team_details():
    team_name = request.args.get('team_name')  # 获取团队id
    team_data = getteamans(team_name)
    return jsonify(team_data)

if __name__ == '__main__':
    app.run(port=80)

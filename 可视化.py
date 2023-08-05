from flask import Flask, request, render_template
import query2 as qy
import query_sarsa as qu
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def select():
    return render_template('选择.html')
@app.route('/temp', methods=['POST'])
def tmp():
    return render_template('地图.html')


@app.route('/luxian', methods=['POST'])
def query():
    # code = request.form.get('name')
    # b=qy.q_net_make(code)
    return render_template('final-road.html')

@app.route('/sarsa_luxian', methods=['POST'])
def sarsa_query():
    # code = request.form.get('name')
    # b=qy.q_net_make(code)
    return render_template('sarsa_final-road.html')




@app.route('/weizhi', methods=['POST'])
def find_first():
    final = request.form.get('name')
    b,e=qy.q_net_make(final)
    return render_template('begin-final-road.html', list1=e)


@app.route('/sarsa_weizhi', methods=['POST'])
def sarsa_find_first():
    final = request.form.get('name')
    b,e1,e=qu.sarsa_net_make(final)
    return render_template('sarsa_begin-final-road.html', list1=e1)

@app.route('/location', methods=['POST'])
def find_road():
    final = request.form.get('name')
    b, e = qy.q_net_make(final)
    first=request.form.get('name2')
    first=int(first)
    c,j,w,l=qy.find(final,first,b)
    qy.show_road(j,w,l)
    return render_template('road_ok.html', list2=c)


@app.route('/sarsa_location', methods=['POST'])
def sarsa_find_road():
    final = request.form.get('name')
    b, e1,e = qu.sarsa_net_make(final)
    first=request.form.get('name2')
    first=int(first)
    b=qu.sarsa_true_net(e,final)
    c,j,w,l=qu.sarsa_find(final,first,b)#qy.find(final,first,b)
    qu.sarsa_show_road(j,w,l)
    return render_template('sarsa_road_ok.html', list2=c)

@app.route('/watch', methods=['GET','POST'])
def find_geo():
    return render_template('geo_road.html')



@app.route('/sarsa_watch', methods=['GET','POST'])
def sarsa_find_geo():
    return render_template('sarsa_geo_road.html')






# @app.route('/system', methods=['GET'])
# def signin_form():
#   return render_template('query.html')
# @app.route('/signin', methods=['GET'])
# def signin_form():
#  return render_template('form.html')
#
# @app.route('/signin', methods=['POST'])
# def signin():
#     username = request.form['username']
#     password = request.form['password']
#     if username=='admin' and password=='password':
#             return render_template('signin-ok.html', username=username)
#     return render_template('form.html', message='Bad username or password', username=username)
#@app.route('/signin', methods=['GET'])
# def signin_form():
#  return render_template('form.html')
#
# @app.route('/signin', methods=['POST'])
# def signin():
#     username = request.form['username']
#     password = request.form['password']
#     if username=='admin' and password=='password':
#             return render_template('signin-ok.html', username=username)
#     return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run(debug=True)


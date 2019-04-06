from flask import Flask
from flask_mysqldb import MySQL 
from flask import flash, render_template, request, redirect
from flask import jsonify
from helper_classes import *

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] =  'anmol'
app.config['MYSQL_PASSWORD'] = 'davinder123'
app.config['MYSQL_DB'] = 'twitter'

mysql = MySQL(app) # initialized the connection

def return_all():
	# use cursor to query the database
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM tweets''')
    rv = cur.fetchall()
    response = {"tweets" :[], "number_of_tweeets" : 0}
    for row in rv:
        temp = tweet()
        temp._initialize(row)
        d = temp._get_dic()
        response["tweets"].append(d)
        response["number_of_tweeets"] += 1
    return response

def author_query(name):
    cur = mysql.connection.cursor()
    query = "SELECT id from author where name = "+ name
    cur.execute(query)
    rv = cur.fetchall()
    response = {"id" :[ ]}
    for id_ in rv:
        response["id"].append(str(id_))
    return response

def hastag_query(hashtag):
    '''
    input = single hastag
    returns  = all tweets corresponding to hastag
    '''
	# use cursor to query the database
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM hastag WHERE' + hashtag + '= text')
    rv = cur.fetchall()
    temp = hashtablerow()
    temp._initialize(row)
    d = temp._get_dic()

    # getting the events corresponding to 

    return d

def event_query(event):
    '''
    input = event string
    return = all tweets related to that event
    '''

def after(time):
    '''
    input = time
    returns = all tweets posted after that time unitl now
    '''

def today():
    '''
    return = all tweets posted today until now
    '''

def week():
    '''
    return = all tweets posted in this week
    ''' 
def author():
    '''
    return = author table
    '''
    cur = mysql.connection.cursor()
    query = '''SELECT * FROM author'''
    cur.execute(query)
    rv = cur.fetchall()
    response = {"id" :[], "name":[], "followers":[], "following":[]}
    for row in rv:
        response["id"].append(row[0])
        response["name"].append(row[1])
        response["followers"].append(row[2])
        response["following"].append(row[3])
    print(response)
    return response

def hastag():
    '''
    return = hastag table
    '''
@app.route('/', methods = ['GET', 'POST'])
def index():
    data = request.data
    arguments = request.form
    arguments = arguments.to_dict(flat=False)
    if request.method == 'POST':
        return search_results(arguments)

@app.route('/api/user', methods = ['POST'])
def search_results(search):
    print(search)
    if search == {}:
        result = return_all()
        return jsonify(result)
    else:
        keyword = list(search.keys())[0]
        print(keyword)
        result = None
        if keyword == 'author':
            query = search[keyword][0]
            if query == '':
                results = author()
            else:
                results = author_query(query)
        if keyword == 'hashtag':
            query = search[keyword][0]
            if query == '':
                results = hashtag()
            else:
                results = hastag_query(query)
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=3000)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'
    #return render_template('index.html')

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

@app.route('/8355')
def students():
    connection = pymysql.connect(host='mrbartucz.com',
                               user='cl8355ps',
                               password='Kabi666',
                               db='cl8355ps_University',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
        execute("SELECT * FROM Students")
        students = self.cur.fetchall()

    return render_template('index.html', data=students, content_type='application/json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
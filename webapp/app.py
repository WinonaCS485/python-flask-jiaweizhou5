from flask import Flask, render_template
import pymysql.cursors

# Connect to database
connection = pymysql.connect(host='mrbartucz.com',
                               user='cl8355ps',
                               password='Kabi666',
                               db='cl8355ps_university',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'
    #return render_template('index.html')

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

@app.route('/students')
def students(): 
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Student"
            cursor.execute(sql)

        output = "<br>"
        for result in cursor:
            output += str(result)
            output += "<br>"
        return (output)

#     return render_template('database.html', output = output)

    finally:
        connection.close()
    
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8355)
    


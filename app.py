from flask import Flask, render_template, request, send_file
import pymysql


def sql_connector():
    conn = pymysql.connect(
        user='root', password='nithesh13631', db='prithvi', host='localhost')
    c = conn.cursor()
    return conn, c


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        conn, c = sql_connector()
        c.execute("INSERT INTO project VALUES ('{}','{}','{}')".format(
            name, email, message))
        conn.commit()
        conn.close()
        c.close()
        print(name, email, message)

    return render_template("index.html")


@app.route('/subsription', methods=['GET', 'POST'])
def subscription():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        conn, c = sql_connector()
        c.execute("INSERT INTO subscription VALUES ('{}','{}','{}')".format(
            name, email, message))

        conn.commit()
        conn.close()
        c.close()
        print(name, email, message)

    return render_template("subscription.html")


@app.route('/inner')
def table_data():

    # conn = mysqlx.connector.connect(
    #     host=app.config['localhost'],
    #     user=app.config['root'],
    #     password=app.config['nithesh13631'],
    #     database=app.config['prithvi']
    # )
    conn = pymysql.connect(
        user='root', password='nithesh13631', db='prithvi', host='localhost')
    cursor = conn.cursor()

    # Fetch table data
    query = "select * from project INNER JOIN subscription ON project.email=subscription.email;"
    cursor.execute(query)
    table_data = cursor.fetchall()

    cursor.close()
    conn.close()

    # Render the template with table data as response
    return render_template('inner.html', table_data=table_data)
    # return render_template('index.html')


@app.route('/left')
def table():

    # conn = mysqlx.connector.connect(
    #     host=app.config['localhost'],
    #     user=app.config['root'],
    #     password=app.config['nithesh13631'],
    #     database=app.config['prithvi']
    # )
    conn = pymysql.connect(
        user='root', password='nithesh13631', db='prithvi', host='localhost')
    cursor = conn.cursor()

    # Fetch table data
    query = "select * from project LEFT JOIN subscription ON project.email=subscription.email;"
    cursor.execute(query)
    table = cursor.fetchall()

    cursor.close()
    conn.close()

    # Render the template with table data as response
    return render_template('left.html', table=table)
    # return render_template('index.html')


@app.route('/operation')
def operation():
    return render_template('button.html')


@app.route('/right')
def right():

    # conn = mysqlx.connector.connect(
    #     host=app.config['localhost'],
    #     user=app.config['root'],
    #     password=app.config['nithesh13631'],
    #     database=app.config['prithvi']
    # )
    conn = pymysql.connect(
        user='root', password='nithesh13631', db='prithvi', host='localhost')
    cursor = conn.cursor()

    # Fetch table data
    query = "select * from project LEFT JOIN subscription ON project.email=subscription.email;"
    cursor.execute(query)
    right = cursor.fetchall()

    cursor.close()
    conn.close()

    # Render the template with right data as response
    return render_template('right.html', right=right)
    # return render_template('index.html')


@app.route('/full')
def full():

    # conn = mysqlx.connector.connect(
    #     host=app.config['localhost'],
    #     user=app.config['root'],
    #     password=app.config['nithesh13631'],
    #     database=app.config['prithvi']
    # )
    conn = pymysql.connect(
        user='root', password='nithesh13631', db='prithvi', host='localhost')
    cursor = conn.cursor()

    # Fetch table data
    query = "select * from project LEFT JOIN subscription ON project.email=subscription.email;"
    cursor.execute(query)
    full = cursor.fetchall()

    cursor.close()
    conn.close()

    # Render the template with full data as response
    return render_template('full.html', full=full)
    # return render_template('index.html')


@app.route('/union')
def union():

    # conn = mysqlx.connector.connect(
    #     host=app.config['localhost'],
    #     user=app.config['root'],
    #     password=app.config['nithesh13631'],
    #     database=app.config['prithvi']
    # )
    conn = pymysql.connect(
        user='root', password='nithesh13631', db='prithvi', host='localhost')
    cursor = conn.cursor()

    # Fetch table data
    query = "SELECT name, email FROM project WHERE name='Nithesh R' UNION SELECT name, email FROM subscription WHERE name='Nithesh R' ORDER BY name;"
    cursor.execute(query)
    union = cursor.fetchall()

    cursor.close()
    conn.close()

    # Render the template with union data as response
    return render_template('union.html', union=union)
    # return render_template('index.html')


@app.route('/ino')
def ino():

    # conn = mysqlx.connector.connect(
    #     host=app.config['localhost'],
    #     user=app.config['root'],
    #     password=app.config['nithesh13631'],
    #     database=app.config['prithvi']
    # )
    conn = pymysql.connect(
        user='root', password='nithesh13631', db='prithvi', host='localhost')
    cursor = conn.cursor()

    # Fetch table data
    query = "SELECT * FROM project WHERE name IN ('Nithesh R', 'nithil', 'palani');"
    cursor.execute(query)
    ino = cursor.fetchall()

    cursor.close()
    conn.close()

    # Render the template with ino data as response
    return render_template('in.html', ino=ino)
    # return render_template('index.html')


@app.route('/between')
def between():

    # conn = mysqlx.connector.connect(
    #     host=app.config['localhost'],
    #     user=app.config['root'],
    #     password=app.config['nithesh13631'],
    #     database=app.config['prithvi']
    # )
    conn = pymysql.connect(
        user='root', password='nithesh13631', db='prithvi', host='localhost')
    cursor = conn.cursor()

    # Fetch table data
    query = "SELECT * FROM subscription WHERE name BETWEEN 'Nithesh R' AND 'Rog-Media' ORDER BY name;"
    cursor.execute(query)
    between = cursor.fetchall()

    cursor.close()
    conn.close()

    # Render the template with between data as response
    return render_template('between.html', between=between)
    # return render_template('index.html')


@app.route('/dis')
def dis():

    # conn = mysqlx.connector.connect(
    #     host=app.config['localhost'],
    #     user=app.config['root'],
    #     password=app.config['nithesh13631'],
    #     database=app.config['prithvi']
    # )
    conn = pymysql.connect(
        user='root', password='nithesh13631', db='prithvi', host='localhost')
    cursor = conn.cursor()

    # Fetch table data
    query = "SELECT DISTINCT name FROM project;"
    cursor.execute(query)
    dis = cursor.fetchall()

    cursor.close()
    conn.close()

    # Render the template with dis data as response
    return render_template('distinct.html', dis=dis)
    # return render_template('index.html')


@app.route('/downloadfile', methods=['GET'])
def download():

    p = "/templates/KA-36 WHITE HATTERS.pdf"

    return send_file(p, as_attachment=True)


    # @app.route('/<nam>')
    # def user(nam):
    #     return f"hello {nam}"
if __name__ == "__main__":
    app.debug = True
    app.run()

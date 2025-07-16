from flask import Flask , render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pravin2003@'
app.config['MYSQL_DB'] = 'flask_project'

mysql = MySQL(app)

@app.route("/")
def home():
  return render_template("home_asmt.html")

@app.route('/breakfast')
def breakfast():
    return render_template('breakfast.html')

@app.route('/meals')
def meals():
    return render_template('meals.html')

@app.route('/dinner')
def dinner():
    return render_template('dinner.html')
 

@app.route('/about')
def about():
  return render_template('about_asmt.html')


@app.route('/contact')
def contact():
    return render_template('contact_asmt.html')

 

@app.route('/place_order', methods=['POST'])
def place_order():
    name = request.form.get('customer_name')
    phone = request.form.get('phone')
    address = request.form.get('address')
    order_items = request.form.get('order_items')
    instructions = request.form.get('instructions')

    cursor = mysql.connection.cursor()

    # Create table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer_orders_final (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20),
            address TEXT,
            order_items TEXT,
            instructions TEXT
        )
    ''')

    # Insert into table
    cursor.execute('''
        INSERT INTO customer_orders_final (name, phone, address, order_items, instructions)
        VALUES (%s, %s, %s, %s, %s)
    ''', (name, phone, address, order_items, instructions))

    mysql.connection.commit()
    cursor.close()

    print("Order saved to DB:", name, phone, address, order_items, instructions)

    return render_template('order_success.html', name=name)


if __name__ == '__main__':
  app.run(debug=True)
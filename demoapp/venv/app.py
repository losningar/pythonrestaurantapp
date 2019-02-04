from flask import Flask, render_template, request, make_response, redirect, abort, url_for, session, g, flash
import pymongo
import uuid 
import json
import os
from db import connectDB
from customclasses import Customer, Menu, Employee
app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def employeelogin():
    mycol = connectDB('Employees') 
    if request.method == 'POST':
        query = {"username": request.form['username']} 
        employee = mycol.find_one(query)
        
        if employee == None:
            return render_template('customerror.html')

        session.pop('user', None)
        if request.form['password'] == employee['password']:
            session['user'] = request.form['username']
            return redirect(url_for('dashboard'))
    return render_template('employeeloginpage.html')
    
    

@app.route('/customers/register/post',methods = ['POST', 'GET'])
def RegisterCustomersPost():
    mycol = connectDB('Customers') 

    customer = Customer()
    customer.firstname = request.form["Firstname"]
    customer.lastname = request.form["Lastname"]
    customer.email = request.form["Email"]
    customer.address = request.form["Adress"]
    customer.postcode = request.form["Postcode"]
    customer.city = request.form["City"]
    customer.username = request.form["Username"]
    customer.password = request.form["Password"]
    
    dictcustomer = (customer.__dict__)

    mycol.insert(dictcustomer)
    
    
    return render_template('registercustomer.html')

@app.route('/customers/register')
def Registercustomers():

    return render_template('registercustomer.html')

@app.route('/customers/index',methods = ['POST', 'GET'])
def GetCustomers():
    mycol = connectDB('Customers') 
    
    return render_template('customersindex.html', allcustomers=mycol.find())

@app.route('/menu/additemspost',methods = ['POST', 'GET'])
def MenuAddItemPost():
    mycol = connectDB('Menu') 
    menu = Menu()
    menu.dish = request.form["dish"]
    menu.dishName = request.form["dishName"]
    menu.dishSize = request.form["dishSize"]
    menu.dishPrice = request.form["dishPrice"]

    dictmenu = (menu.__dict__)

    mycol.insert(dictmenu)
    return render_template('addmenu.html')

@app.route('/menu/additems')
def MenuAddItem():

    return render_template('addmenu.html')

@app.route('/menu',methods = ['POST', 'GET'])
def GetMenu():
    mycol = connectDB('Menu') 
    return render_template('menuindex.html', menu=mycol.find())

@app.route('/employees/register/post',methods = ['POST', 'GET'])
def RegisterEmployeesPost():
    mycol = connectDB('Employees') 
    e = Employee()
    e.firstname = request.form["Firstname"]
    e.lastname = request.form["Lastname"]
    e.email = request.form["Email"]
    e.permissions = request.form["Permissions"]
    e.username = request.form["Username"]
    e.password = request.form["Password"]
    e.tokenID = "empty"
    dicte = (e.__dict__)

    mycol.insert(dicte)
    
    
    return render_template('registeremployees.html')

@app.route('/employees/register')
def Registeremployees():

    return render_template('registeremployees.html')

#@app.route('/admindashboard',methods = ['POST', 'GET'])
#def AdminDashboard():
    
 #   username = request.cookies.get('username') #ÄNDRA TILL tokenID här!
    
  #  reqPerm = "admin"

   # auth = CheckPermissions(username, reqPerm) 
    
    #if auth == True:
     #   return render_template('admindashboard.html')
    
    #else:
     #   return render_template('customerror.html')


def CheckPermissions(username, requriedPermissions): #ÄNDRA TILL tokenID här!
    
    mycol = connectDB('Employees') 
    
    query = {"username": username} #ÄNDRA TILL tokenID här!

    employee = mycol.find_one(query)

    
    if employee['permissions'] == requriedPermissions:
       return True
    else:
       return False

#@app.route('/admin/loginpost',methods = ['GET','POST'])
#def AdminLoginPost():
 #   mycol = connectDB('Employees') 
  #  username = request.form["username"]
   # password = request.form["password"]

    #query = {"username": username}

    #employee = mycol.find_one(query)
    #if password == employee['password']:

     # response = make_response(redirect(url_for('AdminDashboard')))
        
        #tokenID = uuid.uuid4().hex
        #tokenID == employee['tokenID']
      #  response.set_cookie('username', password) #ÄNDRA TILL tokenID här!
       # return response
    #else: 
     #   return render_template('customerror.html')

#@app.route('/admin/login')
#def AdminLogin():

 #   return render_template('adminloginpage.html')

@app.route('/dashboard')
def dashboard():
    if g.user:
        return render_template('dashboard.html')

    return redirect(url_for('employeelogin'))


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']

    return 'Not logged in!'

@app.route('/logout')
def dropsession():
    session.pop('user', None)
    return render_template('logout.html')

@app.route('/order/menu')
def ordermenu(): 
    mycol = connectDB('Menu') 
    return render_template('ordermenu.html', menu=mycol.find())
    



if __name__ == '__main__':
    app.run(debug=True)
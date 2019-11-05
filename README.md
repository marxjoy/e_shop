# Application for placing orders and generating invoices

## 
* [General info](#general-info)
* [Setup](#setup)
* [Technologies](#technologies)

## General info
Simple Django shop application for placing orders and generating invoices.
Anonymous user:
* see all products in shop
* see product detail
* search products by name or manufacturer
* register Customer account
* login
* reset password
 
There are two roles in the application:
* Customer
* Seller

##Seller
To create Seller account log as SUPERUSER in Django Admin at
```
/admin
```
Add new user or choose user from exisiting.
In Groups panel add sellers to chosen groups.

In Setup section there is a optional
creating sample Seller account. Credentials are below.


Seller can:
* add new product
* delete product
* update product


##Customer
To create Customer account register on page. 
Customer can:
* add product to cart
* remove product from cart
* update quantity of product in cart
* make order

After placing order email is sent to Customer 
with invoice in pdf format in the attachment.


## Setup
Install requirements 
```
pip3 install -r requirements.txt
```
Make migrations
```
python manage.py makemigrations
python manage.py migrate
```
Install fixture with SELLERS group:
 ```
python manage.py loaddata sellers.json
```
(Optional) Install fixture with sample seller account:
 ```
python manage.py loaddata sample_seller.json
```
Sample seller credentials:
```
login: clerk
password: not4sale
```
Install fixture with sample products:
 ```
python manage.py loaddata sample_products.json
```
Sync database:
```
python manage.py migrate --run-syncdb
```
Run server:
```
python manage.py runserver
```

## Technologies
Project is created with:
* Django==2.2
* Pillow==6.2.0
* sorl-thumbnail==12.5.0
* WeasyPrint==50

Database:
* SQLite

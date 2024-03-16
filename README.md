E-Commerce Web Application
This is a Django-based e-commerce web application where users can buy and sell products. It allows administrators to manage products, orders, and customers efficiently.

Installation
To run this application locally, you need to install the following Python libraries using pip:

bash
Copy code
pip install django pillow
The libraries you need to install are:

Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
Pillow: A Python Imaging Library (PIL) fork that adds support for opening, manipulating, and saving many different image file formats.
Features
Admin Features:
Add, remove, and update products.
Manage orders: view, complete, and cancel orders.
Add, remove, and update customer information.
Customer Features:
Browse products and add them to the cart.
Update the cart: change quantities or remove items.
Proceed to checkout and place orders.
View past orders and order status.
Usage
Clone this repository to your local machine.

bash
Copy code
git clone https://github.com/mehakpreetkaur21/E_commerce.git~
Navigate to the project directory.

bash
Copy code
cd e-commerce
Run the Django migrations to set up the database.

bash
Copy code
python manage.py migrate
Start the development server.

bash
Copy code
python manage.py runserver
Open your web browser and go to http://127.0.0.1:8000/ to view the application.

Accessing the Admin Interface
To access the Django admin interface, go to http://127.0.0.1:8000/admin in your web browser. Log in with your admin credentials to manage the site.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

License
This project is licensed under the MIT License.

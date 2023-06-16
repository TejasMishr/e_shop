# Adiham Shopping

This is a Python program that allows users to sign up and log in to an e-commerce website named Adiham Shopping. The program uses a MySQL database to store user information and order details.

## Installation

This program requires the following software to be installed on your system:

- Python 3.x
- MySQL Server

To install the necessary Python packages, run the following command:

```
pip install mysql-connector-python
```

## Usage

To use the program, follow these steps:

1. Run the `connection` script to connect to the MySQL database.
2. Choose between logging in or signing up.
3. If signing up, enter your phone number, user ID, and name. If logging in, enter your phone number and user ID.
4. After logging in, you can start browsing the items and placing orders.


This is a program that allows a user to select a category of products and navigate through different levels of subcategories to finally
select and view details of a specific item.

The program starts by displaying three categories - Electronics, Grocery, and Home Decor. The user is asked to choose a 
category by entering a corresponding number. If the user enters an invalid choice, the program displays an error message 
and prompts the user to choose again.

If the user selects Electronics, the program displays three subcategories - Mobiles, Laptops, and LED TVs.
 The user is again asked to select a subcategory by entering a number. If the user enters an invalid choice,
 the program displays an error message and prompts the user to choose again.

If the user selects Mobiles, the program displays different series of smartphones available from Samsung.
 The user can choose a series and then select a specific smartphone model to view its details, i
ncluding key features, price, and rating.

The program also stores the name of the selected item in a global variable called zz. 
This variable can be used later in the program to perform additional actions with the selected item.

Overall, this program provides a basic framework for building a more extensive e-commerce platform,
allowing users to browse and purchase products online. Additional features, such as user accounts, 
shopping carts, and payment gateways, can be added to enhance the functionality of the program.

The user is asked to enter their payment details, including their card number, CVV, and OTP,
 and then the payment is processed and stored in a database.
 The user is then given the option to view their account details, 
cancel their order, or see all orders.
The "About us" option provides information about the developers of the program.



## Contributing

If you find any bugs or issues with the program, feel free to create a pull request or an issue in this repository. 

## Credits

This program was written by a developer @tejasmishr & prachi 

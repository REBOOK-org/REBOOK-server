# Rebook Project 

Welcome to the Rebook project repository! Rebook is an e-commerce platform specifically tailored for buying and selling used books.

## Overview

Rebook is built using the Django web framework for the backend. It provides users with the ability to upload books they want to sell and browse through a catalog of available books to purchase from other users. The platform facilitates the exchange of used books, allowing users to discover new reads while also providing a platform for selling books they no longer need.

## Features

- **User Authentication**: Users can sign up, log in, and manage their accounts securely.
- **Book Listing**: Users can upload details of books they want to sell, including title, author, description, condition, and price.
- **Book Search**: Users can search for books based on book name
- **User Profile**: Users can view and edit their profiles, including personal information and uploaded books.
- **Admin Panel**: Admins have access to an admin panel to manage users, books, orders, and site settings.

## Our Commit Style

- **feat**: A new feature is introduced with the changes
- **fix**: A bug fix has occurred
- **chore**: Changes that do not relate to a fix or feature and don't modify src or test files (for example updating dependencies)
- **refactor**: Refactored code that neither fixes a bug nor adds a feature
- **docs**: Updates to documentation such as the README or other markdown files
- **style**: Changes that do not affect the meaning of the code, likely related to code formatting such as white-space, missing semi-colons, and so on.
- **test**: Including new or correcting previous tests
- **perf**: Performance improvements
- **ci**: Continuous integration related
- **build**: Changes that affect the build system or external dependencies
- **revert**: Reverts a previous commit


## Setup Instructions

To set up the Rebook project locally, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:
    ```
    git clone https://github.com/REBOOK-org/rebook-server.git
    ```

2. **Navigate to the Directory**: Enter the project directory:
    ```
    cd rebook-server
    ```

3. **Create Environment**: Create Virtual Environment:

    For macOS and Linux
    ```
    python -m venv env
    source env/bin/activate
    ```
    For Windows
    ```
    python -m venv env
    env\Scripts\activate
    ```

4. **Install Dependencies**: Install the required dependencies using pip:
    ```
    pip install -r requirements.txt
    ```

5. **Database Migration**: Run migrations to create database schema:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create Superuser (Admin)**: Create a superuser to access the admin panel:
    ```
    python manage.py createsuperuser
    ```

7. **Run the Development Server**: Start the Django development server:
    ```
    python manage.py runserver
    ```


## Contributing

Contributions to the Rebook project are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

## Contact Us
For any inquiries or support, feel free to contact us.
 #### Abeer Mosaad:

* [LinkedIn](https://www.linkedin.com/in/abeermosaad/)
* [Twitter](https://twitter.com/Abeer_MOsaad0)

 #### Yousef Abdoawoud:

* [LinkedIn](https://www.linkedin.com/in/abodawoud/)
* [Twitter](https://twitter.com/Abodaawoud)


<hr>
Thank you for using Rebook! Happy buying and selling books :) 📚

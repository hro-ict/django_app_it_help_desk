# Django IT Helpdesk Ticketsystem Project

This project is developed using the Django web framework and run in a virtual environment.

## Getting Started

This guide provides general information on how to set up the project and run it in a virtual environment.

### Requirements

To run the project, you will need the following software and tools:

- Python 3.9.4
- pip (Python package manager)
- QR code for admin login. Scan the QR code below with any authenticator app (such as Google Authenticator, Microsoft Authenticator). Then, generate an OTP code to log in as an admin

 ![OTP QR Code](https://github.com/hro-ict/django_app_it_help_desk/blob/main/bweb1/bweb1/otp.png)



### Installation

1. Clone the project:

    ```bash
    git clone https://github.com/hro-ict/django_app_it_help_desk
    ```



2. Go to projectfolder:

    ```bash
    cd \django_app_it_help_desk\bweb1\django_app_it_help_desk\bweb1
    ```

3. Create a virtual environment:

    ```bash
    python3 -m venv myenv
    ```

4. Activate the virtual environment:

    - For Windows:

        ```bash
        myenv\Scripts\activate
        ```

    - For macOS and Linux:

        ```bash
        source myenv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Create the database and start the application:

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

7. Navigate to `http://localhost:8000` in your browser.

## Usage

### Logging in as Admin

To log in as an admin, follow these steps:

1. Click on Login as Admin at Home Page.

2. Enter the following credentials:
   - Username: admin@ithelpdesk.nl
   - Password: Admin1234

3. Next, you'll need to provide a one-time password (OTP) for authentication. Follow these steps to generate an OTP token using an authenticator app:

   - Open your authenticator app (such as Google Authenticator, Microsoft Authenticator).
   
   - If you haven't already, scan QR code above.
   
   - Once the account is added, the app will generate a new OTP token every few seconds.
   
   - Enter the current OTP token from the authenticator app into the provided field on the login page.

4. After entering the OTP token, click on the "Login" button to access the admin dashboard.



## Contributing

If you would like to contribute, please feel free to make suggestions or submit a pull request.



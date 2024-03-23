# Django IT Helpdesk Ticketsystem Project

This project is developed using the Django web framework and run in a virtual environment.

## Getting Started

This guide provides general information on how to set up the project and run it in a virtual environment.

### Requirements

To run the project, you will need the following software and tools:

- Python 3.9.4
- pip (Python package manager)
 -QR code for admin login

 ![OTP QR Code](https://github.com/hro-ict/django_app_it_help_desk/blob/main/bweb1/bweb1/otp.png)

![screenshot](https://github.com/hro-ict/django_app_it_help_desk/blob/main/bweb1/bweb1/otp.png)

### Installation

1. Clone the project:

    ```bash
    git clone https://github.com/hro-ict/django_app_it_help_desk
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv myenv
    ```

3. Activate the virtual environment:

    - For Windows:

        ```bash
        myenv\Scripts\activate
        ```

    - For macOS and Linux:

        ```bash
        source myenv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Create the database and start the application:

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

6. Navigate to `http://localhost:8000` in your browser.

### Usage

Information about how to use this project will go here.

## Contributing

If you would like to contribute, please feel free to make suggestions or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

# Django IT Helpdesk Ticketsystem Project

This project is developed using the Django web framework and run in a virtual environment.

## Getting Started

This guide provides general information on how to set up the project and run it in a virtual environment.

### Requirements

To run the project, you will need the following software and tools:

- Python 3.9.4
- pip (Python package manager)
 -QR code for admin login


![OTP QR Code](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAcIAAAHCAQAAAABUY/ToAAACk0lEQVR4nO3awW3DMAyFYQIewCN59YyUAQyoEclHqZYTFD22vw5JHPHLiZAoKtZ+OR6GRCKRSCQS+Yek5dj6N9vrcT9fE0+z9uifHq8pf4xxIJGr9If23Prr+ZrrKCaeHuo/tLUpGIm8SA/ocz3dXtnX5/aMiokuPUGRyM/SA45r4pkhkT+VD0887YeJYlVDIj9Jf4u5PvZvW2E+ft4/kf9c5thix3vzoigkcpXXEee4qqluQ5DIWUbBFA0BH94VaOfUFdB3SOQbqS1Oj5Y/NOqnyEPV6khku+5lmX3RhDxaZuToD2hBO5ddEImUjNBMPLNsaccBr5JR4UjkVUapXUX3nue4qabKnsGSfUhk5FKEtizEm6JGzlnew5kEEjlLT73sLFV8diJPhexN/QEkcpEjBZWHp5YxH5GRViUWEnmVkWmegvOOVxN1c7KeBZFIJd63ajyL85rQPVzkIhJ5I0c1HiloeuxRiXxVQyLv5fjGxj/VruXUU8UWEvlpFxwjsvIROae2ZXxCIleZ3ewsonS7n0WUDnNeZ12rcSRSsk3VuAJyLVM1bvpxJHKR/nXGV/ZlQC1tu/4F0JDIRerMZjaiMudG69v0H1skcpWxbsVvtDalW6RgjKeOegcSucjRO5rSramVFAe82g+RyBs5liftgnVbqyJKCbpWUkhka9EVyDWqet1xmIslqxqTt50lJHIakXhjVGcptsd6QSKX7DOzaj1OodXhjsTLZEQiF+kPo1bqIypv/1R3I5Z3uUjkKqdqPGslzznxS3sJiXwvp80u4zdV6KqukMiPMrsC2vsyqjLSx4FE3kh/k8xGttqR8dLq5qQhkavMUZVU8HFVoq7Aes+LRLZfDiQSiUQikcg/Ir8AYeNN7G4WOa0AAAAASUVORK5CYII=)


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

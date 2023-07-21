#### michochoprogrammer

# DesignHive 
DesignHive is a course web application for learning technology based remote skill like graphic design, web design, network marketing and the likes. It is a smart dynamic course app which tracks your progress, gives professional tips on productivity, and even offer job offers if available after the end of any course on DesignHive. 

## SetUp - Development server
1. Create a virtual environment using the following command:
  ```
  python3 -m venv env
  ```
  or 
  ```
  python -m venv env
  ```

2. Activate the virtual environment:

- For Windows:
  In Powershell terminal of the root directory
  ```
  cd env
  Scripts\activate
  ```
  In Command Prompt terminal of the root directory
  ```
  env\Scripts\activate
  ```

- For macOS/Linux:

  ```
  source env/bin/activate
  ```

3. Install the required libraries by running the following command:

    ```
    pip install -r requirements.txt
    ```
    This will install all the libraries and packages used.

## Running the Application

To run the server, execute the following command:

    ```
    python manage.py runserver
    ```
    This will serve the app on port 8000
    On your browser, navigate to http://127.0.0.1:8000

## Usage
### Sign In 
By default, an account with admin previledge is already created;
Login with: 
email - admin@gmail.com
password - ilovethis

### Sign Up
To signup, fill the credentials with the appropriate format. A flash message will show up notifying that an account has been created for the user and logged in.

### Start Course
To start a course, navigate to the course page and choose among the available courses.

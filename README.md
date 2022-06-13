## Project Description
A django based application that is a replication of the instagram app. Users are able to log in, register if they have no accounts.Like pictures and comment on pictures as well as search users based on their profile.Users are also able to update their profiles and add posts.
## Link to Live Project
https://bekitainsta.herokuapp.com/

## Author
Becky Ocholla
## Setup Instructions
#### Cloning
* $ git clone https://github.com/BECKY-OCHOLLA/Insta-clone
* $ cd insta-clone

* $ pipenv install request
* Install and activate a Virtual Environment
* $ pipenv shell
 
#### Set-up a Database
* Set your database User and Password 
* Make Migrations & Migrate
* $ python manage.py makemigrations <DB Name> 

* $ python manage.py migrate 
#### Run the application
* python manage.py runserver 
#### Testing the application
* python manage.py test 
* Open the application on your browser 127.0.0.1:8000.

### Technologies Used
Python
Django
Bootstrap
pillow
crispy forms
### Contact Information
Email- ochollabecky@gmail.com

## license
Copyright (c) 2022 Becky Ocholla

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


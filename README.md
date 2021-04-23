# Gallery
## Description
Galerie is a personal gallery application that you display photos for others to see.

## User Story
* User can view all photos on index page ordered by the date they were posted
* Hovering on an image will reveal more information about it; the title, description, location and time posted.
* User can click on the copy button on an image to copy its url for sharing purposes
* Clicking an image will toggle a modal with an expanded view of the image
* User can search photos based on their categories
* User can browse photos based on the location they were taken


## Author
[Charity Mutoni](https://github.com/CharityMutonii)



## Technologies Used
* Python
* Django
* SQLite3
* Postgres database
* HTML5  
* CSS3
* Javascript
* jQuery
* Bootstrap4
* Google Font API

## Requirements
* This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)
* Once python is installed, install the folowing external libraries provided in the requirements.txt file using pip
* Example:
    * **`pip install django==1.11`**

## Installation and Set-up
To view the app, open the live site link provided below on the README.
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`git clone https://github.com/CharityMutonii/Gallery.git`**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:
    * **`pip install virtualenv`**
    * **`virtualenv venv`**
    * **`source venv/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
* **Step 4** : Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**
* **Step 5** : You can now launch the application locally by running the command **`python manage.py runserver`** and copying the link given on the termnal on your browser.
   * To post photos, run the command  **`python manage.py createsuperuser`** to create an admin account in order to post. Access to the admin panel is by adding the path /admin to the address bar.


## Support and contact details
You can reach out to me through:
* charitytoni0@gmail.com

## Live Site link
You can view the live application by following this 

## License
#### [*MIT License*](LICENSE)
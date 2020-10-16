# Python_school_project_simple_webapp

This a school project that I created with Python / Django tools. 
It is a simple web application called Warehouse that works like a "TO DO list" where you can add some records of companies, goods they sell, make etc. then list between them and delete if needed.
Django framework takes care for most of the manage logic and database stuff (using inbuild SQLite).
This app was tested in Python Virtual enviroment on local computer, so that means it was not tested in real web enviroment.



Most important files to look at:
- WareHouseProject/templates/WareHouseProject -> html files that provides template "How a webpage should look (blue print)"
- WareHouseProject/views.py -> file that takes care of "How should browser render wepage"
- WareHouseProject/models.py -> file which contains stuff for creating "tables in SQLite database"
- WareHouseProject/forms.py -> file that contains forms for user to interact with database (UI)


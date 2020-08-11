# FSND-Project-Capstone
#Final Capstone Project for Udacity

#Project Context:

    The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.
    You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

#Models:

    'Movies' model defined with attributes title and release date
    'Actors' model defined with attributes name, age and gender
  
    You can find the models in models.py file.
    
    # Local Postgres DATABASE details are available in setup.sh file for reference.


#Endpoints: All below Endpoints have been created, please refer app.py file.

    GET /actors and /movies
    DELETE /actors/<int> and /movies/<int>
    POST /actors and /movies
    PATCH /actors/<int> and /movies/<int>


#Auth0 Setup:

    AUTH0_DOMAIN, ALGORITHMS and API_AUDIENCE are all available in the setup.sh file for reference.

    #Roles: All 3 roles have been defined in Auth0 and following permissions as shown for each role below are also defined in Auth0

        Casting Assistant
            get:actors and get:movies
        Casting Director
            All permissions a Casting Assistant has and…
            post:actors and delete:actors
            patch:actors and patch:movies
        Executive Producer
            All permissions a Casting Director has and…
            post:movies and delete:movies

     #Json Web Tokens: You can find JWTs for each role in the setup.sh file to run the app locally.

#Deployment Details:

  - App is deployed to Heroku.
  - URL where the application is hosted - https://navitcastingagency.herokuapp.com.
  - Heroku Postgres DATABASE details are available in setup.sh file for reference.

  Use the above stated endpoints and append to this link above to execute the app either thru CURL or Postman.
  For example: 
      $ curl -X GET https://navitcastingagency.herokuapp.com/actors?page=1
      $ curl -X POST https://navitcastingagency.herokuapp.com/actors
      $ curl -X PATCH https://navitcastingagency.herokuapp.com/actors/1
      $ curl -X DELETE https://navitcastingagency.herokuapp.com/actors/1
      Similarly, you can build these for /movies endpoints too.


#Testing:
  - App has been tested locally using Unittest.
  - App has been tested from the Heroku Deployment thru Postman. You can refer following postman deliverables:
      a. Collection with Scripts: udacity-fsnd-navit-capstone-cagency.postman_collection_heroku.json
      b. Test Run Results: udacity-fsnd-navit-capstone-cagency.postman_test_run_heroku.json


#Thank You!

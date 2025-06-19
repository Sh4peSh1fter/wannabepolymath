1.  A web application has two endpoints - https://<url>/login and https://<url>/register.  
    this web application reading and writing to DB instances were everything is stored.

    - Clients are trying to reach the website and are getting error 500. what should we do?

    The 500 error indicates something went wrong on the server side.  
     First we check the web applications and see if the backend is up and healthy.  
     look at the logs of the web sever or the application.  
     Next thing is to check the DB connectivity. Ensure the DB is up and healthy, the web server can access it (in the network, and with the correct user and credentials). Look at the logs of the DB.

    - We can see the DB is full of requests from the web applications and he just drops some of them.

    to fix this we can scale the DBs and pu a queue between them and the web applications.

    - We put to use some queues that get and redirect all the requests from the web servers to the DBs. Is there a way to optimize the queues redirection to the DBs given the web endpoints?

    When we scale DBs, we use a primary one to which we write all the data to, and a group of secondary DBs that sync and used as disaster recovery in the DB cluster. From the endpoints we know that the login endpoint gets data, sends it to the DB to confirm it and send the answer back. The register endpoint however, gets data, sends it to the DB which writes it down and syncs it with the other DBs. The register action requires the primary DB, while the login action can be done with any DB. So in the queue we can redirect according to the endpoint, to the group of DBs that can satisfy the needs without stressing the primary DB too much.

    Another point of view is the usage of the endpoint. more people will use the login in the day to day, so its more important to give a better user experience to this endpoint then the register one. This can be down by giving a priority in the queue to the login endpoint.

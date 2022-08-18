# snapp trip bootcamp project
## group 2

this project will check some conditions and base on them applies rules and actions.

you have to first run balancer.go file with config.json inside config folder and you can chanage the urls and balancer port. (balancer is on port 8080 and you can change it)
you can also run new nodes and add url on config file for more server and faster response (by default it have two listening port on 8001 and 8002).
load balancer is also uses round robin technique.

server nodes can run by "python manage.py runserver" command and start to send request to servers.

you can add rules, condiotions, actions in "/admin" url.
conditions have 2 types (minimumPrice, you should give number for value) and (userType, you should give either 'B2B' or 'B2C')

you can add new conditions by simply adding function to valuate the conditions by true or false and you should add the name of functions in condition_functions and condioton_functions class.



we also found mistakes from your documents :))))) (MIN and MAX mistake)

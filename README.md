# snapp trip bootcamp project
## group 2
- Ali Alef Khani
- Sara Javaherian
- Ali Hezaeveh
- Mohammad Sadegh Mohammadi
- Sajad Javani

this project will check some conditions and base on them applies rules and actions.
### Load Balancer
you have to first run balancer.go file with config.json inside config folder and you can chanage the urls and balancer port. (balancer is on port 8080 and you can change it)
you can also run new nodes and add url on config file for more server and faster response (by default it have two listening port on 8001 and 8002).
load balancer is also uses round robin technique.

server nodes can run by "python manage.py runserver {8001 or 8002}" command and start to send request to servers.

### Edit Rules, Conditions and Actions
You can add rules, conditions and actions in "/admin" url.
Conditions have 2 types (minimumPrice, you should give number for value) and (userType, you should give either 'B2B' or 'B2C')
#### adding new Conditions
You can add new conditions by simply adding function to valuate the conditions by true or false and you should add the name of functions in condition_functions and condioton_functions class.



we also found mistakes from your documents :))))) (MIN and MAX mistake)

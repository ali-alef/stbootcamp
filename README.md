# Snapp Trip bootcamp project

this project will check some conditions and base on them applies rules and actions.
## group 2
- Ali AlefKhani
- Sara Javaherian
- Ali Hezaveh
- Mohamad Sadegh Mohammadi
- Sajad Javani


### Input
a JSON, must include `'price'`, and other necessary fields for Conditions (e.g. `userType`)

### Output
`applied`: if a rule has applied to price (based on appliedRules length)\
`appliedRules`: list of rule that are applied to input price.

## Load Balancer
you have to first run balancer.go file with config.json inside config folder and you can chanage the urls and balancer port. (balancer is on port 8080 and you can change it)\
you can also run new server nodes and add url on config file for more server and faster response (by default it have two listening port on 8001 and 8002).
load balancer is also uses round robin technique.

server nodes can run by "python manage.py runserver {8001 or 8002}" command and start to send request to servers.

## Edit Rules, Conditions and Actions
You can add rules, conditions and actions in "/admin" url.
Conditions have 2 types (minimumPrice, you should give number for value) and (userType, you should give either `'B2B'` or `'B2C'`)
### adding new Conditions
You can add new conditions by simply adding function to valuate the conditions by true or false and you should add the name of functions in condition_functions and condition_functions class.

## Models
- **Rule**: should have name, type and action (foreign key), type defines the `MARKUP` or `DISCOUNT`
- **Action**:  `percentageDisplacementAmount`, `fixedDisplacementAmount`, `maximumDisplacementAmount`
- **Condition**: Rule (foreign key), type (`userType` or `minimumPrice`), value

## superuser info
**username**: ali\
**password**: Passw0rd$96

(or you can create a new superuser by `python manage.py createsuperuser`)\
\
\
\
**we also found mistakes from your documents :))))) (MIN and MAX mistake)** ⚠️

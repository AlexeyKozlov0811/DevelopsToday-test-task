# DevelopsToday-test-task

## To access an app use link:
https://developstoday-test-task-kozlov.herokuapp.com/
## To run an app locally use commands:

- git clone https://github.com/AlexeyKozlov0811/DevelopsToday-test-task.git
- cd DevelopsToday-test-task
- docker-compose up -d --build

When app is started you will see a message like this:

```sh
[+] Running 2/2
 - Container developstoday-test-task_db_1   Started                                                                7.0s
 - Container developstoday-test-task_web_1  Started                                                                6.1s
```

Now you can access app using link below via browser:
http://127.0.0.1:8000/

## Postman collection to test API:
https://www.getpostman.com/collections/330f14dd9a35d2cbbcb5

### To use collection successfully you need to specify postman environment variables
### For development evnironment:
- base_url = http://127.0.0.1:8000/
### For production evnironment:
- base_url = https://developstoday-test-task-kozlov.herokuapp.com/

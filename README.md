# Task-Manager-with-REST-API

A task management web app with REST API using Django
## Demo

#### The Task Page
![K_S](https://raw.githubusercontent.com/rifatjamil54/Task-Manager-with-REST-API/afterDeadline/demo/task_demo.gif)

#### Filter task by Priority
![K_S](https://raw.githubusercontent.com/rifatjamil54/Task-Manager-with-REST-API/afterDeadline/demo/filter_demo.gif)

## Project Overview

### User Authentication

The project includes user authentication features that allow users to register and log in securely.

### Task App Feature

1. Create task with title.
2. View task details.
3. Update task details.
4. Attach photo with task.
5. Filter task by Priority


## Installation and Setup

To run the project locally, follow these steps:

1. Clone the repository:
```
git clone -b <branchname> https://github.com/rifatjamil54/Task-Manager-with-REST-API.git
```


2. Navigate to the project directory and Create a virtual environment:
```
cd task_manager
python -m venv venv 

```


4. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. Install dependencies, Migrate database, Run development server
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
6. Access the project in your web browser: http://127.0.0.1:8000/

## API Endpoint

### Get All Input Values

- All tasks list: ```GET http://localhost:8000/api/task/```
- Create a task: ```POST http://localhost:8000/api/task/```
  
      In Body:  

      {
        "user": 1,
        "title": "",
        "description": "",
        "d_time": "YYYY-MM-DD",
        "priority": ""
      }
- Retrieve a task: ```GET http://localhost:8000/api/task/{task_id}/```
- Update a task: ```PUT or PATCH http://localhost:8000/api/task/{task_id}/```

      In Body:

      {
        "id": 33,
        "user": 1,
        "title": "hi",
        "description": "hi i am refat",

        "d_time": "2020-01-10T00:00:00Z",
        "priority": "Low",
        "mark": false
        }
- Delete a task: ```DELETE http://localhost:8000/api/task/{task_id}/```

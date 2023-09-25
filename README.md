# Task-Manager-with-REST-API

A task management web app with REST API usin Django
## Demo

#### The Task Page
![K_S](https://raw.githubusercontent.com/rifatjamil54/Task-Manager-with-REST-API/dev.0.0.1/demo/Peek%202023-09-25%2009-29.gif)


## Project Overview

### User Authentication

The project includes user authentication features that allow users to register and log in securely.

### Task App Feature

1. Create task with title.
2. View task details.
3. Update task details.
4. Attach photo with task.


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
- Retrieve a task: ```GET http://localhost:8000/api/task/{pk}/```
- Update a task: ```PUT or PATCH http://localhost:8000/api/task/{pk}/```
- Delete a task: ```DELETE http://localhost:8000/api/task/{pk}/```

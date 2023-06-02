# Take-Home Assignment

This is a prototyping solution for the MFKessai take-home assignment. 

It is implemented in Python 3.11.

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/lo/) - A modern, fast (high-performance), web framework for building APIs. 
I chose it because it is easy to learn, fast to code, and good for prototyping. 
- [Uvicorn](https://www.uvicorn.org/) - An ASGI web server implementation for Python.
- [Pydantic](https://docs.pydantic.dev/latest/) - Data validation library. It is used for validating query parameters.
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM toolkit for SQL. It can help me handle the interaction with the DB, 
allowing me to focus on business logic.

## Directory structure:
```
app/
├── database.py
├── Dockerfile
├── main.py
├── model.py
├── repository.py
├── requirements.txt
├── schema.py
└── validator.py

```
- database.py: sets up the configuration for connecting to a MySQL database
- main.py: implements a FastAPI application
- model.py: defines an SQLAlchemy model for storing transaction data
- repository.py: provides a repository for the CRUD of financial data
- schema.py: defines the `Transaction` model class using the Pydantic for validation
- validator.py: defines the validators for validating query parameters

### Secrets management
Now, the secrets of the database are hard-coded in the `database.py` file. We can use better methods to manage them.

#### Development Environment

The sensitive data can be stored in a separate configuration file called `.env`, 
which is specific to the development environment. This file should not be committed to version control systems. 
The application code retrieves the password from the environment variable. 
This approach allows for easy configuration and avoids exposing passwords in the code. 
I believe this is sufficient for development purposes.

#### Production Environment
We can consider use a secure secrets management system, for example:
- [HashiCorp Vault](https://www.hashicorp.com/products/vault)
- [AWS Secrets Manager](https://aws.amazon.com/jp/secrets-manager/)
- [GCP Secrets Manager](https://cloud.google.com/secret-manager)

These tools provide secure storage and retrieval of sensitive data, including api_key, passwords. 
Access to the secrets can be tightly controlled, and the passwords can be rotated regularly for enhanced security.

## Usage
This project was tested successfully on 
- Ubuntu 18.04.4 LTS
- Docker version 20.10.14, build a224086
- docker-compose version 1.29.2, build 5becea4c

You can run it on your local environment by following these steps:

1. Open the project folder and run the command
```shell
docker-compose up -d
```

2. If all goes well, the app is ready now.
```shell
docker-compose ps

         Name                        Command               State                          Ports
----------------------------------------------------------------------------------------------------------------------
mfkessai_codetest_app_1   uvicorn main:app --host 0. ...   Up      0.0.0.0:8888->8888/tcp,:::8888->8888/tcp
mfkessai_codetest_db_1    docker-entrypoint.sh mysqld      Up      0.0.0.0:3306->3306/tcp,:::3306->3306/tcp, 33060/tcp
```

3. Run the test
```
developer@hostname:/mfkessai$ go test main_test.go
ok      command-line-arguments  0.381s
```

4. You can use `docker-compose down` to stop and remove the service
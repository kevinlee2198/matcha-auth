# matcha-auth

## Background

This is a FastAPI python server that acts as a wrapper around supertokens. Supertokens does not have a Java SDK,
so this auth server will act as an extension of supertokens as recommended by their docs (https://supertokens.com/docs/quickstart/introduction)

> If you are using a backend for which we do not have an SDK, you will have to spin up an additional auth service in a language for which we do have a backend SDK (NodeJS, Python or Golang).

## Start Server

First start up the docker containers for supertokens and postgres with `docker-compose up -d`

Use `docker ps` to check the status of the containers

Then start the FastAPI server with `fastapi dev main.py`

Now go to `http://127.0.0.1:8000/docs` to see swagger documentation of API endpoints

Shut down the docker containers with `docker-compose down`

## Hit the Server

When you’re using SuperTokens (self-hosted or cloud), the Core service exposes several API endpoints under `/auth` in the python server.

For example, I can POST:
`/auth/signup`

```json
{
  "formFields": [
    {
      "id": "email",
      "value": "user@example.com"
    },
    {
      "id": "password",
      "value": "mypassword1"
    }
  ]
}
```

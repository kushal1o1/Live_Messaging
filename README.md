# Live_Messaging
# API Endpoints

## User Endpoints

- **List Users**
  - `GET /api/users/`
  - Retrieves a list of all users.

- **Create User**
  - `POST /api/users/`
  - Creates a new user.

- **Retrieve User**
  - `GET /api/users/{id}/`
  - Retrieves a user by ID.

- **Update User**
  - `PUT /api/users/{id}/`
  - Updates a user by ID.

- **Delete User**
  - `DELETE /api/users/{id}/`
  - Deletes a user by ID.

## Message Endpoints

- **List Messages**
  - `GET /api/messages/`
  - Retrieves a list of all messages.

- **Create Message**
  - `POST /api/messages/`
  - Creates a new message.

- **Retrieve Message**
  - `GET /api/messages/{id}/`
  - Retrieves a message by ID.

- **Messages Between Users**
  - `GET /api/messages/between_users/?sender={sender_id}&receiver={receiver_id}`
  - Retrieves messages between two specific users.

## Authentication Endpoints (Djoser)

- **Token Login**
  - `POST /api/v1/token/login/`
  - Obtain an authentication token.

- **Token Logout**
  - `POST /api/v1/token/logout/`
  - Logout by deleting the authentication token.

- **Register User**
  - `POST /api/v1/users/`
  - Register a new user.

- **Reset Password**
  - `POST /api/v1/users/reset_password/`
  - Request a password reset.

- **Confirm Reset Password**
  - `POST /api/v1/users/reset_password_confirm/`
  - Confirm password reset.

- **Set Password**
  - `POST /api/v1/users/set_password/`
  - Set a new password.

- **Activate User**
  - `GET /api/v1/users/activate/`
  - Activate a user account.

# Blog_Post_Assignment

This is a Django-based project called "Blog_post" that provides a RESTful API for managing blog posts. It includes user registration and login functionality using 
'dj-rest-auth' for secure authentication. The project also integrates JWT (JSON Web Tokens) for enhanced security.

# User Registration and Login

This project uses 'dj-rest-auth' to provide user registration and login functionality. Users can register with a unique username and password. Once logged in, users can access protected APIs and perform actions like creating and updating blog posts

# BlogPost Model

The BlogPost model represents a blog post with the following fields:

Author: A foreign key to the User table, representing the author of the blog post.
Title: The title of the blog post (TextField).
Body: The content of the blog post (TextField).
Created At: The date and time when the blog post was created (DatetimeField).
Updated At: The date and time when the blog post was last updated (DatetimeField).

# JWT Integration

This project integrates JWT (JSON Web Tokens) for secure authentication. To obtain a JWT token, make a 'POST' request to '/api/token/' with the user's credentials. The token can then be used for authentication by including it as a bearer token in the Authorization header of protected API requests.

To refresh a JWT token, make a POST request to '/api/token/refresh/' with a valid refresh token. The refresh token can be used to obtain a fresh access token without having to provide the user's credentials again.



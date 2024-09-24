
# OpenID Connect Playground

This repository contains a simple OpenID Connect (OIDC) playground application, demonstrating the authorization flow using Keycloak as the identity provider. It is prepared for [CNCF Ahmedabad Meetup #13](https://community.cncf.io/events/details/cncf-ahmedabad-presents-cncf-ahmedabad-meetup-13/)

## Overview

The application consists of two main components:

1. **Frontend**: A web application built using HTML, CSS, and JavaScript, which interacts with the user and handles the OIDC flow.
2. **Backend**: A Python application using the Keycloak library, which acts as the OIDC client and communicates with the Keycloak server.

## Setup and Configuration

To run the application, follow these steps:

1. Clone the repository and navigate to the project directory.
2. Create a `.envrc` file in the root directory and add the following environment variables:
```makefile
KEYCLOAK_URL=http://localhost:8080
KEYCLOAK_REALM=meetup
KEYCLOAK_CLIENT_ID=backend
KEYCLOAK_CLIENT_SECRET=XXXXXXXX
```
3. Bring  the stack up via `docker-compose up -d`

## Usage

1. Open a web browser and navigate to `http://localhost:8000`.
2. Click on the "Discovery" button to retrieve the OpenID Provider Configuration.
3. Click on the "Authentication" button to generate an authentication request.
4. Enter the required credentials and click on the "Send Authentication Request" button.
5. Follow the prompts to complete the authorization flow.

## Keycloak configuration

- Create realm named `meetup`
- Create frontend public client `frontend` . Enable the consent.
- Create backend authenticated client `backend` with authorization enabled.
- Create the following
  - Roles: finops_role, sales_role
  - Resources: finops_billing_data, sales_data
  - Policy: finops_policy, sales_policy
  - Permissions: finops_permission, sales_permission
  - Users: user1 with finops_role, user2 with sales_role
- Configure events - Admin, User

## Presentation

- [Open Source Identity and Access management with Keycloak](https://docs.google.com/presentation/d/1LTBFjt6YXI9lkpFpnGBXiTkfybfwtjLbn9VfQ1l0lRI/edit?usp=sharing)

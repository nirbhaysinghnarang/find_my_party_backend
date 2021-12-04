Backend written in Flask for Find My Party. Team Submission for Cornell AppDev HackChallenge 2021.

Database model:
- A relational many-to-many database.
- There are two classes - Party and User - that are linked with an association table. 

Deployed on (https://findmypartyhck1.herokuapp.com/api/)

Routes:

- "/api/parties/" - Get all parties. (GET)
- "/api/parties/host/" - Host a party. (POST)
- "/api/party/int:party_id/" - Get a party by its ID. (GET)
- "/api/users/" - Add a new user. (POST)
- "/api/user/int:user_id" - Get user by ID. (GET)
- "/api/party/int:party_id/attend/" - Attend a party by its ID. (POST)
- "/api/party/int:party_id/attendees/" - Get all attendees of a party by its ID. (GET)
- "/api/user/int:user_id/parties/" - Get all parties hosted by a user. (GET)
- "/api/user/email/" - Get user by email, created because GoogleSignIn is used for auth. (GET)
- "/api/user/delete/" - Delete user by email in request body. (DELETE)
- "/api/party/int:party_id/delete/" - Delete party by party ID. (DELETE)

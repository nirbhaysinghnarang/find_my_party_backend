Backend written in Flask for Find My Party.
Team Submission for Cornell AppDev HackChallenge 2021.

Deployed on (https://findmyparty-wj6gklp34a-ue.a.run.app/)

Routes:

1. "/api/parties/" - Get all parties. (GET)
2. "/api/parties/host/" - Host a party. (POST)
3. "/api/party/<int:party_id>/" - Get a party by its ID. (GET)
4. "/api/users/" - Add a new user. (POST)
5. "/api/user/<int:user_id>/" - Get user by ID. (GET)
6. "/api/party/<int:party_id>/attend/" - Attend a party by its ID. (POST)
7. "/api/party/<int:party_id>/attendees/" - Get all attendees of a party by its ID. (GET)
8. "/api/user/<int:user_id>/parties/" - Get all parties attended by a user. (GET)
9. "/api/user/email/" - Get user by email, created because GoogleSignIn is used for auth. (GET)
10. "/api/user/delete/" - Delete user by email in request body. (DELETE)
11. "/api/party/<int:id>/delete/" - Delete party by party ID. (DELETE)



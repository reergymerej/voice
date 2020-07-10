# voice_db

This is the only lambda that will interact with the database.  This allows other
routes to call it without spreading db logic and auth everywhere.

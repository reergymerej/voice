# voice_db

This is the only lambda that will interact with the database.  This allows other
routes to call it without spreading db logic and auth everywhere.

`psycopg2/` is in the package.zip, but not included locally.  This is because
locally, use the one from Pipenv.  In Lambda, use the one in the zip.`

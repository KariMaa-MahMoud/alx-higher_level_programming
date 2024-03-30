<<<<<<< HEAD
#!/bin/bash
# sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -sX DELETE $1 -L
=======
#!/bin/bash
# Sends a DELETE request
curl -s "$1" -X DELETE
>>>>>>> bda9b6b4a0c239bb9b2b7b5c180f2fd0e5d219e4

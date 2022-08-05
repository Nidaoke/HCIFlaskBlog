#moved code to testfile.py

# makes the create_app function inside 
# website folder available from this file
from website import create_app

if __name__ == "__main__":
    #call create_app function
    app = create_app()

    # updates the server when changes are made in python so you 
    # don't have to restart it manually 
    app.run(debug=True)

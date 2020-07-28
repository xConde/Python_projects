# Python_projects
### Series of small python projects to re-explore the languages libraries and review syntax. 

## Dictionary_JSON 
#### Define.py : dictionary.json
Loads a JSON to find a definition for a users word. If the user slightly mistypes the word or is close 
it will try to identify the next best thing by using an imported library get_close_matches. 


## Stop_Discord 
#### Block_Websites.py
Stops user interaction during the period of 0600 to 1700 (6AM-5PM) to websites specified in website_list
to encourage productivity. Manages host file for blocked websites. Currently set to check every 10 seconds.

#### Block_Applications.py
Stops user interaction during the period of 0600 to 1700 (6AM-5PM) to programs specified in program_list
to encourage productivity. Utilizes tasklist to check if a task that is blocked is running. Currently set to check every 10 seconds.

## Library_Collection
#### Library_Frontend.py, Library_Backend.py : library.db
Allows user to manage a library database through a GUI. User may modify records through adding, deleting, and updating. Library_Frontend.py utilizes tkinter to create GUI, while Library_Backend.py creates and manages the database through sqlite3. 

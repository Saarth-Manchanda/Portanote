
                                                            // PORTANOTE //
                                                     Interactive Dot Matrix Edition

<img width="1366" height="766" alt="image" src="https://github.com/user-attachments/assets/51b54f53-d033-44d2-b063-faf67011e248" />


Portanote is a minimalist, retro-futuristic web-based note-taking application. 
It pairs a brutalist, monospaced dark-mode interface with a fluid, cursor-reactive 
dot matrix canvas background. Notes are saved securely to a PostgreSQL database 
and mapped to catchy, random 5-letter word codes for instant sharing and recall.

-------------------------------------------------------------------------------
[+] FEATURES
-------------------------------------------------------------------------------

* Interactive Dot Matrix Background
  An HTML5 Canvas grid that dynamically repels and highlights dots based on 
  cursor movement and touch interactions.

* Word-Based Identifiers
  Notes are accessed via memorable 5-letter word keys (e.g., "apple", "beach", 
  "orbit") instead of cryptic UUIDs or long numeric IDs.

* Persistent PostgreSQL Storage
  Integrated with Neon (or any standard PostgreSQL database) via environment 
  variables using `psycopg2`.

* Instant Clipboard Actions
  One-click copy buttons for note text and shareable URLs with smooth visual 
  tooltips.

* Dynamic Typewriter Placeholder
  Cycles through helpful usage prompts in the text area when empty.

* Responsive Brutalist UI
  Optimized layout with sharp borders, hard shadows, and clean scaling across 
  mobile and desktop screens.

-------------------------------------------------------------------------------
[#] TECH STACK
-------------------------------------------------------------------------------

* Backend:  Python, Flask
* Database: PostgreSQL (psycopg2)
* Frontend: HTML5, CSS3, Vanilla JavaScript, HTML5 Canvas API
* Fonts:    JetBrains Mono (Google Fonts)

-------------------------------------------------------------------------------
[>] GETTING STARTED
-------------------------------------------------------------------------------

1. Prerequisites
   Ensure you have Python 3.8+ installed along with a PostgreSQL connection 
   string (e.g., from Neon.tech or a local instance).

2. Clone & Setup
   Save the code as `app.py`.

3. Install Dependencies
   $ pip install flask psycopg2-binary

4. Set Environment Variables
   Set your PostgreSQL connection string:

   - Linux / macOS:
     $ export DATABASE_URL="postgres://user:password@host:5432/dbname?sslmode=require"

   - Windows (CMD):
     > set DATABASE_URL="postgres://user:password@host:5432/dbname?sslmode=require"

   - Windows (PowerShell):
     > $env:DATABASE_URL="postgres://user:password@host:5432/dbname?sslmode=require"

5. Run the Server
   $ python app.py

   Navigate to http://localhost:5000 in your browser.

-------------------------------------------------------------------------------
[*] USAGE GUIDE
-------------------------------------------------------------------------------

1. Creating a Note
   Type or paste content into the editor and click [ Save Note ]. A random 5-letter 
   code will be assigned and the page will redirect to the note's shareable link.

2. Accessing a Note
   Enter a valid 5-letter code into the top search bar and click [ Open Note ], 
   or directly navigate to `/<code_name>` in your browser address bar.

3. Deleting a Note
   Click the red [ Delete ] button on an existing note's page to permanently 
   remove it from the database.

-------------------------------------------------------------------------------
[@] AUTHOR
-------------------------------------------------------------------------------

Created by Saarth Manchanda
GitHub: https://github.com/Saarth-Manchanda

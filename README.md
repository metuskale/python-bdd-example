# Write a breaf documentation here

# Structure

Project_name
├── config # contains all hardcoded strings and settings
|   ├── defaults.yaml # default configuration values to be overriden by the environment
|   ├── production.yaml # production configuration values
|   └── __init__.py # config loader
├── features
|   ├── steps # contains all test steps
|   |   ├── common.py # common steps between features
|   |   └── search.py # feature specific steps
|   ├── environment.py # Setup/Teardown environment. Includes all hooks.
|   └── search.feature # Feature file that contains test scenarios for the search feature
├── lib # contains services, handlers, and other scripts
├── unittests # tests for all lib code
├── .gitignore # list of files to ignore when pushing to github
├── README.md # readme
└── requirements.txt # list of project package requirements
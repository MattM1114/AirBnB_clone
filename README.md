0x00 AirBnB clone - The console
In this Repository you will find a implementation of a AirBnB clone. In this first step is implementation of the Console. Commands for create, update, destroy, show and manage diferent classes and attributes for the items that the app will offer to the users.

The console
create your data model
manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file) The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored. This abstraction will also allow you to change the type of storage easily without updating all of your codebase. The console will be a tool to validate this storage engine
Command interpreter
Our command interpreter looks like a mini shell and allow us manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object
Objectives of project
How to create a Python package
How to create a command interpreter in Python using the cmd module
What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
How to manage datetime
What is an UUID
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function
Content of Directory
Models Folder: Classes of the project. BaseModel is the parent Class. The other classes (amenity, city, place, review, state, user) inherit from BaseModel and specify others attributes for itselfs.
Tests Folder : Unittests for the project
AUTHORS: Information about the authors
console.py: Eceutable file for the console
file.json: JSON file with all information of instances

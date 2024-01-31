# Benjamin Davies Workbook A

## Question 1

    Flask is a backend framework built for python, flask is great for small applications, but it doesn’t scale well. As your your project becomes larger and you require more views it becomes more difficult to maintain your code. When your application grows in size or complexity, you may want to structure your code in a differently to keep it maintainable and clear. 

## Question 2

    Identify a database management system (DBMS) commonly used in web applications (including Flask) and discuss the pros and cons of this database oracle, MySQL and PostgreSQL

## __Question 3__

### _Discuss the implementation of Agile project management methodology_

    Before implementing an Agile project management (APM), one must see whether an APM is appropriate for the project and the company. Agile requires a willingness from all parties to work management and devs need to adapt an agile system so it may succeed. Agile has a strong focus on user stories and users' end experience, it does this by getting the developers to answer the following sentence when planning a feature or branch, "As a who', I 'want to', so 'that why'". By looking at the application from different perspectives developers can gain greater insight into how an application or feature should function. The benefits of choosing an agile system for a project include:
            
            1. Increased Skateholder involvement, allowing for a clear and direct path to meet the client's application needs. 
            2. Greater Team comradery and improved team support and morale.
            3. Faster application delivery teams work on small parts of an application at a time instead of the entire thing.
            4. Improved risk management and ability to identify potential problems in the application earlier.

    An (APM) system is best suited to projects that have an unknown or open-ended amount of requirements/features this also includes projects whose plan is likely to change frequently. One common Agile project management framework in software development is called (scrum). Scrum utilizes a fixed length of work, these are called sprints. Each sprint contains 4 parts.

            1. Sprint Planning, A meeting among the team to determine what should be completed in the upcoming sprint.
            2. Demonstration, A chance to show other team members what they've completed in that sprint.
            3. Daily Standup, A chance for the teams to collaborate.
            4. Review, A review of the sprint, to see what went well and what can be improved.

    Another Agile framework called kanban, Kanban is different as instead of sprints it uses "Work In Progress limits" or "WIP" for short, Kanban has a continuous stream of tasks or cards that should be completed. The amount of work to be completed depends on the size of the team and is determined before production starts. Kanban is typically faster than Scrum and offers the ability to react faster to application changes. 
![Agile cycle](Images/AGILE%20CYCLE.png)

## __Question 4__

### _Provide an overview and description of a standard source control workflow_

    Project source control is crucial when planning a project, good source control will allow developers to maintain backups, keep a history, view changes, experiment with features, and collaborate on projects. There are two types of source control repositories they are centralized repositories or distributed repositories.
    
        - A centralized repository is a single server that holds all of the data on the project.
        - A distributed repository is where each developer clones the repository to their computer. 
    
    While Version control doesn't affect our workflow it's important to understand where our data is being stored. The most common distributed repository at the moment is Github others include BitBucket and SourceForge. A complex Web Application is made up of many different components, when developing an application we break it into more manageable pieces these are called features. This is great in principle but problems can arise when we have more than one developer or team working on an application. If we have more than one feature that shares the same module of code then we need to be careful when commit our changes, Pre-existing features or features that are in development may depend on this module. This is why repositories provide us with information about the changes to our code. 

    In modern-day programming, the main branch of the project sometimes referred to as the trunk is created at the beginning development phase. Then branches are formed for each feature of the application, by creating features separate from the main source control we can properly test and review our code before making changes to the application. Once the testing and review phase is complete we will merge the code into the main and the application will have gained a new version. Features can be created before and after deployment of the application. The stages of source control workflow can be defined in order:

        1. Create a new branch for the intended feature
        2. Develop the new feature
        3. Commit changes to branch
        4. Create a pull request
        5. Review and test new feature with the team lead
        6. Merge the new feature into the main  
    
    The image below illustrates how we would add a new feature to an application. 
![Source Control Workflow](Images/source_control_workflow.png)

## __Question 5__

### _Provide an overview and description of a standard software testing process (e.g. manual testing with example)_

    A critical part of developing web applications is testing, when we test an application we aren't necessarily looking for syntax errors or bugs in our code but rather the structure of the application. We can break an application into different categories and then ask ourselves the following questions about our application:

        1. Functionality - does the website do what we want it to?
        2. Useability - is the easy to use and appeals to the client/customers?
        3. Application Interface - does the application talk to the web server and database correctly and handle errors?
        4. Compatability - what browsers/devices is it compatible with?
        5. Performance - how does it perform with search engines are the load speeds within a reasonable timeframe?
        6. Security - is our stored data secure?

    Manual testing is one type of software testing we can conduct, it consists of first understanding what the desired output should be from the application, then creating a plan to test the application, executing the test, recording the results of the test, and then updating or modifying the application if required. This process can be repeated as many times are necessary until the application's desired output is reached. An example of how we can test an application's Interface is checking for errors or inconsistencies between the application web server and the database. This process is sometimes referred to as Workflow testing or end-to-end (E2E) testing. The goal of E2E testing is to make an HTTP request to the web server and then the web server will perform an action or query depending upon the request and then return something to the user. An example of E2E testing is checking if a user's login credentials are correct. To test this we would have to

            1. Make an HTTP POST request to the web server with the user's login credentials
            2. The webserver will query the database to check if the post request data matches users' login credits
            3. After that the web server will return the result to the user

    A coding example of this is shown below.

## Question 6

    Discuss and analyse requirements related to information system security and how they relate to the project

## Question 7

    Discuss common methods of protecting information and data and how you would apply them to the project

## Question 8

    Research what your legal obligations are in relation to handling user data and how they can be met for the project

## Question 9

    Describe the structural aspects of the relational database model. Your description should include information about the structure in which data is stored and how relations are represented in that structure.

## Question 10

    Describe the integrity aspects of the relational database model. Your description should include information about the types of data integrity and how they can be enforced in a relational database.

## Question 11

    Describe the manipulative aspects of the relational database model. Your description should include information about the ways in which data is manipulated (added, removed, changed, and retrieved) in a relational database.

## Question 12

    Conduct research into a web application (app) and answer the following parts:  a. List and describe the software used by the app.
        b. Describe the hardware used to host the app.
        c. Describe the interaction of technologies within the app
        d. Describe the way data is structured within the app
        e. Identify entities which must be tracked by the app
        f. Identify the relationships and associations between the entities you have identified in part (e)
        g. Design a schema using an Entity Relationship Diagram (ERD) appropriate for the database of this website (assuming a relational database model)

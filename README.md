# System-Monitor-Service-Challenge
This challenge involves creating a system monitor similar to a task manager. The objective is to develop a service class that can run multiple services on individual threads, collect system information, and present it graphically.

## Task 1: Create Service Class
Design and implement a service class that allows two services to start and run individually on separate threads. One service should periodically collect system information (e.g., CPU usage, memory usage) and send it as JSON. The other service should receive this data into a queue and iterate through the queue to present updates on a graph. Ensure that the services can be managed and controlled effectively.

### Expected Result
A base service class with start, stop, and run methods.
Two concrete service implementations: one for data collection and one for data presentation.
Use of threads to run services concurrently.
Thread-safe queue for communication between services.

## Task 2: Flowchart Creation
Analyze a provided piece of code from the project and create an elaborated flowchart that details the system's architecture, including interactions between different components, data flow, and key processes. Use draw.io for creating the flowchart.

### Expected Result
A clear and detailed flowchart illustrating the system architecture.
Identification of key components and their interactions.

## Task 3: Extend the Existing System
Using the code and flowchart from Task 2, implement a new feature or functionality. This could be adding another service, enhancing existing functionality, or integrating additional components. Ensure the new implementation integrates seamlessly with the existing system and follows best practices for code clarity and maintainability.

### Expected Result
New feature or functionality added to the existing system.
Seamless integration with the existing codebase.
Clear documentation and justification for design choices.
Instructions
Structure your code with OOP principles, ensuring clarity and maintainability. Document your approach and results clearly, highlighting any assumptions or decisions made during the implementation. Provide flowcharts for each task using draw.io to illustrate your design and implementation process.

**Good luck!**

# System-Monitor-Service-Challenge
This challenge involves creating a system resource monitor similar to a the graphs displayed in windows task manager. The objective is to develop a service class that can run multiple services on individual threads, collect system information one one service, and present it graphically with another service.
This challenge is losely instructed on purpose (as if you would get the instructions from product department). It is your responssibility to ask for specific details for certain parts of the implementation that are not detailed enough in this document. Try to use your common sense to settle on at least some of those details by your own.
When designing the code using OOP, it is suggested to start with writing an example script of the main file which uses the classes before starting to write the classes and designing the architecture of your code.
For each task, you are required to implement a flow chart (see empty files within `flowcharts` folder). The flowcharts should be created using the opensource draw.io web app and they should illustrate the architecture of the service as a generic class and the flow of each specific implementation of the service and the interaction between them.

## Code evaluation
- Using OOP concepts properly
- Applying design patterns
- Testing edge cases and providing relevant exceptions
- Generic implementation which can be expanded easily
- Clarity for other programmers
- Zero bugs (task 3 is reserved for testing and fine-tuning to resolve all bugs)

## Important instructions
- After cloning the repository. Create a branch called `task_1/[your name or nickname]` and when you are ready, push the branch. Do the same with tasks 2 and 3. **It is recommanded to push all tasks after you complete all of them** in case you will have some modifications you would like to do on previous tasks.
- **It is recommanded to create an experiments package** and conduct there scripts for trying things out before implementing them into your code structure.
- **Do not use chatGPT or other language models for this challenge.** They often provide entire code segments which differ and influence your code design. There are plenty of resources online for multi-threading so you won't need to deal with that.
- Read all tasks before you start. They are incremental.

## Task 1: Create Service Class
Design and implement a service class that allows two services to start and run individually on separate threads. One service should periodically collect system information (e.g., CPU usage, memory usage) and send it as JSON. The other service should receive this data into a queue and iterate through the queue to present updates on a graph. When creating the service class, separate the generic implementation of a service from the specific implementation of the two specified services.
1 second for the periodic collection and transmission is enough and it doesn't half to be super accurate. Make it simple to add other system information variables into the json without requiring to dive in to many segments of the code.

### Expected Result
A base service class with start, stop, and run methods.
Two concrete service implementations: one for data collection and one for data presentation.
Use of threads to run services concurrently.
Thread-safe queue for communication between services.
The data collection service should periodically sample and send system information and the presentation service should simply print to console the received data.

## Task 2: Create the monitor UI
Once you have the two services working properly and sharing data, you can create a UI for monitor. You should deside wether to run the UI from within the presentation service or to run the presentation service on the UI class (or do something else). Either way, remember that the UI should be initiated on the main thread in order to work and that every data that is displayed on the UI might be sent from another thread so you need to figure out what would be a good way to do it while maintaining the a uniform design of your service architecture (it is okay to change the service architecture for this but make sure it aligns with a new design uniformity and doesn't look like an ugly workaround).
Displaying the data as two graphs depending on time which are updated dynamically. Make sure you use the exact time (in seconds) of the time the system information was taken. The graph can be updated as well every 1 second.
You don't half to use pyqt for the UI. A simple matplotlib with two plots (one for each system infromation).

### Expected Result
When running the program, you will see a window with two line charts and proper titles. A nice realtime chart of CPU usage (%) and memory usage (RAM currently used in Mb/Gb) will be displayed.
When closing the 

**Good luck!**

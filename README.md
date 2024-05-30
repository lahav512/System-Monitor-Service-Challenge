# System-Monitor-Service-Challenge
This challenge involves creating a system resource monitor similar to the graphs displayed in Windows task manager (can be done similarly for Mac or Linux). The objective is to develop a service class that can run multiple services on individual threads, collect system information on one service, and present it graphically with another service.

This challenge is closely instructed on purpose (as if you would get the instructions from the product department). It is your responsibility to ask for specific details for certain parts of the implementation that are not detailed enough in this document. Try to use your common sense to settle on at least some of those details on your own.

It is recommended to write your action plan in some rich text file (like *.md or *.docx) in the `documents` folder of this repository to write the instructions in your own words and make each task instruction and requirement explicit.

When designing the code using OOP, it is suggested to start with writing an example script of the main file that uses the classes before starting to write the classes and designing the architecture of your code.
For each task, you are required to implement a flow chart (see empty files within the `flowcharts` folder). The flowcharts should be created using the opensource [DrawIO](https://app.diagrams.net/) web app and they should illustrate the architecture of the service as a generic class and the flow of each specific implementation of the service and the interaction between them (it is fine if flowcharts of two tasks are almost the same). The flowcharts should be expressive enough but don't write every small function or every variable. It should be used for visually reading and understanding the architecture you chose to apply. The specific implementation of functional functions is irrelevant to the flowchart.

You are expected to write this software in Python, but you are allowed to request a different programming language for your choice.

## Code evaluation
- Project structure (don't write everything in a single file, you have an entire branch for yourself)
- Using OOP concepts properly
- Applying design patterns
- Testing edge cases and providing relevant exceptions
- Generic implementation which can be expanded easily
- Clarity for other programmers
- Zero bugs (task 3 is reserved for testing and fine-tuning to resolve all bugs)
- The flowchart is expressive enough to demonstrate the actual structure of your code (if you are not sure if your flowcharts are expressive enough, you can ask)

## Important instructions
- After cloning the repository. Create a branch called `task_1/[your name or nickname]` and when you are ready, push the branch. Do the same with tasks 2 and 3. **It is recommended to push all tasks after you complete all of them** in case you have some modifications you to do on previous tasks.
- **It is recommended to create an experiments package** and conduct their scripts for trying things out before implementing them into your code structure.
- **Do not use chatGPT or other language models for this challenge.** They often provide entire code segments that differ and influence your code design. There are plenty of resources online for multi-threading so you won't need to deal with that.
- **Read all tasks before you start. They are incremental.**
- Upon submission, create a video that illustrates your monitor software besides Windows task manager graphs to prove you get the same graphs.

## Task 1: Create Service Class
Design and implement a service class that allows two services to start and run individually on separate threads. One service should periodically collect system information (CPU usage and memory usage) and send it as JSON. The other service should receive this data in a queue and iterate through the queue to present updates on a graph. When creating the service class, separate the generic implementation of a service from the specific implementation of the two specified services.
1 second for the periodic collection and transmission is enough and it doesn't have to be super accurate. Make it simple to add other system information variables into the JSON without requiring to dive into many segments of the code.

### Expected Result
A base service class with start, stop, and run methods.
Two concrete service implementations: one for data collection and one for data presentation.
Use of threads to run services concurrently.
Thread-safe queue for communication between services.
The data collection service should periodically sample and send system information and the presentation service should simply print to console the received data.

## Task 2: Create the monitor UI
Once you have the two services working properly and sharing data, you can create a UI for the monitor. You should decide whether to run the UI from within the presentation service or to run the presentation service on the UI class (or do something else). Either way, remember that the UI should be initiated on the main thread to work and that every data that is displayed on the UI might be sent from another thread so you need to figure out what would be a good way to do it while maintaining the a uniform design of your service architecture (it is okay to change the service architecture for this but make sure it aligns with a new design uniformity and doesn't look like an ugly workaround).
Displaying the data as two graphs depending on time which are updated dynamically. Make sure you use the exact time (in seconds) of the time the system information was taken. The graph can be updated as well every 1 second.
You don't have to use pyqt for the UI. A simple matplotlib with two plots (one for each system information).

### Expected Result
When running the program, you will see a window with two line charts and proper titles. A nice real-time chart of CPU usage (%) and memory usage (RAM currently used in Mb/Gb) will be displayed.
When closing the window, all running threads should be closed properly.
You can test this monitor by comparing it to a Windows task manager monitor and running programs you know occupy substantial CPU usage or use a decent amount of RAM.

## Task 3: Test and validate
Go through all edge cases and make sure the code is robust. Apply exceptions for the communication between the processes and handle them properly when they are thrown.
Clean up the code and make sure it is readable and that you are proud of it and feel free to show it to another programmer.
Make sure that your code will print an error message if the software someone tries to run this software on a non-supported operating system. It is okay if it runs on only one OS platform (you can use either Windows, macOS, or Linux).
Validate your work by self-criticizing your code based on this list: [Code Evaluation](#code-evaluation).

### Expected Result
The same software from task 2 is running with no bugs. Your code is ready for submission.

## Bonus (recommended): Add more system information
If you already built a generic and modular code, you can easily add more system information to your JSON and sample it periodically the same way you did with CPU usage and memory usage.
From the UI perspective, it can be relatively easy. You can add a configuration file that specifies which system information you would like to see when you are running the software.
Make sure the UI properly adjusts the different configurations and that the user can easily understand what each graph means. When choosing which system information to display, you can take inspiration from the Windows task manager or choose your desired system information to sample and display.

### Expected Result
The user can specify in a configuration file (true or false) for each system information that the software can display in graphs. When running the software, it will display the selected system information in the graphs and organize the graphs and the window size according to the number of displayed graphs. There is no need for dynamic updates from the configuration file. Loading the configuration file once when starting the software will suffice.

## You are in charge here
This challenge is designed to test your independence. You are more than welcome to ask questions for clarifications but you should also use your expertise and make decisions based on coding practices and common sense of the expected result and user experience of using the software.

## Food for thought
This software could be done without creating service architecture. Think why is essential to still choose such architecture for this program. How would it affect adding more complex features for such a monitor?
Remember, when we are building software, we think about what we need now, what we will probably need in the future, and how other programmers will be able to easily contribute to the software and add more features without having to dive into the internals of your code for every simple feature.

**Good luck!**

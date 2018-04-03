This Project is a simple Demonstration of DOS (Denial Of Service) attack, which is entierly for learning purposes and not intended to be used for illegal purposes.

The DOS.py file is the file that performes the attack. 
It's a simple python script that sends the fluid requests through different 50 threads, each thread sending 5000 different request with random numbers to be calculated by the server(Server.js). 

The Server.js file is a node server that accepts simple GET request with two numbers, and performes simple arthimetic maniuplation on it and sends back the response.
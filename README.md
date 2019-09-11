# IoT_Simulator

A  small IoT project that simulates a device, a connection to server with a database, along with a client view and potential control of the device. Main idea is to create a type of infrastructure that will pipeline the data between clients (being devices and users) and the server. This project is very early stage I may add to this solution using gRPC for efficiency reasons.

P.S. I'm just a newb go easy on me.


### Tasks.. So far
- [ ] Create a connection from simulated device to the server
- [ ] Create a simple user client interface to view queried data on request
- [ ] Create a simple db_injection system that saves the data categorized by device UUID, Current status, sensor_value, and timetamp in epochs 
- [ ] Make sure data in transit and in rest and a certain level of encryption
- [ ] More to be added as I think about it
- [x] Created a code that simulates a simple IoT device

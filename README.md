**Hotel Management**

**Scenario**

You have been hired by the Artemis Hotel to create a hotel management system.  The system will be used by the hotel for managing customers bookings and their details.

The program system must be capable of providing the following information:

Hotel Booking, Provide you with Hotel Rooms Info, Room Service, Billing and Record-Keeping.

**Methods**

- Analyse the detailed requirements using suitable methods, i.e. analysis by decomposition of requirements (breaking down the tasks into manageable parts)
- Elements and functions table
- algorithms / pseudocode or flow diagram 
- Show the iterative development of the individual solutions with suitable testing throughout the process. 
- Test the final product with an appropriate test table and evaluate your solution against the detailed requirements you identified in the analysis.

**System Requirements**

- Main Menu options
- Personal details: including type of room and service booked.
- Hotel room details: Type of room, number of persons, number of beds, what is included in the room i.e. on-suite, couch, TV etc.
- Bookings
- Billing and payments
- Record keeping guest records, guests and allocated rooms, vacancy of rooms, room services
- Database CSV document for customer / guests’ details
- Test table to show that the system works.

**

**Example of Functions Required:**

Home()- Function to display the project’s main screen i.e. the home page of the project or you can say the main menu for selecting the desired operation to perform. 

Date(str)- Function to validate date entered by the user/customer. 

Booking()- Function for booking room in hotel by entering user/customer details. 

Room\_Info()- Function to provide users/customers with hotel rooms information(i.e. about room amenities). 

Restaurant()- Function for room service which provides user/customer with the restaurant’s menu card to order food at the room. 

Payment()- Function for payment of hotel room and restaurant bill generation at the time of check-out. 

Record()- Function for keeping records of customers stayed in the hotel. 



Client Requirement 

|**Requirement ID** |**Description** |**Mandatory [M] or desirable [D]** |
| :- | :- | :- |
|1|Main Menu|M|
|2|Personal Details|M|
|3|Room Details|M|
|4|Bookings|M|
|5|Billing And Payments|M|
|6|` `Save Details|M|



Task Table 

|**Requirement ID** |**Description** |
| :- | :- |
|1|Create a main menu|
|2|Input and output personal details|
|4|Check if room is available|
|5|Take payment|
|6|Save as a csv file for details|
|4|Book room|
|3|Change room details|



Flow Diagram

![](Aspose.Words.1d6ccd49-9e00-4d2c-ad15-53ab2be853d8.001.png)

Psuedocode

OUTPUT Menu

SELECT Task

IF Task = 1 THEN

`    `INPUT Date,Beds,Quality

`    `FIND Room IN Rooms

`    `Book Room

END IF

IF Task = 2 THEN

`    `OUTPUT Room Info



Variable Table 

|**Variable Name** |**Description** |**Data Validation** |**Data Type** |
| :- | :- | :- | :- |
|||||
|||||
|||||
|||||
|||||
|||||


Method Table 

|**Method Name** |**Input** |**Process** |**Output** |
| :- | :- | :- | :- |
|GetRooms|N/a|gathers the list of rooms|output all room details|
|ValidInput|anything|validate it that its acceptable|output if it is|
|CastVariable|variable and a datatype|nicely convert to that datatype|the variable|
|SaveRooms|updated rooms|saved the rooms to disk|n/a|
|PrintRooms|n/a|prints all the room details|pritns all the room details|
|ViewRooms|n/a|view all available rooms|pritns the availbalbe rooms|
|PrintRoom|a rooms|n/a|prints the room|
|ViewBookings|list of rooms| returns the not empty rooms|prints rooms|
|AddBooking|list of rooms|change room to be occupied|n/a|
|AddRoom|List Of Rooms|adds a new room|n/a|




Testing Plan

1. Use of Testing to Identify Defects (Explain your test table, the columns you used and what you where testing) 
1. How you will be documenting the testing process (e.g Show screenshots of your testing and explain each step) 
1. Explain any changes you have made to the Solution during testing. (Show any solutions that you came up with after your testing)



Testing** Table

|Test Type|Test Data|Reason|Expected Outcome|Actual Outcome|Pass or Fail?|Actions Required?|
| :- | :- | :- | :- | :- | :- | :- |
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||



Evaluation

**Comparison to designs​**

- Provide a well-developed line of reasoning which is clear and logically structured. The information presented is relevant and substantiated.​
- Discuss the maintainability of the solution. ​
- Discuss potential further developments of the solution. ​
- Discuss any changes and why they are different from the original designs.


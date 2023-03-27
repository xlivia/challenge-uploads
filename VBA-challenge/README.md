# Olivia's VBA Excel Assignment
## UofT Data Analytics Bootcamp Module 2 Challenge 

alphabetical_testing was for testing VBA code

Multiple_year_stock_data.xlsx has the results in excel

Multiple_year_stock_data_vba_code.vba has the code I used to generate the responses.

1. run sub typvchanges() on each sheet to generate the yearly and percent change and total volume for each stock
2. run sub greatestvalues() on each sheet to find the max and min of percent change and max of total stock volume

Note: the number after the "To" in the "for loops" needs to be switched out with the appropriate length of data entries for each sheet.
Note: The number of entries for each sheet is listed in a comment in the code.


### Background
You are well on your way to becoming a programmer and Excel master! In this homework assignment, you will use VBA scripting to analyze generated stock market data. Depending on your comfort level with VBA, you may choose to challenge yourself with a few of the challenge tasks.

### Before You Begin
1. Create a new repository for this project called `VBA-challenge`. **Do not add this homework to an existing repository**.
2. Inside the new repository that you just created, add any VBA files that you use for this assignment. These will be the main scripts to run for each analysis.

### Files
* [Test Data](Resources/alphabetical_testing.xlsx) - Use this while developing your scripts.
* [Stock Data](Resources/Multiple_year_stock_data.xlsx) - Run your scripts on this data to generate the final homework report.

### Instructions
Create a script that loops through all the stocks for one year and outputs the following information:
  * The ticker symbol.
  * Yearly change from opening price at the beginning of a given year to the closing price at the end of that year.
  * The percent change from opening price at the beginning of a given year to the closing price at the end of that year.
  * The total stock volume of the stock.

**Note:** Make sure to use conditional formatting that will highlight positive change in green and negative change in red.

### Bonus
Add functionality to your script to return the stock with the "Greatest % increase", "Greatest % decrease", and "Greatest total volume". The solution should match the following image:

Make the appropriate adjustments to your VBA script to allow it to run on every worksheet (that is, every year) just by running the VBA script once.

### Other Considerations
* Use the sheet `alphabetical_testing.xlsx` while developing your code. This data set is smaller and will allow you to test faster. Your code should run on this file in less than 3 to 5 minutes.
* Make sure that the script acts the same on every sheet. The joy of VBA is that it takes the tediousness out of repetitive tasks with one click of a button.
* Some assignments, like this one, contain a bonus. It is possible to achieve proficiency for this assignment without completing the bonus. The bonus is an opportunity to further develop your skills and be rewarded extra points for doing so.
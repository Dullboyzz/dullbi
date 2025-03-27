# Practical 1: SQL Server and Microsoft Excel Integration

## Step-by-Step Guide

### 1. Open SSMS (SQL Server Management Studio)
- Open SQL Server Management Studio (SSMS).
- You will see a SQL Server popup. Click on "Copy Server Name" and check the box for "Trust Server Certification".

### 2. Click on "Connect"
- After filling in the necessary details, click on "Connect".

### 3. Open a New Query
- On the top of the Object Explorer, click on "New Query". 
- You will see a blank page for writing your SQL queries.

### 4. Run the Code
- Use the code provided below in the blank query page.

### 5. Create Database
- Run the following code to create a new database called `StudentDB`:

    ```sql
    CREATE DATABASE StudentDB;
    GO
    ```

### 6. Select the Database
- Run the following code to select the `StudentDB` database:

    ```sql
    USE StudentDB;
    GO
    ```

### 7. Create a Table
- Run the following code to create a `Students` table:

    ```sql
    CREATE TABLE Students (
        StudentID INT IDENTITY(1,1) PRIMARY KEY,
        FirstName NVARCHAR(50),
        LastName NVARCHAR(50),
        Age INT,
        Gender NVARCHAR(10),
        Course NVARCHAR(100),
        Marks INT,
        AdmissionDate DATE
    );
    GO
    ```

### 8. Insert Data into Students Table
- Run the following code to insert sample data into the `Students` table:

    ```sql
    INSERT INTO Students (FirstName, LastName, Age, Gender, Course, Marks, AdmissionDate)
    VALUES 
        ('Amit', 'Sharma', 20, 'Male', 'Computer Science', 85, '2023-06-15'),
        ('Pooja', 'Gupta', 22, 'Female', 'Data Science', 90, '2022-07-10'),
        ('Rohan', 'Verma', 21, 'Male', 'Mathematics', 75, '2023-01-25'),
        ('Neha', 'Singh', 23, 'Female', 'Physics', 88, '2021-08-30');
    GO
    ```

### 9. Check Table (Optional)
- Run the following code to check the data in the `Students` table:

    ```sql
    SELECT * FROM Students;
    GO
    ```

### 10. Verify Databases in Object Explorer
- If you want to view your databases, go to the Object Explorer.
- In Object Explorer, click on "Databases" and find your created database (`StudentDB`).

### 11. Open Microsoft Excel
1. Open Microsoft Excel.
2. Go to the "Data" tab.
3. Select "Get Data" and then choose "From SQL Server Databases".
4. Enter the Server Name and click "Ok" to continue.
5. Wait for the list of databases to appear, then select your `StudentDB` database and load the data.

### 12. Apply Pivot Table in Excel
1. After loading the data, select the entire table.
2. Go to the "Insert" tab and select "Pivot Table".
3. Choose "New Worksheet".
4. Once the Pivot Table is created, the Pivot Table list will appear on the right side.
5. Drag and drop the required fields according to the task's question.

### 13. Apply Pivot Chart
1. After applying the Pivot Table, select the Pivot Table.
2. Go to the "Insert" tab and select "Pivot Chart".
3. Choose the desired chart type and format it accordingly.

## Conclusion
You have successfully created a database and table in SQL Server, inserted sample data, and used Microsoft Excel to load, analyze, and visualize the data using a Pivot Table and Pivot Chart.

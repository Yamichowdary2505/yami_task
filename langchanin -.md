Date - 09/02/2026



* langchanin -
* langgraph - data can be converted into graph
* langsmith - platform to trace and debug the LLM
* git \& GitHub -
* hugging face -
* pytorch -
* LLM API - llm's that are developed by langchain can be integrated into apps using these API's
* prompt engineering - giving the proper or an correct prompt to AI in order to get the desired output
* RAG - LLM can retrive the required to info or search for the desired answer
* Embeddings - Numerical representation of an Text or an Images Data
* Streamlit - Library or an platform which can be used to build Python apps using any or taking any help of frontend
* LLM Models -
* Version Control (GIT \& GITHUB)
* Language Used is Python



* Installations Required are VS code , MY SQL installer and GIT installer and GITHUB login



Date - 10/02/2026



* Databases - SQL (structured Query Language ) , helps us to store data and it helps us to retrieve the required data from the huge Stored data depending on the Query
* by using the query we will manipulate and modify the data
* SQL - relational Database
  -> Stored in form of different tables (rows , Columns )
  -> examples : MYSQL , ORACLE, SQL SERVER
  -> Queried written in form of Tables
* NO SQL - Non Relational Database
  -> we have **Key: value** pairs
  -> Examples : MongoDB (stored in form of Dictionary )
* Examples of using SQL and MYSQL is AMAZON ordering system where the data of the Person as NAME; PHONE NO ; Address is stored in database so the process can happen smoothly .
* Relational Data requires SQL
  -> SQL is not Case Sensitive
  -> Ex : CREATE / create/CReate considers all as same and takes it as Create
  -> SQL can be connected with any language like Nodejs , Python ., etc.
* Databases can only understand Queries so we use SQL and not coding languages
* Databases have schemas ( blueprints) which tell us or gives us complete info of DATA so it can help us with accessing or performing actions using Data.
* Example : we have 3 tables that has info of Users, orders, Items and all these tables are connected with each other using FK(Foreign Key) and all these combined together are considered as E-Commerce site . This is called Schema which is the blueprint of Database , where our Ecommerce Platform is our Database.



MYSQL Command Line Client .

STEPS : 1. mysql> SHOW DATABASES;(shows all the Databases)

2\. mysql> USE employeedb;(we can go inside the Database)

3\. mysql> SHOW TABLES;(shows all the tables present inside)



Today Work : Prepare One schema with min of 6 tables and connect them using FK .
-> Using Draw.io
-> share SS to tech@sourcesys.co



Date - 11/02/2026



* Data languages : **Transaction Control language**

   -> COMMIT : save changes permanently

   -> ROLLBACK : to go to saved point

   -> SAVE POINT : go back to particular point

* **DDL**: **Data definition language**

   -> CREATE : tables creation

   -> ALTER : modify table structures

   -> DROP : delete database / columns / tables

   -> TRUNCATE :table structure remains same but the record is deleted

* **DML : data manipulation language**

   -> INSERT : add

   -> UPDATE : existing data

* **DQL : data query language**

   -> Fetch : get the records

* **DCL : data control language**

   -> GRANT : give permission to the user

   -> REVOKE : refuse to give permission



* Data types :

1. Numeric Data Type :

                            INT -> -ve , +ve , 0

                            SMALL INT = small numbers

                            BIG INT = large numbers such as contact numbers



2\. Decimal Data Type :

                            DECIMAL (p,s) = 4.67

                            p = total no. of digits before point (4)

                            s = after the point (.67)

                            NUMERICAL(p,s)



3\. Floating point Data Type :

                            FLOAT : approx. values

                            DOUBLE : more precise float values (percentages)

                            REAL :



4\. String / Chars :

                            CHAR(n) -> gives fixed length string

                            VARCHAR(n) -> pass the length = its variable

                            TEXT -> stores large texts such as paragraphs



5\. Date :

                            DATE : YYYY-MM-DD

                            TIME : HH-MM-SS

                            DATETIME - YYYY-MM-DD-HH-MM-SS

                            TIMESTAMP : it updates automatically in the present format



* DDL COMMANDS :

1\. mysql-> SHOW DATABASES;

2\. mysql-> CREATE DATABASE clgdb;

3\. mysql-> USE clgdb;

4\. mysql-> CREATE TABLE details(

        -> id INT PRIMARY KEY, ------------> primary key to check whether ids are unique

        -> name VARCHAR(50),

        -> age INT

        ->);

5\. mysql-> SHOW TABLES;

6\. mysql-> DESCRIBE details;

7\. mysql-> ALTER TABLE details

        -> ADD address VARCHAR(100);

8\. mysql-> DESC details;

9\. mysql-> ALTER TABLE details

        -> MODIFY address VARCHAR(100) NOT NULL;

10\. mysql-> ALTER TABLE details

         -> DROP COLUMN address;

11\. mysql-> SELECT\*FROM details; ---> truncate

USEFUL Commands
-> INSERT INTO customers (name, phone, email) VALUES  /////    In order to insert the details into the Tables

('Ravi Kumar', '9876543210', 'ravi@gmail.com'),

('Anjali Sharma', '9123456780', 'anjali@gmail.com'),

('Suresh Reddy', '9012345678', 'suresh@gmail.com');



-> SELECT \* FROM customers;  /// to check with the details in the tales



Date - 12/02/2025



* DML -
* CURD operations
* where clause and or clause
* AND , OR Gate (one input should be true)
* XOR Gate (both i/p same : 0 ; if diff : 1)
* NOT gate (o/p opposite to i/p)
* ORDER BY ASC,DESC(to sort values in ascending or descending order in the table if no command given it will default sort in Asc)
* LIMIT ( keep the records upon given no like if LIMIT(30) , limits to 30)
* LIKE a,a,a ; a% a%
* arthematic Operators :
  -> Addition
  -> Subtraction
  -> Multiplication
  -> Divison
  -> Modulo Divison
* Bit wise operators :
  -> Bitwise AND -\&
  -> OR-|
  -> Left shift <<
  -> Right Shift >>
  -> 5 -0101
  -> 4 -0100
  -> 0 - true-1
  -> 1- False -0
  -> 5-0101 <<1
  16 8 4 2 1
  0  0 1 0 1
  0  1 0 1 0 <<1
  1  0 1 0 0 <<2
  0  0 0 1 0 >>1



Date - 13/02/26



* Aggregated functions : helps for calculations , Ex: if we have multiple salaries to handle
  -> SUM()
  -> avg()
  -> COUNT()
  -> MIN()
  -> MAX()
* To write conditions we use GROUP BY
  ->  HAVING it can be used only when we use GROUP BY and we can't use WHERE

   
CONSTRAINTS



* NOT NULL -> make sures that there are no null values in the table
  NAME VARCHAR(50) NOT NULL -> it will not accept any null or if we skip any part of the table
* UNIQUE
* email VARCHAR(50) UNIQUE
* PRIMARY KEY  unique + not null
* FOREIGN KEY
* CHECK
* age INT CHECK(age>18) DEFAULT 19
* DEFAULT
* status VARCHAR(20) DEFAULT "pending"
* ALTER TABLE table\_name

ADD CONSTRAINT unique\_email UNIQUE(email)



Date - 17/02/2026



* **main concepts of python**
  -> variables and datatypes (to declare variables)
*  **datatypes** : int-stores natural, whole, integars
  float  
  string
  Boolean - true or false
  list
  tuple
  set
  dictionaries - {key:value} pairs



* **operators:**
  Athematic - +,-,\*,/,%,//,\*\*
  comparison - ==(compare),=(assign),!=(not equal),>,<,>=,<=
  logical - and, or , not
  assignment - =,+=,-=,/=,%=,\*=,\*\*=
  bitwise - \&,|,~,^,<<,>>



* **expressions :**
  -> (a+b)\*(a-b) BODMAS
  -> (),\*\*,++,-- // first priority and then to athematic operations
  -> \*,/,//,%,+,-
  -> and, or, not



Date - 18/02/2026



* **Loops** - while loop and for loop(that repeats again and again)
  -> diff between while and for is , we use for loop when we have finite no of iterations and while loop when we have infinite no of iterations
* **Strings -** they have certain rules
  -> example if n = "henry" ; to provide string for a variable we use ""/''
  **->** strings are immutable ("my name is 'henry'")
  **->** when we have chances of duplicates , we can modify the code  such way where it either converts uppercase to lowercase or vice versa
  -> replace - where it replaces a value given : replace("e","E")
  **->** Substring - which states true or false ex: "r" in n // if r is present in n it gives true
  ->Count() - no need of any loops we can use count directly ex: count("e")
  **->** use index values to get from letters ex : n\[4] ; find("n")
  -> strip - which removes the extra space either at start or last of an word , as python calculates the space as well ex: strip(" name")
* **string formatting**
  -> name =
  age =
  print(f" my name is{name},my age  is {age}")
  print("my name is{},my age is {}".format(name,age))

  **->** reversing of a string
  -> break will terminate the loop
  -> In python do while loop will not support , do while will atleast execute once even if the condition is false
  -> while loop used mostly during entering your credentials , if any user name of password entered wrong the loop runs , once entered correct it allows inside
  -> typecasting - converting the type of variable

  

  string methods , string operations mixed with loops - todays task

  

  

  Date - 19/02/2026

  

* lists, Tuples and conditional statements
* Todays task - perform
* Conditional Statements - if , if else , if elif else  it is used when we have a particular error , if condition has true value and if the value is not true the if else statement will be coming into action .
* list -> collection of data \[1,2,3,4]
  -> it can hold or handle multiple data \[2,3,4,6,True,False,"A","mother"]
* list -\[]
  tuple -()
  list -\[4]
  tuple -(4)
* perform strings , list, tuple along with loops.

  

  Date - 20/02/2026

  

* **sets -** no duplicates values can be stored in sets , they are mutable
  and can store any datatypes
  ->setA-{1,2,3,4} ; setB-{1,2,5,6}
  set()
  set.add(5)
  -> sets has different operations like : union {1,2,3,4,5,6}
  intersection {1,2}  \&
  difference - setA-SetB {3,4}
  SetB-SetA {5,6}
  symmetric difference - setA-setB U setB-setA {3,4,5,6}

  -> we have different set methods - updating , modifying
  setA.add(10)

      remove(1)

      pop()

      clear()

      cop()       Set comprehensions ->{expression for iterable in condition}

  &nbsp;   nested set ={frozenset(\\\[1,2]),frozenset(\\\[3,4])
     
  

  

* Dictionaries = { key : value }, NOSQL -> databases
  MONGODB -> stored in form of dictionaries
  -> student ={ name:"henry", Study :"B.E", age:23 , email :"henry@gmail.com"}
  -> student \["name"], to update u need to specify the key
  -> student\["email"] = henry123@gmail.com
  ->pop("key")
  -> del student\["name"]
  -> del student  
  -> for key, value in dict1
  print(key, value)  
  

Date - 23/02/2026





* fuctions , Modules , OOPS concepts 
  -> function is defined using def key word ; ex : def func\_name()
  -> Try;excpet ; else ; finally (exceptional handling)
  -> oops concept : classes,objects,inheritance,polymorphispm ,abstraction,encapsulation 


  

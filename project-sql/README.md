ITO4132 Introduction to Databases
Assignment 2 - SQL
Generative AI tools cannot be used in this assessment task
In this assessment, you must not use generative artificial intelligence (AI) to generate
any materials or content in relation to the assessment task.
City Run (CR) is a running carnival which is held on separate dates at various capital cities in
Australia during different seasons (Summer, Autumn, Winter and Spring) of the year. The
carnival naming convention that City Run uses is CR <season name> Series <city name>
<year>
. So, for example, a carnival to be held during the Summer season in Melbourne in
2024 will be named as CR Summer Series Melbourne 2024.
Anyone can attend a CR Carnival, the carnivals are open to all members of the public. A
carnival is run on a particular date, in a particular location and only lasts for one day. CR only
runs one carnival on any particular date. During a carnival a range of events are offered
from the following list (only some may be offered):
● Marathon 42.2 Km
● Half Marathon 21.1 Km
● 10 Km Run
● 5 Km Run
● 3 Km Community Run/Walk
City Run expects to offer around 10 - 20 such events across all carnivals in a given year.
When a competitor initially registers for City Run, they are assigned a unique competitor
number. A competitor is required to provide details of an emergency contact at the time of
registration. The relationship to the competitor can be Parent (P), Guardian (G), Partner (T) or
Friend (F).
When a carnival is being offered, City Run contacts all registered competitors and provides
details of the carnival date and what events are on offer. Competitors can enter for only one
event within a carnival. Every entry is assigned a unique entry id (e.g. 3021). Using official
timing devices at the carnival, City Run records the entrants starting and finishing times.
A major focus of the City Run Carnivals is to raise funds for various charities. When a
competitor enters an event, they may nominate a charity for which they will raise funds (not all
competitors will select a charity for each event they enter). Competitors who have entered the
carnival can also form teams with other competitors, whom they know and who have entered
the carnival, to support their training and run as a group. The first competitor to register a team
for a given carnival is assigned as the Team Manager. Teams are identified by a unique team
name which the team manager must select when they first create the team. This team
manager can then add/invite other competitors from the carnival to join their team. Team
names are unique only within a given carnival, A given team name may be reused by different
Page 1 of 18
competitors in a different carnival as teams are recreated for each carnival depending on
which competitors have entered an event for the carnival. City Run wishes to record, as part of
the stored data, how many members are on each team. Teams may also nominate a charity
for which they will raise funds, although not all teams will do so. All charities for which funds
can be raised must first be approved by City Run.
Note that an individual competitor may be supporting a charity as an individual and also the
same or a different charity as a team member.
A data model has been developed for this situation. The logical model is shown below:
Page 2 of 18
From this logical model the following relational model has been created:
For this assignment, you will populate these tables with appropriate test data and complete the
tasks specified below. You must ensure that any activities you need to carry out in the
database to complete the assignment tasks conform to the requirements of the provided
data model.
The schema/insert file for creating this model (cr-schema-insert.sql) is available in the archive
ass2-student.zip - this file creates the City Run tables and populates several of the tables
(those shown in purple on the supplied model) - you should read this schema carefully and be
sure you understand the various data requirements. You must not alter the schema file in
any manner, it must be used as supplied. This schema file contains a single commit after the
inserts have completed since this is setting up an initial state of the database for you to work
with, you should not use this as your standard method of approach.
Page 3 of 18
IMPORTANT points for you to observe, when completing this assignment, are:
1. 2. 3. 4. 5. 6. The ass2-student.zip archive also contains several files for you to type your answers in,
you should ensure these files are regularly pushed to GitLab server so a clear
development history is available for the marker to verify (a minimum of fourteen
pushes are required - two per task). In each file, you must fill in the header details
with your name and student ID before beginning any work. Your SQL script files must
not include any SPOOL or ECHO commands. Although you might include such
commands when testing your work they must be removed before submission (a
grade penalty will be applied if your documents contain spool or echo commands).
You are free to make assumptions if needed. However, your assumptions must align
with the details here and in the Ed Assignment 2 forum and must be clearly
documented (see the required submission files).
REMEMBER you must keep up to date with the Ed Assignment 2 forum where further
clarifications may be posted (this forum is to be treated as your client). Please be
careful to ensure you do not post anything which includes your reasoning, logic
or any part of your work to this assignment forum as doing so violates Monash
plagiarism/collusion rules.
SQL views must not be used in arriving at any solutions for the tasks you are required
to complete as part of this assessment.
In handling dates, the default date format must not be assumed; you must make use
of the TO
DATE and TO
_
_
CHAR functions where appropriate.
ANSI joins must be used where joining of tables in SQL is required.
In completing the following tasks, you must design your test data so that you always
get output for the SQL scripts/queries specified below- this may require you to add
further data as you move through completing the required tasks. Such extra data MUST
be added as part of Task 2 (i.e. as part of your load of test data). Queries that are
correct but do not produce any output (“no rows selected” message) using your
test data will lose 50% of the marks allocated, so you should carefully check your
test data and ensure it thoroughly validates your SQL queries.
******************************************************************************************************
In answering these tasks you are ONLY permitted to use the SQL structures and syntax
which have been covered within this unit:
● Module 2A The Relational Model
● Module 3B Creating and Altering the Database Structure (DDL),
● Module 4 DML & Transactions and SQL Part I,
● Module 5 SQL Part II and III and the Oracle Common Functions document.
● Module 6 Non-Relational Databases
SQL syntax and commands outside of the covered work, as detailed above, will NOT be
accepted/marked.
******************************************************************************************************
Page 4 of 18
Assignment Tasks
TASK 1: Relational Database Queries - Relational Algebra (6 marks)
Your answers for this task (Task 1) must be written in an Ms Word document or Google
document. Once you have completed all questions, download or print the document as a pdf
file and name the file as T1-cr-ra.pdf.
For this task you are required to write the relational algebra operations for the following
queries (your answer must show an understanding of query efficiency). Please ensure you
copy and paste each of the questions below (a) - (c) into your answer document.
List of symbols for copying/pasting as you enter your answers below:
project: π, select: σ, join: ⨝, intersect: ⋂, union: ⋃, minus: -
Example:
Question:
Feb 2023 .
List the Team ID and Team name for all teams involved with the carnival held on the 1st
Answer:
OR
R = π team
id, team
_
_
name (σ carn
_
date= ''01-Feb-2023" TEAM)
R1 = σ carn_date = ''01-Feb-2023" TEAM
R = π team
id, team
_
_
name (R1)
(a) List the carnival date, carnival name name and location for all carnivals which have an
event type code of "10K"
.
[1 mark]
(b) List competitor number, first and last name and date of birth for any competitor who is
registered by City Run but has as yet not registered for an events (added an entry)
[2 marks]
(c) List competitor number, first and last name, and their emergency contact’s first name,
last name and phone number for all competitors who registered in a carnival named ''CR
Summer Series Sydney 2023'''
.
[3 marks]
Page 5 of 18
TASK 2: Data Insert (10 marks)
You may need to rerun the schema (cr-schema-insert.sql), especially when you have been
experimenting with your solutions and may have corrupted the database unintentionally. If you
suspect that there might be such problems, simply rerun the schema. The schema includes the
appropriate drop commands at the head of the file.
Load selected tables with your own additional test data: using the supplied
T2-cr-insert.sql script file, code the SQL commands which will insert, as a minimum, the
following sample data into the yellow coloured relations in the logical model -
● 20 ENTRIES,
● 5 TEAMS
Please note, these are the minimum number of entries you must insert; you are encouraged to
insert more to provide a richer data set to draw from and to validate your queries in task 4.
For this task only, data that you add in the database should follow the rules mentioned below:
1. 2. 3. You may treat all of the data that you add as a single transaction since you are setting up
the initial test state for the database.
The primary key values for this data should be hardcoded values (i.e., NOT make use of
sequences) and must consist of values below 100.
The entries and teams must be spread across at least three carnivals which have been
completed. Within a given carnival at least two different events must be used.
For this task ONLY, you can look up and include values for the loaded tables/data directly
where required. However, if you wish, you can still use SQL to get any non-key values.
You are reminded again that in carrying out this task you must not modify any data or
add any further data to the tables which were previously populated by the supplied
schema file.
[10 marks]
For all subsequent tasks (Task 3 onwards) you are NOT permitted to manually:
● manually lookup an attribute/s in the database to obtain any value,
● manually calculate values (including dates/times) external to the database, e.g. on a
calculator and then use such values in your answers. ALL necessary calculations
must be carried out as part of your SQL code, or
● assume any contents in the database - rows in a table are potentially in a constant
state of change
You must ONLY use the data as provided in the text of the questions. Where a particular
case (upper case, lower case, etc.) for a word is provided you must only use that case. You
may divide names such as Brigid Radcliffe into the first name of Brigid and a last name of
Radcliffe if required. Failure to adhere to this requirement will result in a mark of 0 for the
Page 6 of 18
relevant question.
TASK 3: Data Manipulation (10 marks)
For the following tasks, your SQL must correctly manage transactions and use
sequences to generate new primary keys for numeric primary key values (under no
circumstances may a new primary key value be hard coded as a number or value). Your
answers for these tasks must be placed in the supplied SQL Script T3-cr-dml.sql.
(a) Create sequences (one for use per table) to provide primary keys for data entry into the
following tables:
● COMPETITOR
● ENTRY
● TEAM
The sequences must begin at 100 and go up in steps of 1 (i.e., the first value is 100, the next
101, etc.).
[1 mark]
(b) Brigid Radcliffe, who has previously registered at City Run, has contacted the organisation
and indicated she would like to run as a competitor in the "CR Summer Series Melbourne
2024" carnival. She would like to enter the "21.1 Km Half Marathon" event. You may assume
that Brigid's phone number 1234567890, is unique in the current competitor data. She has
indicated, for this carnival, that she will raise funds to support the "Amnesty International"
charity.
Make these changes to the data in the database. This entire registration should be treated as
a single transaction.
[3 marks]
(c) A few weeks later Brigid Radcliffe emails the City Run organisers and reports that she has
suffered an injury in training and would like to change her entry (called downgrading) for the
"CR Summer Series Melbourne 2024" carnival from the "21.1 Km Half Marathon" to the "10
Km Run"
. You may assume that Brigid's phone number 1234567890, is unique in the current
competitor data. She also indicates that she would like to form a team called "Kenya
Speedstars" for this carnival. City Run staff check and confirm that the team name is not
currently in use for this carnival, so inform her that such a team can be created. The new team
will support the "Beyond Blue" charity.
Make these changes to the data in the database. These changes must be treated as a single
transaction.
[3 marks]
Page 7 of 18
(d) The following week Brigid Radcliffe emails the City Run organisers and reports that her
injury has got a lot worse and that she will need to withdraw from the "CR Summer Series
Melbourne 2024" carnival. Although she has asked a few friends to join her team for this
carnival she is not sure if any have actually taken up the offer; it is possible some have. She
did direct that her team,
"Kenya Speedstars"
, should be disbanded. Brigid Radcliffe indicated
that she is looking forward to competing in the next 2024 carnival. You may assume that
Brigid's phone number 1234567890, is unique in the current competitor data.
Make these changes to the data in the database. These changes must be treated as a single
transaction.
[3 marks]
TASK 4: SQL Queries (46 marks)
Your answers for these tasks must be placed in the supplied SQL Script T4-cr-queries.sql
You are reminded that you must design your test data so that you always get output for
your SQL queries and thus test them appropriately- this may require you to add further
data as you move through completing the required tasks. Such extra data MUST be added as
part of Task 2 (ie. as part of your load of test data). Queries that are correct but do not
produce any output (“no rows selected” message) using your test data will lose 50% of
the marks allocated. Where a question indicates "Your output must have the form shown
below"
- this means the same appearance and alignment of columns/data as the sample output
shows. Clearly your actual data may be different.
In any query where the sort order (descending or ascending) is not specified, you should use
the system default.
(a) List the first name and the last name of the runners who have registered using a Gmail
email address of the form 'gmail.com' in carnivals organised by City Run.
The listing must include
● the date of the carnival(s),
● the name of the carnival(s),
● the event description of the event(s) joined for the carnival(s), and
● the first name and last name of the runners as a single column called fullname.
The listing should be displayed in ascending order of the carnival date and runner's full name
within a carnival. Your output must have the form shown below.
[5 marks]
Page 8 of 18
(b) List all registered runners who registered to support a charity as an INDIVIDUAL for the
'42.2 km Marathon' event.
The listing must include
● the carnival date,
● the first name and last name of the runner as a single column called runner,
● the charity name,
● the charity contact person, and
● the full description of the supported event in which the runner is running
order the listing in ascending order of carnival date, within a carnival order by the charity name
and then by the runners' full name within a supported charity.
[5 marks]
(c) List the number of events all competitors have completed over the previous two calendar
years. For example if this report is run in 2023 it should show the events completed for 2022
(the last calendar year) and 2021 (two calendar years back). To allow this to occur dates must
not be hardcoded as actual values.
The listing must include
● the competitors number,
● the competitors first name,
● the competitors last name,
● the competitors gender,
● how many events they entered two calendar years back,
● how many events they entered for the previous calendar year, and
● how many events they entered across these two previous calendar years. If they have
entered no events for the two years, display 'Completed No Runs'
order the listing to show those who have completed no runs first, and for each of the two
groups (those who have completed some runs and those who have completed no runs) by
competitor number. Your output must have the form shown below.
[8 marks]
Page 9 of 18
(d) List the total number of entries/participants in the "5 Km Run'' for each carnival held in the
year 2023.
The listing must include
● the date of the carnival,
● the carnival name, and
● the total number of entries/participants in the carnival for this event. Name the column
as total
entries5Km
_
order the listing in descending order of total number of entries, if several carnivals have the
same number of entries they should be ordered with the group in ascending carnival date
order. Your output must have the form shown below.
[8 marks]
(e) For all carnivals which have been run by City Run (i.e. the carnival has been finished), list
those events which have had no entries.
The listing must include
● the date of the carnival,
● the carnival name,
● the event description
order the output by event description within the carnival date. Your output must have the form
shown below.
[8 marks]
Page 10 of 18
(f) List the team details for each carnival where the most popular team name/s (the team
name/s used most often across all carnivals) have been used.
The listing must include
● the team name,
● the date of the carnival,
● the team leaders competitor number as four digits and the first name and last
name of the team leader as a single column called TEAMLEADER, and
● the number of members in the team
order the output by the team name and within the team name by carnival date.
Your output must have the form:
[12 marks]
Page 11 of 18
TASK 5: Design Modifications (13 marks)
Your answers for these tasks must be placed in the supplied SQL Script T5-cr-mods.sql
These tasks should be attempted only after task 2, 3 and 4 have been successfully
completed. They are to be completed on the "live" database ie. the database with the data
loaded from your previous work.
In completing this task, you must:
● if you need to add new columns, tables or related constraints, follow the naming
conventions used in the data models and schema file which have been provided,
● provide column comments for any new columns that you add, and
● correctly manage any transactions used as part of your solution
(a) City Run organisers have noted that several competitors have enrolled in multiple events in
the same carnival which they do not wish to occur.
Change the database structure to prevent a competitor from enrolling in two events for the
same carnival.
[2 marks]
(b) City Run has decided that they would like to have the elapsed time (finish time - start time)
for a runner in a particular event stored as part of the system, rather than having to calculate it
every time it is required.
Add a new attribute which will record the runner's elapsed time in an event. The time should
be stored as the number of minutes elapsed to two decimal places e.g. 26.12
This attribute must be initialised to the correct elapsed time based on the data which is
currently stored in the system. You should note that the system may contain registrations for
future events which currently do not have either a start or finish time.
[4 marks]
(c) When an emergency contact has been required to be contacted due to a problem with a
competitor, there have been several instances of where the listed emergency contact has not
been able to be contacted. To help alleviate this issue, City Run would like to be able to have
a competitor, if they choose to do so, nominate more than one emergency contact.
Change the database structure to allow this to occur.
[7 marks]
Page 12 of 18
TASK 6: Non Relational Database Queries - MongoDB (10 marks)
Y our answers for this task (T ask 6) must be placed in the supplied sql file
the supplied MongoDB text file T6b-cr-mongo.mongodb.js
T6a-cr-json.sql and
(a) Write an SQL statement in T6a-cr-json.sql to generate a collection of JSON
documents using the following structure/format from the City Run tables used in tasks 4
and 5 (code/run this after task 5). Each document in the collection represents an event
in a particular carnival and contains the entry details for that event. The document
identifier (_
id) is made up of the date of the event in the form ddmmyyyy and the event
type code separated by an underscore e.g.
"19092021
10K" :
_
Note only partial (two) documents shown.
[4 marks]
Page 13 of 18
(b) Create a new collection named events and insert all documents generated in
Task 6 (a) above into MongoDB in this collection.
[1 mark]
(c) List all events which have been inserted in (b)
(d) [1 mark]
List all events which have more than two participants and which are of type 10K.
Display the carnival date, the location, the number of competitors and for all
competitors registered their competitor number and name.
[2 marks]
(e) The carnival on the "01-Feb-2023" was moved to
"Lake Gillawarna, Georges Hill, 2198"
The location was not entered correctly in the database. Correct the necessary
documents using a single MongoDB command. After correction use an
appropriate db.find command to confirm the change was successful.
[2 marks]
Page 14 of 18
SUBMISSION REQUIREMENTS
Please note, if you need to resubmit, you cannot depend on your staffs' availability, for this
reason, please be VERY CAREFUL with your submission. It is strongly recommended that
you submit several hours before this time to avoid such issues.
For this assignment there are seven files you are required to submit:
● T1-cr-ra.pdf
● T2-cr-insert.sql
● T3-cr-dml.sql
● T4-cr-queries.sql
● T5-cr-mods.sql
● T6a-cr-json.sql
● T6b-cr-mongo.mongodb.js
If you need to make any comments to your marker/tutor please place them at the head of each
of your solution scripts/answers in the "Comments for your marker:" section.
Do not zip these files into one zip archive, submit seven independent SQL scripts. The individual
files must also have been pushed to the FIT GitLab server with an appropriate history as you
developed your solutions.
Late submission will incur penalties at the rate of -10 marks for every 24 hours the
submission is late.
The seven files must also exist in your FITGitLab server repo and show a clear history of
development (a minimum of two pushes per file).
Please note we cannot mark any work on the GitLab Server, you need to ensure that you
submit correctly via Moodle since it is only in this process that you complete the required
student declaration without which work cannot be assessed.
It is your responsibility to ENSURE that the files you submit are the correct files - we
strongly recommend after uploading a submission, and prior to actually submitting, that
you download the submission and double-check its contents.
Your assignment MUST show a status of "Submitted for grading" before it will be
marked.
Page 15 of 18
If your submission shows a status of "Draft (not submitted)" it will not be assessed and will
incur late penalties after the due date/time.
Please carefully read the documentation under the "Assignment Submission" on the
Moodle Assessments page which covers things such as extensions and resubmission.
Marking Guide
Submitted code will be assessed against an optimal solution for these tasks. In some tasks
where SQL is involved there are often several alternative approaches possible, such
alternatives will be graded based on the code successfully meeting the briefs requirements. If
it does, the answer will be accepted and graded appropriately.
Marking Criteria Items Assessed
TASK 1 Relational Algebra Queries 6 marks
Maximum 6 marks - Satisfy brief requirements:
● Marks awarded, as listed, (a) - (c) for relational algebra
which meets the expressed requirement
● Marks awarded for correct use of RA operations and the
use of appropriate symbols
● Mark penalty applied if your answer does not show an
understanding of query efficiency ie. you must not make
use of unnecessary joins, nor carry attributes and tuples
up through the query which are not necessary
● 0 marks will be awarded if SQL select statements are
provided as solutions for task 1
TASK 2 Data Insert 10 marks
Insert of required items of
test data
Maximum 5 marks - Insert of data:
● Marks awarded for correct insert of required data
○ 20 ENTRY entries
○ 5 TEAM entries
● Marks awarded for correct management of transactions
Insert of valid test data Maximum 5 marks - Valid data inserted:
● Marks awarded for validity of data inserted
Page 16 of 18
○ meets the requirements expressed in the
assignment brief
● Marks awarded for correct management of dates when
inserting
Task 3 Data Manipulation 10 marks
Maximum 10 marks - Satisfy brief requirements:
● Marks awarded (a) - (d) for SQL code which meets the
expressed requirement
● Mark penalty applied if commit not used appropriately
● Mark penalty applied if date handling and string database
lookups not managed correctly
Task 4 SQL Queries 46 marks
Maximum 20 marks - Satisfy brief requirements:
● Marks awarded, as listed, (a) - (f) for SQL code which
meets the expressed requirement
● Mark penalty applied if output does not match the form
supplied for each question
● Mark penalty applied if date handling and string database
lookups are not managed correctly
● Mark penalty applied if column aliases are not used
when arithmetic calculation, concatenation, functions, or
other output manipulation is used in a query
● Mark penalty applied if manual lookup/calculation is used
for values from the database
● Statements which do not execute correctly in Oracle will
be awarded a maximum of 50% of the available marks
less 1 mark. For example, if a question is worth 6 marks
and runs with an error in SQL the maximum mark
awarded will be 2 marks
Task 5 Design Modifications 13 marks
Maximum 18 marks - Satisfy brief requirements:
● Marks awarded (a) - (c) for SQL code which meets the
expressed requirement (including appropriate use of
constraints). In making these modifications there must be
no loss of existing data or data integrity within the
database.
● Mark penalty applied if commit not used appropriately
● Mark penalty applied if column comments not used
where required
Task 6 Non Relational Database Queries - MongoDB 10 marks
Maximum 16 marks - Satisfy brief requirements:
● Maximum of 4 marks awarded for creation of a JSON
document which matches the supplied document format
● Marks awarded, as listed, (b) - (e) for MongoDB code
which meets the expressed requirement
Page 17 of 18
● Mark penalty applied if field names and predicates (such
as "&eq") are not enclosed in double quotes
Correct use of Git 5 marks
● Marks awarded for a minimum of fourteen pushes (two per
file) showing a clear development history of the work for
Assignment 2
● Marks awarded for correct Git author details used in
pushes
● Marks awarded for the use of meaningful commit
messages (i.e. not blank or of the form "Push1")
Late submission penalty -5 marks for each 24 hours late or part thereof
Final Assignment Mark Calculation
Total: 100 marks, recorded as a grade out of 50
Page 18 of 18
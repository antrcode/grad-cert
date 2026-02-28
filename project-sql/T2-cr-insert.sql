--*****PLEASE ENTER YOUR DETAILS BELOW*****
--T2-cr-insert.sql

-- ITO Assignment 2 Task 2

--Student ID: atra0119
--Student Name: Anna Tran

/* Comments for your marker:

Assumed entry start and finish times also inclulde seconds.


*/


-- ENSURE that your SQL code is formatted and has a semicolon (;)
-- at the end of every statement. When marked this will be run as
-- a script.


-- Insert into ENTRY

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 1,
           TO_DATE('19/09/2021 06:01:25','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('19/09/2021 06:47:11','dd/mm/yyyy hh24:mi:ss'),
           'Amnesty International',
           1,
           TO_DATE('19/09/2021','dd/mm/yyyy'),
           '10K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 2,
           TO_DATE('19/09/2021 06:22:12','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('19/09/2021 07:31:02','dd/mm/yyyy hh24:mi:ss'),
           'RSPCA',
           2,
           TO_DATE('19/09/2021','dd/mm/yyyy'),
           '10K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 3,
           TO_DATE('19/09/2021 08:15:23','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('19/09/2021 08:56:10','dd/mm/yyyy hh24:mi:ss'),
           'Beyond Blue',
           3,
           TO_DATE('19/09/2021','dd/mm/yyyy'),
           '5K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 4,
           TO_DATE('04/09/2022 07:14:35','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('04/09/2022 08:07:11','dd/mm/yyyy hh24:mi:ss'),
           'Salvation Army',
           4,
           TO_DATE('04/09/2022','dd/mm/yyyy'),
           '10K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 5,
           TO_DATE('04/09/2022 07:14:31','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('04/09/2022 08:21:07','dd/mm/yyyy hh24:mi:ss'),
           'Salvation Army',
           5,
           TO_DATE('04/09/2022','dd/mm/yyyy'),
           '10K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 6,
           TO_DATE('04/09/2022 07:11:31','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('04/09/2022 09:43:12','dd/mm/yyyy hh24:mi:ss'),
           'Salvation Army',
           6,
           TO_DATE('04/09/2022','dd/mm/yyyy'),
           '5K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 7,
           TO_DATE('01/02/2023 09:33:45','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('01/02/2023 09:56:55','dd/mm/yyyy hh24:mi:ss'),
           'Amnesty International',
           7,
           TO_DATE('01/02/2023','dd/mm/yyyy'),
           '3K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 8,
           TO_DATE('01/02/2023 08:34:21','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('01/02/2023 09:01:02','dd/mm/yyyy hh24:mi:ss'),
           'RSPCA',
           8,
           TO_DATE('01/02/2023','dd/mm/yyyy'),
           '5K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 9,
           TO_DATE('01/02/2023 06:45:45','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('01/02/2023 09:26:22','dd/mm/yyyy hh24:mi:ss'),
           'Beyond Blue',
           9,
           TO_DATE('01/02/2023','dd/mm/yyyy'),
           '21K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 10,
           TO_DATE('08/09/2023 06:56:11','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('08/09/2023 11:09:46','dd/mm/yyyy hh24:mi:ss'),
           'Beyond Blue',
           10,
           TO_DATE('08/09/2023','dd/mm/yyyy'),
           '42K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 11,
           TO_DATE('08/09/2023 06:55:46','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('08/09/2023 11:15:34','dd/mm/yyyy hh24:mi:ss'),
           'Beyond Blue',
           11,
           TO_DATE('08/09/2023','dd/mm/yyyy'),
           '42K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 12,
           TO_DATE('08/09/2023 06:56:02','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('08/09/2023 11:29:56','dd/mm/yyyy hh24:mi:ss'),
           'Beyond Blue',
           12,
           TO_DATE('08/09/2023','dd/mm/yyyy'),
           '42K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 13,
           TO_DATE('08/09/2023 10:02:23','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('08/09/2023 10:29:23','dd/mm/yyyy hh24:mi:ss'),
           'Amnesty International',
           13,
           TO_DATE('08/09/2023','dd/mm/yyyy'),
           '5K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 14,
           TO_DATE('08/09/2023 09:22:11','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('08/09/2023 9:39:32','dd/mm/yyyy hh24:mi:ss'),
           'Salvation Army',
           14,
           TO_DATE('08/09/2023','dd/mm/yyyy'),
           '3K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 15,
           TO_DATE('08/09/2023 08:00:43','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('08/09/2023 08:15:09','dd/mm/yyyy hh24:mi:ss'),
           'RSPCA',
           15,
           TO_DATE('08/09/2023','dd/mm/yyyy'),
           '3K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 16,
           TO_DATE('20/02/2024 06:33:42','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('20/02/2024 07:29:09','dd/mm/yyyy hh24:mi:ss'),
           'RSPCA',
           16,
           TO_DATE('20/02/2024','dd/mm/yyyy'),
           '10K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 17,
           TO_DATE('20/02/2024 06:33:45','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('20/02/2024 07:31:32','dd/mm/yyyy hh24:mi:ss'),
           'RSPCA',
           17,
           TO_DATE('20/02/2024','dd/mm/yyyy'),
           '10K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 18,
           TO_DATE('20/02/2024 06:33:51','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('20/02/2024 08:59:35','dd/mm/yyyy hh24:mi:ss'),
           'RSPCA',
           18,
           TO_DATE('20/02/2024','dd/mm/yyyy'),
           '21K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 19,
           TO_DATE('20/02/2024 06:33:54','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('20/02/2024 07:01:45','dd/mm/yyyy hh24:mi:ss'),
           'RSPCA',
           19,
           TO_DATE('20/02/2024','dd/mm/yyyy'),
           '5K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 20,
           TO_DATE('20/02/2024 07:34:23','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('20/02/2024 08:03:44','dd/mm/yyyy hh24:mi:ss'),
           'Amnesty International',
           20,
           TO_DATE('20/02/2024','dd/mm/yyyy'),
           '5K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 21,
           TO_DATE('19/09/2021 07:24:11','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('19/09/2021 08:10:26','dd/mm/yyyy hh24:mi:ss'),
           'Salvation Army',
           4,
           TO_DATE('19/09/2021','dd/mm/yyyy'),
           '10K' );

INSERT INTO entry (
    entry_id,
    entry_starttime,
    entry_finishtime,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( 22,
           TO_DATE('20/2/2024 06:01:01','dd/mm/yyyy hh24:mi:ss'),
           TO_DATE('20/2/2024 06:38:12','dd/mm/yyyy hh24:mi:ss'),
           'Amnesty International',
           1,
           TO_DATE('20/2/2024','dd/mm/yyyy'),
           '10K' );

COMMIT;

-- Insert into TEAM

INSERT INTO team (
    team_id,
    team_name,
    carn_date,
    team_no_members,
    char_name,
    entry_id
) VALUES ( 1,
           'Ozzy ozzy ozzy',
           TO_DATE('19/09/2021','dd/mm/yyyy'),
           2,
           'Beyond Blue',
           1 );

INSERT INTO team (
    team_id,
    team_name,
    carn_date,
    team_no_members,
    char_name,
    entry_id
) VALUES ( 2,
           'Army Blazers',
           TO_DATE('04/09/2022','dd/mm/yyyy'),
           3,
           'Salvation Army',
           4 );

INSERT INTO team (
    team_id,
    team_name,
    carn_date,
    team_no_members,
    char_name,
    entry_id
) VALUES ( 3,
           'Young and Dangerous',
           TO_DATE('01/02/2023','dd/mm/yyyy'),
           2,
           'RSPCA',
           7 );

INSERT INTO team (
    team_id,
    team_name,
    carn_date,
    team_no_members,
    char_name,
    entry_id
) VALUES ( 4,
           'Run for Fung',
           TO_DATE('08/09/2023','dd/mm/yyyy'),
           3,
           'RSPCA',
           10 );

INSERT INTO team (
    team_id,
    team_name,
    carn_date,
    team_no_members,
    char_name,
    entry_id
) VALUES ( 5,
           'Tell your dog I said hi',
           TO_DATE('20/02/2024','dd/mm/yyyy'),
           4,
           'RSPCA',
           16 );

COMMIT;

--Extra data I have added

INSERT INTO team (
    team_id,
    team_name,
    carn_date,
    team_no_members,
    char_name,
    entry_id
) VALUES ( 6,
           'Army Blazers',
           TO_DATE('08/09/2023','dd/mm/yyyy'),
           3,
           'Salvation Army',
           13 );

SELECT *
  FROM entry;

UPDATE entry
   SET
    team_id = 1
 WHERE entry_id = 1;

UPDATE entry
   SET
    team_id = 2
 WHERE entry_id = 4;

UPDATE entry
   SET
    team_id = 3
 WHERE entry_id = 7;

UPDATE entry
   SET
    team_id = 4
 WHERE entry_id = 10;

UPDATE entry
   SET
    team_id = 5
 WHERE entry_id = 16;

UPDATE entry
   SET
    team_id = 6
 WHERE entry_id = 13;

SELECT *
  FROM entry;

UPDATE entry
   SET
    team_id = 1
 WHERE comp_no = 2;

UPDATE entry
   SET
    team_id = 1
 WHERE comp_no = 3;

UPDATE entry
   SET
    team_id = 2
 WHERE comp_no = 5;

UPDATE entry
   SET
    team_id = 2
 WHERE comp_no = 6;

UPDATE entry
   SET
    team_id = 3
 WHERE comp_no = 8;

UPDATE entry
   SET
    team_id = 4
 WHERE comp_no = 11;

UPDATE entry
   SET
    team_id = 4
 WHERE comp_no = 12;

UPDATE entry
   SET
    team_id = 5
 WHERE comp_no = 17;

UPDATE entry
   SET
    team_id = 5
 WHERE comp_no = 18;

UPDATE entry
   SET
    team_id = 5
 WHERE comp_no = 19;

UPDATE entry
   SET
    team_id = 6
 WHERE comp_no = 14;

UPDATE entry
   SET
    team_id = 6
 WHERE comp_no = 15;

SELECT *
  FROM entry;

SELECT *
  FROM competitor;

COMMIT;
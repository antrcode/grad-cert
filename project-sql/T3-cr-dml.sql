--*****PLEASE ENTER YOUR DETAILS BELOW*****
--T3-cr-dml.sql

-- ITO Assignment 2 Task 3

--Student ID: atra0119
--Student Name: Anna Tran

/* Comments for your marker:

For c) I couldn't add in a new team without the team_no_members (primary key). I assumed it is just Bridig so
the team_no_member value I used was 1. 


*/

-- ENSURE that your SQL code is formatted and has a semicolon (;)
-- at the end of every statement. When marked this will be run as
-- a script.

/*
(a)
*/

DROP SEQUENCE competitor_seq;

CREATE SEQUENCE competitor_seq START WITH 100 INCREMENT BY 1;

SELECT *
  FROM cat;

DROP SEQUENCE entry_seq;

CREATE SEQUENCE entry_seq START WITH 100 INCREMENT BY 1;

SELECT *
  FROM cat;

DROP SEQUENCE team_seq;

CREATE SEQUENCE team_seq START WITH 100 INCREMENT BY 1;

SELECT *
  FROM cat;

/*
(b) 
*/

INSERT INTO entry (
    entry_id,
    char_name,
    comp_no,
    carn_date,
    eventtype_code
) VALUES ( entry_seq.NEXTVAL,
           'Amnesty International',
           (
               SELECT comp_no
                 FROM competitor
                WHERE comp_phone = 1234567890
           ),
           (
               SELECT carn_date
                 FROM carnival
                WHERE upper(carn_name) = upper('CR Summer Series Melbourne 2024')
           ),
           (
               SELECT eventtype_code
                 FROM eventtype
                WHERE upper(eventtype_desc) = upper('21.1 Km Half Marathon')
           ) );

SELECT *
  FROM entry;

COMMIT;

/*
(c)
*/

INSERT INTO team (
    team_id,
    team_name,
    carn_date,
    team_no_members,
    char_name,
    entry_id
) VALUES ( team_seq.NEXTVAL,
           'Kenya Speedstars',
           (
               SELECT carn_date
                 FROM carnival
                WHERE upper(carn_name) = upper('CR Summer Series Melbourne 2024')
           ),
           1,
           'Beyond Blue',
           (
               SELECT entry_id
                 FROM entry e
                 JOIN competitor c
               ON e.comp_no = c.comp_no
                WHERE comp_phone = 1234567890
                  AND carn_date = (
                   SELECT carn_date
                     FROM carnival
                    WHERE upper(carn_name) = upper('CR Summer Series Melbourne 2024')
               )
           ) );

SELECT *
  FROM team;

UPDATE entry
   SET eventtype_code = (
    SELECT eventtype_code
      FROM eventtype
     WHERE upper(eventtype_desc) = upper('10 Km Run')
),
       team_id = (
           SELECT team_id
             FROM team
            WHERE upper(team_name) = upper('Kenya Speedstars')
       )
 WHERE entry_id = (
    SELECT entry_id
      FROM entry e
      JOIN competitor c
    ON e.comp_no = c.comp_no
     WHERE comp_phone = 1234567890
       AND carn_date = (
        SELECT carn_date
          FROM carnival
         WHERE upper(carn_name) = upper('CR Summer Series Melbourne 2024')
    )
);

SELECT *
  FROM entry;

COMMIT;

/*
(d) 
*/

ALTER TABLE team DROP CONSTRAINT entry_team;

DELETE FROM entry
 WHERE comp_no = (
        SELECT comp_no
          FROM competitor
         WHERE comp_phone = '1234567890'
    )
   AND carn_date = (
    SELECT carn_date
      FROM carnival
     WHERE upper(carn_name) = upper('CR Summer Series Melbourne 2024')
);

SELECT *
  FROM entry;

DELETE FROM team
 WHERE upper(team_name) = upper('Kenya Speedstars')
   AND carn_date = (
    SELECT carn_date
      FROM carnival
     WHERE upper(carn_name) = upper('CR Summer Series Melbourne 2024')
);

ALTER TABLE team
    ADD CONSTRAINT entry_team FOREIGN KEY ( team_id )
        REFERENCES team ( team_id );

SELECT *
  FROM team;

COMMIT;
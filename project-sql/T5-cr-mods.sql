--*****PLEASE ENTER YOUR DETAILS BELOW*****
--T5-cr-mods.sql

-- ITO Assignment 2 Task 5

--Student ID: atra0119
--Student Name: Anna Tran

/* Comments for your marker:




*/

-- ENSURE that your SQL code is formatted and has a semicolon (;)
-- at the end of every statement. When marked this will be run as
-- a script.

/*
(a)
*/

ALTER TABLE entry ADD CONSTRAINT comp_carn_uq UNIQUE ( comp_no,
                                                       carn_date );

COMMIT;

   
/*
(b)
*/

ALTER TABLE entry ADD elapsedtime NUMBER(5);

SELECT *
  FROM entry;

UPDATE entry
   SET
    elapsedtime = ROUND(
        ((entry_finishtime - entry_starttime) * 1440),2
    )
 WHERE entry_finishtime IS NOT NULL
   AND entry_starttime IS NOT NULL;

SELECT * FROM entry;

COMMIT;


/*
(c)
*/

ALTER TABLE competitor DROP CONSTRAINT emercontact_competitor;

DROP TABLE emercontact;

CREATE TABLE emercontact (
    ec_id    NUMBER(5),
    comp_no  NUMBER(5),
    ec_fname VARCHAR2(30),
    ec_lname VARCHAR2(30),
    ec_phone CHAR(10),
    CONSTRAINT emercontact_pk PRIMARY KEY ( ec_id ),
    CONSTRAINT emercontact_competitor_fk FOREIGN KEY ( comp_no )
        REFERENCES competitor ( comp_no )
);

COMMENT ON COLUMN emercontact.ec_id IS
    'emergency contact id';

COMMENT ON COLUMN emercontact.ec_fname IS
    'emergency contact first name';

COMMENT ON COLUMN emercontact.ec_lname IS
    'emergency contact last name';

COMMENT ON COLUMN emercontact.ec_phone IS
    'emergency contact phone number';

COMMIT;
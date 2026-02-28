--*****PLEASE ENTER YOUR DETAILS BELOW*****
--T6a-cr-json.sql

-- ITO Assignment 2 Task 6a

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

SELECT
    JSON_OBJECT(
        '_id' VALUE to_char(
            carn_date,
            'ddmmyyyy'
        )
                    || '_'
                    || eventtype_code,
                'carnival_date' VALUE to_char(
            carn_date,
            'dd-Mon-yyyy'
        ),
                'carnival_location' VALUE carn_location,
                'event' VALUE
            JSON_OBJECT(
                'type' VALUE eventtype_code,
                        'description' VALUE eventtype_desc
            ),
                'no_competitors' VALUE COUNT(comp_no),
                'competitors' VALUE JSON_ARRAYAGG(
            JSON_OBJECT(
                'comp_no' VALUE comp_no,
                        'name' VALUE comp_fname
                                     || ' '
                                     || comp_lname,
                        'gender' VALUE
                    CASE comp_gender
                        WHEN 'F' THEN
                            'Female'
                        WHEN 'M' THEN
                            'Male'
                    END,
                        'phone' VALUE comp_phone
            )
        )
    FORMAT JSON)
    || ','
  FROM entry
NATURAL JOIN carnival
NATURAL JOIN eventtype
NATURAL JOIN competitor
 GROUP BY carn_date,
          eventtype_code,
          carn_location,
          eventtype_code,
          eventtype_desc
 ORDER BY carn_date,
          eventtype_code;
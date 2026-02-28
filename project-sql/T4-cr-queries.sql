--*****PLEASE ENTER YOUR DETAILS BELOW*****
--T4-cr-queries.sql

-- ITO Assignment 2 Task 4

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

SELECT to_char(
    e.carn_date,
    'Dy dd Month yyyy'
) AS carnival_date,
       carn_name AS carnname,
       eventtype_desc AS eventtypedesc,
       comp_fname
       || ' '
       || comp_lname AS fullname
  FROM entry e
  JOIN carnival c
ON e.carn_date = c.carn_date
  JOIN eventtype ev
ON e.eventtype_code = ev.eventtype_code
  JOIN competitor co
ON co.comp_no = e.comp_no
 WHERE lower(comp_email) LIKE '%gmail.com'
 ORDER BY e.carn_date;


/*
(b)
*/

SELECT to_char(
    e.carn_date,
    'dd-Mon-yyyy'
) AS carnival_date,
       comp_fname
       || ' '
       || comp_lname AS runner,
       e.char_name AS charity_name,
       char_contact AS charity_contact_person,
       eventtype_desc AS event_description
  FROM entry e
  JOIN competitor c
ON e.comp_no = c.comp_no
  JOIN eventtype ev
ON e.eventtype_code = ev.eventtype_code
  JOIN charity ch
ON e.char_name = ch.char_name
 WHERE upper(eventtype_desc) = upper('42.2 km Marathon')
 ORDER BY e.carn_date ASC,
          e.char_name,
          runner;

/*
(c)
*/

SELECT c.comp_no AS compno,
       comp_fname AS compfname,
       comp_lname AS complname,
       comp_gender AS compgender,
       (
           SELECT COUNT(entry_id)
             FROM entry e
            WHERE e.comp_no = c.comp_no
              AND EXTRACT(YEAR FROM e.carn_date) = EXTRACT(YEAR FROM sysdate) - 2
       ) AS twoyrsback,
       (
           SELECT COUNT(entry_id)
             FROM entry e
            WHERE e.comp_no = c.comp_no
              AND EXTRACT(YEAR FROM e.carn_date) = EXTRACT(YEAR FROM sysdate) - 1
       ) AS lastcalyear,
       CASE
           WHEN ( (
                   SELECT COUNT(entry_id)
                     FROM entry e
                    WHERE e.comp_no = c.comp_no
                      AND EXTRACT(YEAR FROM e.carn_date) = EXTRACT(YEAR FROM sysdate) - 2
               ) = 0
              AND (
               SELECT COUNT(entry_id)
                 FROM entry e
                WHERE e.comp_no = c.comp_no
                  AND EXTRACT(YEAR FROM e.carn_date) BETWEEN EXTRACT(YEAR FROM sysdate
                  ) - 2 AND EXTRACT(YEAR FROM sysdate) - 1
           ) = 0 ) THEN
               'Completed No Runs'
           ELSE
               to_char((
                   SELECT COUNT(entry_id)
                     FROM entry e
                    WHERE e.comp_no = c.comp_no
                      AND EXTRACT(YEAR FROM e.carn_date) BETWEEN EXTRACT(YEAR FROM sysdate
                      ) - 2 AND EXTRACT(YEAR FROM sysdate)
               ))
       END AS last2calendaryears
  FROM competitor c
 ORDER BY
    CASE
        WHEN (
            SELECT COUNT(entry_id)
              FROM entry e
             WHERE e.comp_no = c.comp_no
               AND EXTRACT(YEAR FROM e.carn_date) BETWEEN EXTRACT(YEAR FROM sysdate) - 2
               AND EXTRACT(YEAR FROM sysdate) - 1
        ) = 0 THEN
            0
        ELSE
            1
    END,
    comp_no;


/*
(d) 
*/

SELECT to_char(
    carn_date,
    'dd-Mon-yyyy'
) AS carnival_date,
       carn_name AS carnname,
       COUNT(entry_id) AS total_entries5km
  FROM entry
NATURAL JOIN carnival
NATURAL JOIN eventtype
 WHERE EXTRACT(YEAR FROM carn_date) = 2023
   AND upper(eventtype_desc) = upper('5 Km Run')
 GROUP BY carn_date,
          carn_name
 ORDER BY total_entries5km DESC,
          carn_date ASC;

/* 
(e) 
*/

SELECT to_char(
    c.carn_date,
    'dd-Mon-yyyy'
) AS carnival_date,
       carn_name AS carnname,
       eventtype_desc AS eventtypedesc
  FROM carnival c
  JOIN event e
ON c.carn_date = e.carn_date
  JOIN eventtype ev
ON e.eventtype_code = ev.eventtype_code
  LEFT JOIN entry en
ON e.carn_date = en.carn_date
   AND e.eventtype_code = en.eventtype_code
 WHERE c.carn_date < sysdate
   AND en.entry_id IS NULL
 ORDER BY c.carn_date,
          ev.eventtype_desc;

/*
(f)
*/

SELECT t.team_name AS teamname,
       to_char(t.carn_date,'dd-Mon-yyyy') AS carnivaldate,
       lpad(
           c.comp_no,
           4,
           '0'
       )
       || ' '
       || c.comp_fname
       || ' '
       || c.comp_lname AS teamleader,
       t.team_no_members AS teamnomembers
  FROM team t
  JOIN entry e
ON t.entry_id = e.entry_id
  JOIN competitor c
ON e.comp_no = c.comp_no
 WHERE t.team_name IN (
    SELECT team_name
      FROM team
     GROUP BY team_name
    HAVING COUNT(*) = (
        SELECT MAX(team_count)
          FROM (
            SELECT COUNT(*) AS team_count
              FROM team
             GROUP BY team_name
        )
    )
)
 ORDER BY t.team_name,
          t.carn_date;
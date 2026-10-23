IF DB_ID('MissionUltronDB') IS NULL
BEGIN
    CREATE DATABASE MissionUltronDB;
END;

SELECT name
FROM sys.databases
WHERE name = 'MissionUltronDB';
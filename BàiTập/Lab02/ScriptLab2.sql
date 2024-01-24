alter session set "_ORACLE_SCRIPT"=true;

CREATE USER salapati IDENTIFIED BY sammyy1;

SELECT default_tablespace, temporary_tablespace
FROM dba_users
WHERE username='SALAPATI';

GRANT CREATE SESSION TO salapati;

CONNECT salapati/sammyy1

CREATE TABLE xyz (name VARCHAR2(30));

ALTER USER salapati
QUOTA 100M ON users;

GRANT CREATE TABLE TO salapati;

SELECT tablespace_name, username, bytes
FROM DBA_TS_QUOTAS;

CREATE USER edgar IDENTIFIED BY ed2002;

CREATE USER salapati_new IDENTIFIED BY sammyy1
TEMPORARY TABLESPACE XYZ
DEFAULT TABLESPACE USERS
QUOTA 500M ON USERS;


==========================================
ALTER SYSTEM SET RESOURCE_LIMIT = TRUE;

CREATE PROFILE app_user LIMIT
FAILED_LOGIN_ATTEMPTS 3
SESSIONS_PER_USER UNLIMITED
CPU_PER_SESSION UNLIMITED
CPU_PER_CALL 3000
CONNECT_TIME 45
IDLE_TIME 60
LOGICAL_READS_PER_SESSION DEFAULT
LOGICAL_READS_PER_CALL 1000;

================================================
CREATE PROFILE password LIMIT
	PASSWORD_LIFE_TIME				60
	PASSWORD_GRACE_TIME				10
	PASSWORD_REUSE_TIME				1
	PASSWORD_REUSE_MAX				5
	FAILED_LOGIN_ATTEMPTS			3;
    
    
create user john identified by p123

alter user john profile password;

GRANT CREATE SESSION TO john;

===========================
thay ??i m?t kh?u c?a john 5 l?n
l?n th? 1
alter user john identified by p2002;
l?n th? 2
alter user john identified by p1704;
l?n th? 3
alter user john identified by p2003;

thay ??i m?t kh?u ban ??u (m?t kh?u l?n th? 1)
alter user john identified by p2002;

l?n th? 4
alter user john identified by pa1200;
l?n th? 5
alter user john identified by pa2002;

thay ??i m?t kh?u ban ??u (m?t kh?u ban ??u)
alter user john identified by p123;


ki?m tra l?ch s? thay ??i c?a user
select * from user_history$;



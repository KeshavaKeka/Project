DROP USER IF EXISTS 'project'@'db';
CREATE USER 'project'@'db' identified by'project123';

GRANT SELECT,INSERT ON trafficfine.login TO 'project'@'db';
GRANT INSERT, SELECT, DELETE ON trafficfine.violation TO 'project'@'db';
GRANT INSERT,SELECT ON trafficfine.payment TO 'project'@'db';
GRANT SELECT ON trafficfine.citizen TO 'project'@'db';
GRANT SELECT ON trafficfine.RTO_Vehicle TO 'project'@'db';

DROP USER IF EXISTS 'admin'@'db';
CREATE USER 'admin'@'db' identified by 'likith';

GRANT ALL PRIVILEGES ON *.* TO 'admin'@'db' WITH GRANT OPTION;
3-1.
INSERT INTO member (name, username, password) 
VALUES ('test', 'test', 'test');

INSERT INTO member (name, username, password, follower_count) 
VALUES 
('Kelly', 'Kelly', '0712', 20),
('Barry', 'Barry', '11235813', 102),
('Rudy', 'Rudy', 'r1231', 33),
('Nathan', 'Nathan', 'nnn707', 5),
('Alisa', 'Alisa', 'a75a8', 85);

INSERT INTO member (name, username, password, follower_count) 
VALUES ('Curtis', 'Curtis', 'uhbijnokm', 60);

INSERT INTO member (name, username, password, follower_count) 
VALUES ('Simon', 'Simon', 's1m0n', 33);

3-2.
SELECT * FROM member;

3-3.
SELECT * FROM member ORDER BY time DESC;
![3-2~3](https://user-images.githubusercontent.com/63653055/151363049-90436bfb-8606-4ecd-b80a-8b9c1b86eec0.png)

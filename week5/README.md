3-1.使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和
password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。

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

3-2. 使用 SELECT 指令取得所有在 member 資料表中的會員資料。 
3-3.使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由
近到遠排序。

![3-2~3](https://user-images.githubusercontent.com/63653055/151363180-42ef7c11-6fe9-4ad6-a852-c043379ab039.png)

3-4.使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，
由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )

![3-4](https://user-images.githubusercontent.com/63653055/151363682-fb590791-4516-4355-b79f-cb8c11f0bea5.png)

3-5.使用 SELECT 指令取得欄位 username 是 test 的會員資料。

![3-5](https://user-images.githubusercontent.com/63653055/151364386-a5190d37-57a9-4558-b7a0-2e9d541b9cf5.png)

3-6.使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

![3-6](https://user-images.githubusercontent.com/63653055/151364404-e8b64643-4bed-4dd9-9b63-8c2feb75f699.jpg)

3-7.使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位
改成 test2。

![3-7](https://user-images.githubusercontent.com/63653055/151364428-cdf3a779-5541-4e56-bcec-7733cd6e588c.jpg)

4-1.取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。

![4-1](https://user-images.githubusercontent.com/63653055/151364523-d56abf86-fa64-4be6-a7ce-95c76093a8e8.jpg)

4-2.取得 member 資料表中，所有會員 follower_count 欄位的總和。

![4-2](https://user-images.githubusercontent.com/63653055/151364556-7c4d749d-1b45-456e-893f-1c3063968a73.jpg)

4-3.取得 member 資料表中，所有會員 follower_count 欄位的平均數。

![4-3](https://user-images.githubusercontent.com/63653055/151364568-a81b0076-ec69-4d56-8463-991ab6742979.jpg)


5-1.在資料庫中，建立新資料表，取名字為message。

CREATE TABLE message
(
id BIGINT AUTO_INCREMENT PRIMARY KEY,
member_id BIGINT NOT NULL,
content VARCHAR(255) NOT NULL,
time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(member_id) REFERENCES member(id)
);

![5-1](https://user-images.githubusercontent.com/63653055/151365127-ca80ae2f-0c57-4ce8-82d8-b5befea2f18e.jpg)


5-2.使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。

![5-2](https://user-images.githubusercontent.com/63653055/151364825-88ca672f-2638-4bd0-91c5-7b6fdd94d122.jpg)

5-3.使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有
留言，資料中須包含留言者會員的姓名。

![5-3](https://user-images.githubusercontent.com/63653055/151364842-68f4f5fd-890c-405e-9b8a-da8acc1262cd.jpg)



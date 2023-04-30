CREATE DATABASE IF NOT EXISTS cop CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE cop;

CREATE TABLE IF NOT EXISTS tags (
    Tagid INT NOT NULL AUTO_INCREMENT,
    TagName VARCHAR(50) NOT NULL,
    TagDes VARCHAR(500) NOT NULL,
    QCount INT NOT NULL,
    PRIMARY KEY (Tagid)
);


CREATE TABLE IF NOT EXISTS users (
    Userid INT NOT NULL AUTO_INCREMENT,
    UserName VARCHAR(50) NOT NULL,
    UserEmail VARCHAR(50) NOT NULL,
    UserPass VARCHAR(200) NOT NULL,
    UserImg VARCHAR(2000) DEFAULT 'https://www.gravatar.com/avatar/8553c44cec56644d4c96707f562a1ec1?s=256&d=identicon&r=PG&f=1' ,
    UserAbout VARCHAR(5000),
    UserLocation VARCHAR(50),
    Rating INT DEFAULT 0,
    PRIMARY KEY (Userid)
);


CREATE TABLE IF NOT EXISTS questions (
    QuesId INT NOT NULL AUTO_INCREMENT,
    QuesTitle VARCHAR(200) NOT NULL,
    QuesDesc VARCHAR(5000) NOT NULL,
    QCreationTime DATETIME ,
    QuesScore INT NOT NULL,
    QuesTags JSON,
    UserId INT,
    FOREIGN KEY (UserId) REFERENCES users(UserId),
    PRIMARY KEY (QuesId)
);



CREATE TABLE IF NOT EXISTS answers (
    AnsId INT NOT NULL AUTO_INCREMENT,
    AnsDesc VARCHAR(5000) NOT NULL,
    AnsScore INT NOT NULL,
    UserId INT NOT NULL,
    ACreationTime DATETIME ,
    QuesId INT NOT NULL,

    FOREIGN KEY (UserId) REFERENCES users(UserId),
    FOREIGN KEY (QuesId) REFERENCES questions(QuesId),
    PRIMARY KEY (AnsId)
);



CREATE TABLE IF NOT EXISTS votes (
    VoteId INT NOT NULL AUTO_INCREMENT,
    UserId INT NOT NULL,
    AnsId INT NOT NULL,
    State INT NOT NULL,
    PRIMARY KEY (VoteId)
);



CREATE TABLE IF NOT EXISTS questionvotes (
    QVoteId INT NOT NULL AUTO_INCREMENT,
    QUserId INT NOT NULL,
    QuesId INT NOT NULL,
    QState INT NOT NULL,
    PRIMARY KEY (QVoteId)
);



INSERT INTO tags (TagName,TagDes,QCount) VALUES ('php','PHP is a server-side scripting language designed for web development but also used as a general-purpose programming language.',798);
INSERT INTO tags (Tagname,TagDes,QCount) VALUES ('mysql','MySQL is an open-source relational database management system.',532);

INSERT INTO tags (Tagname,TagDes,QCount) VALUES ('java','Java is a general-purpose programming language that is class-based, object-oriented, and designed to have as few implementation dependencies as possible.',234);
INSERT INTO tags (Tagname,TagDes,QCount) VALUES ('addition','Addition is one of the four basic operations of arithmetic; the others are subtraction, multiplication and division.',21);
INSERT INTO tags (Tagname,TagDes,QCount) VALUES ('subtraction','Subtraction is an arithmetic operation that represents the operation of removing objects from a collection.',32);
INSERT INTO tags (Tagname,TagDes,QCount) VALUES ('multiplication','Multiplication is one of the four elementary mathematical operations of arithmetic, with the others being addition, subtraction and division.',423);
INSERT INTO tags (Tagname,TagDes,QCount) VALUES ('division','Division is one of the four basic operations of arithmetic, the ways that numbers are combined to make new numbers.',90);
INSERT INTO tags (Tagname,TagDes,QCount) VALUES ('python','Python is an interpreted, high-level and general-purpose programming language.',17);
INSERT INTO tags (Tagname,TagDes,QCount) VALUES ('c++','C++ is a general-purpose programming language created by Bjarne Stroustrup as an extension of the C programming language, or "C with Classes".',18);
INSERT INTO tags (Tagname,TagDes,QCount) VALUES ('c','C is a general-purpose, procedural computer programming language supporting structured programming, lexical variable scope, and recursion, with a static type system.',991);
INSERT INTO tags (Tagname,TagDes,QCount) VALUES ('javascript','JavaScript, often abbreviated as JS, is a programming language that conforms to the ECMAScript specification.',69);
INSERT INTO tags (Tagname,TagDes,QCount) VALUES ('html','Hypertext Markup Language is the standard markup language for documents designed to be displayed in a web browser.',111);
INSERT INTO tags (Tagname,TagDes,QCount) VALUES ('css','Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.',220);

INSERT INTO users (UserId,UserName,UserEmail,UserPass,Rating) VALUES (1,'admin','admin@gmail.com','admin',100);
INSERT INTO users (UserId,UserName,UserEmail,UserPass,Rating) VALUES (2,'user1','user1@gmail.com','user1',10);
INSERT INTO users (UserId,UserName,UserEmail,UserPass,Rating) VALUES (3,'rounik','rounik@gmail.com','user2',10);

INSERT INTO questions (QuesTitle,QuesDesc,QuesScore,QuesTags,UserId) VALUES ('2+2=?','I am stupid','10','["php","addition"]',1);

INSERT INTO questions (QuesTitle,QuesDesc,CreationTime,QuesScore,QuesTags,UserId) VALUES ('2+4=?','six','2008-08-01 20:15:55','40','["addition"]',1);

INSERT INTO questions (QuesTitle,QuesDesc,QuesScore,QuesTags,QCreationTime,UserId) VALUES ('2+7=?','twenty-seven','20','["php","addition"]',"2008-08-10 13:57:55",1);



INSERT INTO questions (QuesTitle,QuesDesc,QuesScore,QuesTags,UserId) VALUES ('How to connect to MySQL database in PHP?','I am trying to connect to MySQL database in PHP. I am using XAMPP. I have created a database named "cop" and a table named "users". I have created a PHP file named "connect.php" and I have written the following code in it. But it is not working. I am getting an error "Error". Please help me to solve this problem.','10','["php","mysql"]',1);

INSERT INTO questions (QuesTitle,QuesDesc,QuesScore,QuesTags,UserId) VALUES ('How is PHP different from Java?','I am a Java developer. I have heard that PHP is also a programming language. I want to know how is PHP different from Java?','120','["php","java"]',2);


INSERT INTO answers (AnsDesc,AnsScore,UserId,QuesId) VALUES ('4','10',3,1);
INSERT INTO answers (AnsDesc,AnsScore,UserId,QuesId) VALUES ('four','40',2,1);
INSERT INTO answers (AnsDesc,AnsScore,UserId,QuesId) VALUES ('6','20',3,2);
INSERT INTO answers (AnsDesc,AnsScore,UserId,QuesId) VALUES ('nine','250',1,3);


INSERT INTO answers (AnsDesc,AnsScore,UserId,QuesId) VALUES ('You can connect to MySQL database in PHP using the following code. You have to change the username and password according to your MySQL database. You can also change the database name if you have created a different database. You can also change the table name if you have created a different table. You can also change the column names if you have created different columns.','10',2,1);

INSERT INTO answers (AnsDesc,AnsScore,UserId,QuesId) VALUES ('PHP is a server-side scripting language designed for web development but also used as a general-purpose programming language. Java is a general-purpose programming language that is class-based, object-oriented, and designed to have as few implementation dependencies as possible.As of 2019, Java was one of the most popular programming languages in use according to GitHub, particularly for client-server web applications, with a reported 9 million developers.','120',3,2);

INSERT INTO answers (AnsDesc,AnsScore,UserId,QuesId) VALUES ('It is intended to let application developers "write once, run anywhere" (WORA), meaning that compiled Java code can run on all platforms that support Java without the need for recompilation. Java applications are typically compiled to bytecode that can run on any Java virtual machine (JVM) regardless of the underlying computer architecture. The syntax of Java is similar to C and C++, but has fewer low-level facilities than either of them.','23',1,2);


INSERT INTO votes (UserId,AnsId,State) VALUES (1,1,1);



INSERT INTO users (UserId,UserName,UserEmail,UserPass,Rating,UserImg) VALUES (1,'admin1212','admi313n@gmail.com','ad121min',100,'https://cdncontent.xxxwaffle.com/gthumb/1/916/1916947_090b5f1_600x_.jpg');
INSERT INTO users (UserId,UserName,UserEmail,UserPass,Rating,UserImg) VALUES (2,'us131er1','use211r1@gmail.com','use313r1',10,'https://cdn.pornpictureshq.com/galleries/gthumb/6/310/6310445_95e8276_600x_.jpg');
INSERT INTO users (UserId,UserName,UserEmail,UserPass,Rating,UserImg) VALUES (3,'roun212ik','rouni31k@gmail.com','us212er2',10,'https://cdncontent.xxxwaffle.com/gthumb/2/902/2902850_fd69e7e_600x_.jpg');


LOAD DATA INFILE 'Database/users_baadal.csv' INTO TABLE users FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;


LOAD DATA INFILE '/var/lib/mysql-files/users_baadal.csv' INTO TABLE users FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;


LOAD DATA INFILE '/var/lib/mysql-files/users_baadal.csv'
IGNORE INTO TABLE users
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
(UserId,UserName,UserEmail,UserPass,UserImg,UserAbout,UserLocation,Rating);


LOAD DATA INFILE '/var/lib/mysql-files/questions_baadal.csv'
IGNORE INTO TABLE questions
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
(QuesId,QuesTitle,QuesDesc,QCreationTime,QuesScore,@QuesTags,UserId)
SET QuesTags = JSON_UNQUOTE(@QuesTags);


LOAD DATA INFILE '/var/lib/mysql-files/questions_baadal.csv'
IGNORE INTO TABLE questions
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
(QuesId,QuesTitle,QuesDesc,QCreationTime,QuesScore,QuesTags,UserId);


mv /home/baadalvm/queriKorner/Database/questions_baadal.csv /var/lib/mysql-files/

INSERT INTO questions (QuesId,QuesTitle,QuesDesc,QCreationTime,QuesScore,QuesTags,UserId) VALUES (889,"SQLStatement.execute() - multiple queries in one statement","<p>I've written a database generation script in <a href=""http://en.wikipedia.org/wiki/SQL"">SQL</a> and want to execute it in my <a href=""http://en.wikipedia.org/wiki/Adobe_Integrated_Runtime"">Adobe AIR</a> application:</p>","2023-04-29 21:13:34",26,'["php"]',1666)

INSERT INTO questions (QuesId,QuesTitle,QuesDesc,QCreationTime,QuesScore,QuesTags,UserId) VALUES (860,"SQLStatement.execute() - multiple queries in one statement","<p>I've written a database generation script in <a href=""http://en.wikipedia.org/wiki/SQL"">SQL</a> and want to execute it in my <a href=""http://en.wikipedia.org/wiki/Adobe_Integrated_Runtime"">Adobe AIR</a> application:</p>",'2008-08-01 13:57:07',26,'["php"]',1666);




INSERT INTO answers (AnsId,AnsDesc,AnsScore,UserId,ACreationTime,QuesId) VALUES (1,"Answer",67,4549416,'2008-08-01 13:57:07',193260)
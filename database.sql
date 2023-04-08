CREATE DATABASE IF NOT EXISTS cop;
USE cop;

CREATE TABLE IF NOT EXISTS tags (
    Tagid INT NOT NULL AUTO_INCREMENT,
    TagName VARCHAR(30) NOT NULL,
    TagDes VARCHAR(200) NOT NULL,
    QCount INT NOT NULL,
    PRIMARY KEY (Tagid)
);

INSERT INTO tags (TagName,TagDes,QCount) VALUES ('php','PHP is a server-side scripting language designed for web development but also used as a general-purpose programming language.',10);
INSERT INTO tags (Tagname,TagDes,QCount) VALUES ('mysql','MySQL is an open-source relational database management system.',10);

CREATE TABLE IF NOT EXISTS users (
    Userid INT NOT NULL AUTO_INCREMENT,
    UserName VARCHAR(50) NOT NULL,
    UserEmail VARCHAR(50) NOT NULL,
    UserPass VARCHAR(30) NOT NULL,
    UserImg LONGBLOB,
    Rating INT DEFAULT 0,
    PRIMARY KEY (Userid)
);

INSERT INTO users (UserId,UserName,UserEmail,UserPass,Rating) VALUES (1,'admin','admin@gmail.com','admin',100);
INSERT INTO users (UserId,UserName,UserEmail,UserPass,Rating) VALUES (2,'user1','user1@gmail.com','user1',10);
INSERT INTO users (UserId,UserName,UserEmail,UserPass,Rating) VALUES (3,'rounik','rounik@gmail.com','user2',10);


CREATE TABLE IF NOT EXISTS questions (
    QuesId INT NOT NULL AUTO_INCREMENT,
    QuesTitle VARCHAR(50) NOT NULL,
    QuesDesc VARCHAR(5000) NOT NULL,
    QuesScore INT NOT NULL,
    QuesTags JSON,
    UserId INT,
    FOREIGN KEY (UserId) REFERENCES users(UserId),
    PRIMARY KEY (QuesId)
);

INSERT INTO questions (QuesTitle,QuesDesc,QuesScore,QuesTags,UserId) VALUES ('2+2=?','I am stupid','10','["php","addition"]',1);

INSERT INTO questions (QuesTitle,QuesDesc,QuesScore,QuesTags,UserId) VALUES ('2+4=?','six','40','["addition"]',1);

INSERT INTO questions (QuesTitle,QuesDesc,QuesScore,QuesTags,UserId) VALUES ('2+7=?','twenty-seven','20','["php","addition"]',2);



-- INSERT INTO questions (QuesTitle,QuesDesc,QuesScore,QuesTags,UserId) VALUES ('How to connect to MySQL database in PHP?','I am trying to connect to MySQL database in PHP. I am using XAMPP. I have created a database named "cop" and a table named "users". I have created a PHP file named "connect.php" and I have written the following code in it. But it is not working. I am getting an error "Error". Please help me to solve this problem.','10','["php","mysql"]',1);

-- INSERT INTO questions (QuesTitle,QuesDesc,QuesScore,QuesTags,UserId) VALUES ('How is PHP different from Java?','I am a Java developer. I have heard that PHP is also a programming language. I want to know how is PHP different from Java?','120','["php","java"]',2);




CREATE TABLE IF NOT EXISTS answers (
    AnsId INT NOT NULL AUTO_INCREMENT,
    AnsDesc VARCHAR(5000) NOT NULL,
    AnsScore INT NOT NULL,
    UserId INT NOT NULL,
    QuesId INT NOT NULL,
    FOREIGN KEY (UserId) REFERENCES users(UserId),
    FOREIGN KEY (QuesId) REFERENCES questions(QuesId),
    PRIMARY KEY (AnsId)
);

INSERT INTO answers (AnsDesc,AnsScore,UserId,QuesId) VALUES ('4','10',3,1);
INSERT INTO answers (AnsDesc,AnsScore,UserId,QuesId) VALUES ('four','40',2,1);
INSERT INTO answers (AnsDesc,AnsScore,UserId,QuesId) VALUES ('6','20',3,2);
INSERT INTO answers (AnsDesc,AnsScore,UserId,QuesId) VALUES ('nine','250',1,3);


-- INSERT INTO answers (AnsDesc,AnsScore,UserId,QuesId) VALUES ('You can connect to MySQL database in PHP using the following code. You have to change the username and password according to your MySQL database. You can also change the database name if you have created a different database. You can also change the table name if you have created a different table. You can also change the column names if you have created different columns.','10',2,1);

-- INSERT INTO answers (AnsDesc,AnsScore,UserId,QuesId) VALUES ('PHP is a server-side scripting language designed for web development but also used as a general-purpose programming language. Java is a general-purpose programming language that is class-based, object-oriented, and designed to have as few implementation dependencies as possible.As of 2019, Java was one of the most popular programming languages in use according to GitHub, particularly for client-server web applications, with a reported 9 million developers.','120',3,2);

-- INSERT INTO answers (AnsDesc,AnsScore,UserId,QuesId) VALUES ('It is intended to let application developers "write once, run anywhere" (WORA), meaning that compiled Java code can run on all platforms that support Java without the need for recompilation. Java applications are typically compiled to bytecode that can run on any Java virtual machine (JVM) regardless of the underlying computer architecture. The syntax of Java is similar to C and C++, but has fewer low-level facilities than either of them.','23',1,2);
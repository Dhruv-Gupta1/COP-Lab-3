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
    UserImg BLOB,
    QueIds JSON,
    AnsIds JSON,
    Rating INT DEFAULT 0,
    PRIMARY KEY (Userid)
);

INSERT INTO users (UserId,UserName,UserEmail,UserPass,Rating) VALUES (1,'admin','admin@gmail.com','admin',100);
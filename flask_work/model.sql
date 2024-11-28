CREATE DATABASE if not exists summarylogin DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

use summarylogin;

CREATE table if not exists accounts(
    id int(11) not null AUTO_INCREMENT,
    username varchar(50) NOT NULL,
    password varchar(255) NOT NULL,
    email varchar(100) NOT NULL,
    PRIMARY KEY(id)
) ENGINE=InnoDB AUTO_INCREMENT = 2 DEFAULT CHARSET = utf8;


-- mysql> source /home/atul/Desktop/Code_vs_code/flask_work/model.sql;
-- Query OK, 1 row affected, 2 warnings (0.01 sec)

-- Database changed
-- Query OK, 0 rows affected, 2 warnings (0.01 sec)
CREATE DATABASE viwit;
USE viwit;

CREATE TABLE  credit_card(
    credit_card_id INT(12) PRIMARY KEY,
    credit_card_owner VARCHAR (50) NOT NULL,
    ccv INT(3) NOT NULL,
    expiration_date DATETIME NOT NULL
);

CREATE TABLE user_viwit (
    user_id INT(12) PRIMARY KEY,
    firstname VARCHAR (30) NOT NULL,
    lastname VARCHAR (30) NOT NULL,
    email VARCHAR (50) NOT NULL,
    reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    user_pasword VARCHAR (128) NOT NULL,
    credit_card INT(12),
    block_account BOOL NOT NULL,
    FOREIGN KEY (credit_card) REFERENCES credit_card(credit_card_id)
);

CREATE TABLE token(
    token_id INT (12) AUTO_INCREMENT PRIMARY KEY,
    token VARCHAR (128) NOT NULL,
    user_id INT (12),
    expiration_date TIMESTAMP NOT NULL,
    creation_date TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW(),
    foreign key (user_id) references user_viwit (user_id)
);



CREATE TABLE login(
    login_id INT (32) AUTO_INCREMENT PRIMARY KEY,
    user_id INT(12) NOT NULL,
    login_date TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user_viwit (user_id)
);


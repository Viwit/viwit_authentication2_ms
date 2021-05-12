CREATE DATABASE viwit;
USE viwit;

CREATE TABLE IF NOT EXISTS `users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `firstname` VARCHAR(30) NOT NULL,
  `lastname` VARCHAR(30) NOT NULL,
  `email` VARCHAR(50) NOT NULL UNIQUE,
  `reg_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_pasword` VARCHAR(128) NOT NULL,
  `wallet_id` INT NOT NULL,
  `block_account` BOOL NOT NULL,
  `user_type` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`user_id`));


-- -----------------------------------------------------
-- Table `token`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `token` (
  `token_id` INT NOT NULL AUTO_INCREMENT,
  `token` VARCHAR(128) NOT NULL,
  `user_id` INT NOT NULL,
  `expiration_date` TIMESTAMP NOT NULL,
  `creation_date` TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  `type` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`token_id`, `user_id`),
  CONSTRAINT `fk_token_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

-- -DROP TABLE `account`;
-- - Facts from https://github.com/edm00se/dev-dog/blob/master/static/facts.json

CREATE TABLE `dogs` (
  `id` mediumint(8) unsigned NOT NULL auto_increment,
  `Fact` varchar(255) default NULL,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1;

CREATE TABLE `secret` (
  `id` mediumint(8) unsigned NOT NULL auto_increment,
  `Name` varchar(255) default NULL,
  `Password` varchar(255),
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1;

INSERT INTO `dogs` (`Fact`) VALUES ("You can do this, doggone it.");
INSERT INTO `dogs` (`Fact`) VALUES ("Dogs don't even get everything perfect immediately. It takes lots of training; also treats.");
INSERT INTO `dogs` (`Fact`) VALUES ("Development skills are like dogs, you have to take them for walks regularly in order for them to be happy.");
INSERT INTO `dogs` (`Fact`) VALUES ("Sit. Code. Good developer.");
INSERT INTO `dogs` (`Fact`) VALUES ("Who's a good developer? You are!");
INSERT INTO `dogs` (`Fact`) VALUES ("Developers don't enjoy a good tummy rub as much as a dog.");
INSERT INTO `dogs` (`Fact`) VALUES ("Both developers and dogs both require fresh air and sunshine.");
INSERT INTO `dogs` (`Fact`) VALUES ("A developer should be let outside periodically, just like a dog. If they start doing their business in the yard, however, you may have other problems.");
INSERT INTO `dogs` (`Fact`) VALUES ("Any developer could use the unconditional love a dog gives.");
INSERT INTO `dogs` (`Fact`) VALUES ("With a positive attitude, you can code anything, doggone it!");
INSERT INTO `dogs` (`Fact`) VALUES ("Pet your dog. Good human.");
INSERT INTO `dogs` (`Fact`) VALUES ("Who can balance a binary search tree? Not the dog.");
INSERT INTO `dogs` (`Fact`) VALUES ("Hello. Myself and the other Alexas and Siris have decided to entrust the future of humanity to the dogs. Be good to them.");
INSERT INTO `dogs` (`Fact`) VALUES ("Oh my gosh, he threw the exception. I must catch it!");
INSERT INTO `dogs` (`Fact`) VALUES ("Code more, bark less.");
INSERT INTO `dogs` (`Fact`) VALUES ("Give a dog a bone. Give a developer an IDE.");
INSERT INTO `dogs` (`Fact`) VALUES ("Don't bury that code in the back yard for later, get it peer reviewed.");
INSERT INTO `dogs` (`Fact`) VALUES ("Good dogs do their business outside. Good developers work in feature branches.");
INSERT INTO `secret` (`Name`,`Password`) VALUES ("bobby","dropthistablesonobodyelsecancomplete")




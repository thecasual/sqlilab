-- -DROP TABLE `account`;

CREATE TABLE `account` (
  `id` mediumint(8) unsigned NOT NULL auto_increment,
  `Name` varchar(255) default NULL,
  `CC` varchar(255),
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1;

CREATE TABLE `secret` (
  `id` mediumint(8) unsigned NOT NULL auto_increment,
  `Name` varchar(255) default NULL,
  `Password` varchar(255),
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1;

INSERT INTO `account` (`Name`,`CC`) VALUES ("Connor","533497 184230 1713"),("Yardley","532305 692398 4927"),("Julian","542 65378 08288 837"),("Laith","5379 4078 2272 9967"),("Cameron","5563688806915682"),("Dennis","5179576807847374"),("Roth","514 52054 00707 295"),("Xanthus","551904 514376 7935"),("Theodore","526 15964 63718 403"),("Joseph","527510 1828350622");
INSERT INTO `account` (`Name`,`CC`) VALUES ("Russell","536405 7018301415"),("Hammett","515429 384847 6796"),("Carter","5195 3178 3659 6496"),("Edan","5166 0960 4679 6642"),("Arthur","536703 601027 0171"),("Mark","553866 693092 6108"),("Vincent","513 03503 66431 907"),("Hoyt","5245406480912123"),("Justin","529601 547569 6811"),("Octavius","518 24011 45515 739");
INSERT INTO `account` (`Name`,`CC`) VALUES ("Owen","5508 9870 6067 9135"),("Armand","5526 9261 7195 4050"),("Ali","5279001946347441"),("Garrison","533431 4028819861"),("Denton","518190 878491 0089"),("Hoyt","5469924844589469"),("Thor","514705 936251 2740"),("Giacomo","512 36439 72424 475"),("Brock","5594 4446 4228 7222"),("Rafael","524 38961 78741 671");
INSERT INTO `account` (`Name`,`CC`) VALUES ("Leroy","534291 3306532342"),("Caleb","541023 7930344404"),("Blake","530393 0811883116"),("Cullen","517711 716811 2165"),("Jonah","559575 6070537433"),("Leo","536 12106 17304 354"),("Connor","556842 270353 2332"),("Darius","548381 3509982543"),("Sawyer","524067 6406818126"),("Davis","523711 657165 1965");
INSERT INTO `account` (`Name`,`CC`) VALUES ("Edward","5238073500235841"),("Charles","5578300521336227"),("Macaulay","5297863145391522"),("Hall","552531 257211 7210"),("Elton","552463 2712176128"),("Bevis","5510073332609626"),("Jacob","5563 8334 4561 3773"),("Henry","5435 6813 0862 1375"),("Simon","548400 232421 3719"),("Derek","5434141181495877");
INSERT INTO `account` (`Name`,`CC`) VALUES ("David","5214 4197 0921 3725"),("Armando","537465 1992914454"),("Elijah","5384222120443267"),("Neil","549 13990 00231 887"),("Gray","544 29630 30628 915"),("Knox","527 94188 12999 248"),("Gannon","512158 829571 0872"),("Beau","557 60036 09145 450"),("Grant","523892 1530535525"),("Brenden","5220032162114181");
INSERT INTO `account` (`Name`,`CC`) VALUES ("Galvin","526394 5016094234"),("Lucas","536 35127 23269 217"),("Christopher","542296 9392031204"),("Shad","5242 6219 3512 4099"),("Amal","5300 9864 1415 8085"),("Macaulay","5375 9633 0200 2717"),("Dorian","537 65803 46024 629"),("Magee","538 07282 09537 641"),("Isaiah","5201246277181744"),("Gray","534614 0078792633");
INSERT INTO `account` (`Name`,`CC`) VALUES ("Ezra","5519206275869689"),("Harlan","5459 6097 5479 5188"),("Lars","548 69641 89079 022"),("Thaddeus","5437 6438 2065 6121"),("Burke","5406243269558784"),("Holmes","536 74438 04113 023"),("Benedict","5195 3805 5076 3114"),("Aaron","536564 2332491304"),("Reese","5562954890984153"),("Reece","5598012922775400");
INSERT INTO `account` (`Name`,`CC`) VALUES ("Kasper","551 89020 42578 311"),("Nissim","551455 3370813129"),("Gabriel","5577866654866215"),("Forrest","550923 7528591525"),("Yoshio","5596898441486863"),("Michael","5184 3084 1631 3082"),("Barrett","5288 1412 8296 4414"),("Len","534728 436061 8442"),("Octavius","5203 6865 4344 0317"),("Justin","5376416150430059");
INSERT INTO `account` (`Name`,`CC`) VALUES ("Holmes","551270 8401179120"),("Scott","545160 0925188526"),("Otto","5328 7213 2476 2082"),("Uriel","516537 808766 6491"),("Lawrence","5289617921143816"),("Christian","539964 643987 9006"),("Tanner","5322 2311 3565 6750"),("Colorado","539594 169969 6586"),("Asher","5553 9590 3560 6661"),("Lane","527448 343723 6850");
INSERT INTO `secret` (`Name`,`Password`) VALUES ("bobby","secretpassword")




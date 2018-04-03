/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50638
Source Host           : localhost:3306
Source Database       : room1

Target Server Type    : MYSQL
Target Server Version : 50638
File Encoding         : 65001

Date: 2018-04-03 12:05:41
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `reseve`
-- ----------------------------
DROP TABLE IF EXISTS `reseve`;
CREATE TABLE `reseve` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `tid` int(11) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rid` (`rid`),
  KEY `tid` (`tid`),
  KEY `uid` (`uid`),
  CONSTRAINT `reseve_ibfk_1` FOREIGN KEY (`rid`) REFERENCES `room` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `reseve_ibfk_2` FOREIGN KEY (`tid`) REFERENCES `time` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `reseve_ibfk_3` FOREIGN KEY (`uid`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of reseve
-- ----------------------------
INSERT INTO `reseve` VALUES ('1', '1', '2018-03-28', '2', '1');
INSERT INTO `reseve` VALUES ('2', '1', '2018-03-28', '3', '1');
INSERT INTO `reseve` VALUES ('3', '1', '2018-03-28', '4', '1');
INSERT INTO `reseve` VALUES ('4', '3', '2018-03-28', '3', '1');
INSERT INTO `reseve` VALUES ('5', '4', '2018-03-28', '2', '1');
INSERT INTO `reseve` VALUES ('6', '5', '2018-03-28', '1', '1');
INSERT INTO `reseve` VALUES ('9', '1', '2018-03-28', '1', '1');
INSERT INTO `reseve` VALUES ('17', '1', '2018-03-29', '1', '1');
INSERT INTO `reseve` VALUES ('18', '1', '2018-03-29', '2', '1');
INSERT INTO `reseve` VALUES ('19', '2', '2018-03-30', '2', '1');
INSERT INTO `reseve` VALUES ('20', '1', '2018-04-02', '2', '1');
INSERT INTO `reseve` VALUES ('21', '2', '2018-03-28', '2', '1');
INSERT INTO `reseve` VALUES ('22', '1', '2018-03-30', '3', '1');
INSERT INTO `reseve` VALUES ('23', '4', '2018-03-29', '2', '1');
INSERT INTO `reseve` VALUES ('24', '4', '2018-03-29', '1', '1');
INSERT INTO `reseve` VALUES ('25', '4', '2018-03-28', '1', '1');
INSERT INTO `reseve` VALUES ('26', '5', '2018-03-29', '1', '1');
INSERT INTO `reseve` VALUES ('27', '1', '2018-03-29', '3', '2');
INSERT INTO `reseve` VALUES ('29', '1', '2018-03-29', '4', '2');
INSERT INTO `reseve` VALUES ('30', '3', '2018-03-29', '4', '2');
INSERT INTO `reseve` VALUES ('31', '4', '2018-03-29', '3', '2');
INSERT INTO `reseve` VALUES ('32', '4', '2018-03-30', '3', '2');
INSERT INTO `reseve` VALUES ('33', '5', '2018-03-30', '5', '2');
INSERT INTO `reseve` VALUES ('34', '2', '2018-03-31', '1', '2');
INSERT INTO `reseve` VALUES ('35', '2', '2018-03-29', '5', '1');
INSERT INTO `reseve` VALUES ('36', '1', '2018-03-31', '2', '1');
INSERT INTO `reseve` VALUES ('37', '2', '2018-03-31', '3', '1');

-- ----------------------------
-- Table structure for `room`
-- ----------------------------
DROP TABLE IF EXISTS `room`;
CREATE TABLE `room` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of room
-- ----------------------------
INSERT INTO `room` VALUES ('1', '菊花室');
INSERT INTO `room` VALUES ('2', '兰花室');
INSERT INTO `room` VALUES ('3', '梅花室');
INSERT INTO `room` VALUES ('4', '竹子室');
INSERT INTO `room` VALUES ('5', '神马室');

-- ----------------------------
-- Table structure for `time`
-- ----------------------------
DROP TABLE IF EXISTS `time`;
CREATE TABLE `time` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datetime` char(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of time
-- ----------------------------
INSERT INTO `time` VALUES ('1', '9:00~10:25');
INSERT INTO `time` VALUES ('2', '10:30~11:55');
INSERT INTO `time` VALUES ('3', '13:00~14:25');
INSERT INTO `time` VALUES ('4', '14:30~15:55');
INSERT INTO `time` VALUES ('5', '16:00~17:25');

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `pwd` char(15) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('gsy121994', '1', 'gao');
INSERT INTO `user` VALUES ('123456789', '2', 'jia');

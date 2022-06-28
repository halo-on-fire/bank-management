/*
 Navicat Premium Data Transfer

 Source Server         : bank
 Source Server Type    : MySQL
 Source Server Version : 80029
 Source Host           : localhost:3306
 Source Schema         : bank

 Target Server Type    : MySQL
 Target Server Version : 80029
 File Encoding         : 65001

 Date: 28/06/2022 03:39:05
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for account
-- ----------------------------
DROP TABLE IF EXISTS `account`;
CREATE TABLE `account`  (
  `Accno` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Age` int NOT NULL,
  `Occup` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Address` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Mob` int NOT NULL,
  `Aadharno` int NULL DEFAULT NULL,
  `amt` double(20, 5) NULL DEFAULT NULL,
  `AccType` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`Accno`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of account
-- ----------------------------
INSERT INTO `account` VALUES (2, 'Hossein', 28, 'Programmer', 'Tehran', 990, 11, 10000000.00000, 'PPF');

-- ----------------------------
-- Table structure for amt
-- ----------------------------
DROP TABLE IF EXISTS `amt`;
CREATE TABLE `amt`  (
  `Accno` int NULL DEFAULT NULL,
  `Amtdeposite` double(20, 5) NULL DEFAULT NULL,
  `month` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of amt
-- ----------------------------
INSERT INTO `amt` VALUES (2, 1000.00000, '50000000');

SET FOREIGN_KEY_CHECKS = 1;

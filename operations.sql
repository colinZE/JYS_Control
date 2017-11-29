/*
Navicat MySQL Data Transfer

Source Server         : 192.168.151.248
Source Server Version : 50525
Source Host           : 192.168.151.248:3306
Source Database       : operations

Target Server Type    : MYSQL
Target Server Version : 50525
File Encoding         : 65001

Date: 2017-11-29 20:06:37
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add group', '2', 'add_group');
INSERT INTO `auth_permission` VALUES ('5', 'Can change group', '2', 'change_group');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete group', '2', 'delete_group');
INSERT INTO `auth_permission` VALUES ('7', 'Can add permission', '3', 'add_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can change permission', '3', 'change_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete permission', '3', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add 用户组', '7', 'add_usergroup');
INSERT INTO `auth_permission` VALUES ('20', 'Can change 用户组', '7', 'change_usergroup');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete 用户组', '7', 'delete_usergroup');
INSERT INTO `auth_permission` VALUES ('22', 'Can add 用户信息', '8', 'add_userinfo');
INSERT INTO `auth_permission` VALUES ('23', 'Can change 用户信息', '8', 'change_userinfo');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete 用户信息', '8', 'delete_userinfo');
INSERT INTO `auth_permission` VALUES ('25', 'Can add 服务器信息', '9', 'add_serverinfo');
INSERT INTO `auth_permission` VALUES ('26', 'Can change 服务器信息', '9', 'change_serverinfo');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete 服务器信息', '9', 'delete_serverinfo');
INSERT INTO `auth_permission` VALUES ('28', 'Can add 机房信息', '10', 'add_datacenter');
INSERT INTO `auth_permission` VALUES ('29', 'Can change 机房信息', '10', 'change_datacenter');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete 机房信息', '10', 'delete_datacenter');
INSERT INTO `auth_permission` VALUES ('31', 'Can add business unit', '11', 'add_businessunit');
INSERT INTO `auth_permission` VALUES ('32', 'Can change business unit', '11', 'change_businessunit');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete business unit', '11', 'delete_businessunit');
INSERT INTO `auth_permission` VALUES ('34', 'Can add 资产信息', '12', 'add_asset');
INSERT INTO `auth_permission` VALUES ('35', 'Can change 资产信息', '12', 'change_asset');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete 资产信息', '12', 'delete_asset');
INSERT INTO `auth_permission` VALUES ('37', 'Can add django session', '13', 'add_djangosession');
INSERT INTO `auth_permission` VALUES ('38', 'Can change django session', '13', 'change_djangosession');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete django session', '13', 'delete_djangosession');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$36000$MwvG1W2rzLyf$7Rt0amieGDlkzfzMoK1mMgZBciLa9D9hEMZsa7xBq7k=', '2017-11-28 16:35:04', '1', 'admin', '', '', '', '1', '1', '2017-09-05 09:48:11');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for cmdb_asset
-- ----------------------------
DROP TABLE IF EXISTS `cmdb_asset`;
CREATE TABLE `cmdb_asset` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `device_type_id` int(11) NOT NULL,
  `device_status_id` int(11) NOT NULL,
  `cabinet_num` varchar(30) DEFAULT NULL,
  `cabinet_order` varchar(30) DEFAULT NULL,
  `bussiness_unit_id` int(11) DEFAULT NULL,
  `idc_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `CMDB_asset_bussiness_unit_id_3cb20742_fk_CMDB_businessunit_id` (`bussiness_unit_id`),
  KEY `CMDB_asset_idc_id_d93e2555_fk_CMDB_datacenter_id` (`idc_id`),
  CONSTRAINT `CMDB_asset_idc_id_d93e2555_fk_CMDB_datacenter_id` FOREIGN KEY (`idc_id`) REFERENCES `cmdb_datacenter` (`id`),
  CONSTRAINT `CMDB_asset_bussiness_unit_id_3cb20742_fk_CMDB_businessunit_id` FOREIGN KEY (`bussiness_unit_id`) REFERENCES `cmdb_businessunit` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cmdb_asset
-- ----------------------------
INSERT INTO `cmdb_asset` VALUES ('6', '1', '2', '123', '123', '20', '51');
INSERT INTO `cmdb_asset` VALUES ('7', '1', '2', '123', '1', '20', '51');
INSERT INTO `cmdb_asset` VALUES ('8', '1', '2', '123', '2', '20', '51');

-- ----------------------------
-- Table structure for cmdb_businessunit
-- ----------------------------
DROP TABLE IF EXISTS `cmdb_businessunit`;
CREATE TABLE `cmdb_businessunit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cmdb_businessunit
-- ----------------------------
INSERT INTO `cmdb_businessunit` VALUES ('2', '金盈所-前台');
INSERT INTO `cmdb_businessunit` VALUES ('20', '金盈所-测试');

-- ----------------------------
-- Table structure for cmdb_datacenter
-- ----------------------------
DROP TABLE IF EXISTS `cmdb_datacenter`;
CREATE TABLE `cmdb_datacenter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `address` varchar(256) DEFAULT NULL,
  `telphone` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cmdb_datacenter
-- ----------------------------
INSERT INTO `cmdb_datacenter` VALUES ('1', '鹏博士', '1230', '123456');
INSERT INTO `cmdb_datacenter` VALUES ('51', '公司', '1', '1');

-- ----------------------------
-- Table structure for cmdb_serverinfo
-- ----------------------------
DROP TABLE IF EXISTS `cmdb_serverinfo`;
CREATE TABLE `cmdb_serverinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` char(39) NOT NULL,
  `model` varchar(256) NOT NULL,
  `manufacture` varchar(256) NOT NULL,
  `sn` varchar(256) NOT NULL,
  `os_platform` varchar(128) NOT NULL,
  `os_version` varchar(128) NOT NULL,
  `cpu` varchar(64) NOT NULL,
  `cpu_physical_count` int(11) NOT NULL,
  `cpu_count` int(11) NOT NULL,
  `mem` varchar(256) NOT NULL,
  `mem_val` double NOT NULL,
  `create_at` datetime NOT NULL,
  `asset_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ip` (`ip`),
  UNIQUE KEY `asset_id` (`asset_id`),
  CONSTRAINT `CMDB_serverinfo_asset_id_35e73aec_fk_CMDB_asset_id` FOREIGN KEY (`asset_id`) REFERENCES `cmdb_asset` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cmdb_serverinfo
-- ----------------------------
INSERT INTO `cmdb_serverinfo` VALUES ('7', '192.168.151.248', 'R720', 'DELL', '123456', 'Linux', 'CentOS 6.4', 'E5 2620 V3', '2', '6', 'DDR3 8G ECC', '64', '2017-11-16 07:23:25', '6');
INSERT INTO `cmdb_serverinfo` VALUES ('10', '192.168.151.247', 'TEST', 'TEST', 'TEST', 'Linux', 'TEST', 'TEST', '1', '1', '1', '1', '2017-11-28 09:06:43', '7');
INSERT INTO `cmdb_serverinfo` VALUES ('11', '192.168.151.249', 'TEST', 'TEST', 'TEST', 'Linux', 'TEST', 'TEST', '1', '1', '1', '1', '2017-11-28 09:09:59', '8');

-- ----------------------------
-- Table structure for cmdb_userinfo
-- ----------------------------
DROP TABLE IF EXISTS `cmdb_userinfo`;
CREATE TABLE `cmdb_userinfo` (
  `username` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL,
  `department` varchar(100) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `CMDB_userinfo_username_45630b93_uniq` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cmdb_userinfo
-- ----------------------------
INSERT INTO `cmdb_userinfo` VALUES ('wzm', '1234', '123', '123@qq.com', '15210254569');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2017-10-27 02:48:04', '鹏博士', '鹏博士', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2017-10-27 02:48:10', '鹏博士', '鹏博士', '2', '[{\"changed\": {\"fields\": [\"telphone\"]}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2017-10-27 04:34:16', '鹏博士', '鹏博士', '2', '[{\"changed\": {\"fields\": [\"telphone\"]}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2017-11-03 07:21:35', '1', '金盈所-测试', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2017-11-03 10:05:00', '2', '金盈所-前台', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2017-11-06 07:13:34', '1', '鹏博士1', '2', '[{\"changed\": {\"fields\": [\"name\"]}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2017-11-06 07:13:47', '1', '鹏博士', '2', '[{\"changed\": {\"fields\": [\"name\"]}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2017-11-06 07:14:12', '1', '鹏博士的', '2', '[{\"changed\": {\"fields\": [\"name\"]}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2017-11-06 07:14:30', '1', '鹏博士', '2', '[{\"changed\": {\"fields\": [\"name\"]}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('10', '2017-11-06 07:36:52', '1', '鹏博士122', '2', '[]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('11', '2017-11-06 07:40:44', '1', '鹏博士1220', '2', '[{\"changed\": {\"fields\": [\"name\"]}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('12', '2017-11-06 07:54:30', '1', '鹏博士1221', '2', '[{\"changed\": {\"fields\": [\"name\"]}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('13', '2017-11-06 07:54:40', '1', '鹏博士1220', '2', '[{\"changed\": {\"fields\": [\"name\"]}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('14', '2017-11-06 07:55:09', '1', '鹏博士1221', '2', '[{\"changed\": {\"fields\": [\"name\"]}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('15', '2017-11-08 09:49:30', '1', '鹏博士-J20-2', '2', '[{\"changed\": {\"fields\": [\"cabinet_order\"]}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('16', '2017-11-08 09:54:03', '1', '鹏博士-J20-2', '2', '[{\"changed\": {\"fields\": [\"bussiness_unit\"]}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('17', '2017-11-08 09:55:03', '1', '192.168.151.248', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('18', '2017-11-08 09:56:17', '1', '鹏博士-J20-None', '2', '[{\"changed\": {\"fields\": [\"cabinet_order\"]}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('19', '2017-11-08 09:56:30', '1', '鹏博士-J20-1', '2', '[{\"changed\": {\"fields\": [\"cabinet_order\"]}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('20', '2017-11-14 02:03:56', '3', '192.168.151.148', '3', '', '9', '1');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('12', 'CMDB', 'asset');
INSERT INTO `django_content_type` VALUES ('11', 'CMDB', 'businessunit');
INSERT INTO `django_content_type` VALUES ('10', 'CMDB', 'datacenter');
INSERT INTO `django_content_type` VALUES ('13', 'CMDB', 'djangosession');
INSERT INTO `django_content_type` VALUES ('9', 'CMDB', 'serverinfo');
INSERT INTO `django_content_type` VALUES ('7', 'CMDB', 'usergroup');
INSERT INTO `django_content_type` VALUES ('8', 'CMDB', 'userinfo');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2017-09-05 09:42:45');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2017-09-05 09:42:50');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2017-09-05 09:42:51');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2017-09-05 09:42:51');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2017-09-05 09:42:52');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2017-09-05 09:42:53');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2017-09-05 09:42:54');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2017-09-05 09:42:54');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2017-09-05 09:42:54');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2017-09-05 09:42:54');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2017-09-05 09:42:54');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2017-09-05 09:42:55');
INSERT INTO `django_migrations` VALUES ('13', 'sessions', '0001_initial', '2017-09-05 09:42:55');
INSERT INTO `django_migrations` VALUES ('14', 'CMDB', '0001_initial', '2017-09-05 10:03:27');
INSERT INTO `django_migrations` VALUES ('15', 'CMDB', '0002_auto_20170908_1623', '2017-09-08 08:24:02');
INSERT INTO `django_migrations` VALUES ('16', 'CMDB', '0003_auto_20170921_1743', '2017-09-21 09:43:33');
INSERT INTO `django_migrations` VALUES ('17', 'CMDB', '0004_auto_20170922_1720', '2017-09-22 09:20:33');
INSERT INTO `django_migrations` VALUES ('18', 'CMDB', '0005_auto_20171010_1726', '2017-10-10 09:26:55');
INSERT INTO `django_migrations` VALUES ('19', 'CMDB', '0006_auto_20171011_1526', '2017-10-11 07:26:34');
INSERT INTO `django_migrations` VALUES ('20', 'CMDB', '0007_auto_20171018_1448', '2017-10-18 06:49:14');
INSERT INTO `django_migrations` VALUES ('21', 'CMDB', '0002_delete_serverinfo', '2017-10-18 09:23:54');
INSERT INTO `django_migrations` VALUES ('22', 'CMDB', '0003_serverinfo', '2017-10-18 09:24:32');
INSERT INTO `django_migrations` VALUES ('23', 'CMDB', '0002_auto_20171101_1605', '2017-11-01 08:05:48');
INSERT INTO `django_migrations` VALUES ('24', 'CMDB', '0002_auto_20171101_1620', '2017-11-01 08:20:24');
INSERT INTO `django_migrations` VALUES ('25', 'CMDB', '0003_delete_serverinfo', '2017-11-08 02:20:11');
INSERT INTO `django_migrations` VALUES ('26', 'CMDB', '0004_serverinfo', '2017-11-08 02:20:32');
INSERT INTO `django_migrations` VALUES ('27', 'CMDB', '0005_auto_20171108_1024', '2017-11-08 02:25:01');
INSERT INTO `django_migrations` VALUES ('28', 'CMDB', '0006_serverinfo', '2017-11-08 02:25:21');
INSERT INTO `django_migrations` VALUES ('29', 'CMDB', '0007_djangosession', '2017-11-23 09:28:15');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('0raatw8zxhji0nk9nr89qp4xws2dxtvw', 'OWE2NWRkN2JlZWFlZWU4ZWRiYjBiYjM3ZWQzNTM2OGIwYTNjZDk4Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmODQ4YTMwNmIwYmZmZmIwYTY5NjExZjg1NmFjYjIwZmJmNzU5Y2IwIn0=', '2017-09-19 12:14:39');
INSERT INTO `django_session` VALUES ('292bjm6cqnauuytaflf7e9xa29p0mf4g', 'ZDU0MWY0Y2E3YzVmN2Y5YjkzNWZhNTI5NTIxNTJlNGY3YzVmYmZiYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmODQ4YTMwNmIwYmZmZmIwYTY5NjExZjg1NmFjYjIwZmJmNzU5Y2IwIiwidXNlciI6MX0=', '2017-12-07 12:16:01');
INSERT INTO `django_session` VALUES ('5tcdb2bditk9wi3ldbjm9w93s2uge87w', 'OWE2NWRkN2JlZWFlZWU4ZWRiYjBiYjM3ZWQzNTM2OGIwYTNjZDk4Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmODQ4YTMwNmIwYmZmZmIwYTY5NjExZjg1NmFjYjIwZmJmNzU5Y2IwIn0=', '2017-11-14 03:02:31');
INSERT INTO `django_session` VALUES ('6ukjvqcgi5zc2hm357cjtzrcdec952de', 'ZDU0MWY0Y2E3YzVmN2Y5YjkzNWZhNTI5NTIxNTJlNGY3YzVmYmZiYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmODQ4YTMwNmIwYmZmZmIwYTY5NjExZjg1NmFjYjIwZmJmNzU5Y2IwIiwidXNlciI6MX0=', '2017-12-07 09:25:44');
INSERT INTO `django_session` VALUES ('99wwenftqmwa0n7uths36yrz7cblsa1r', 'OWE2NWRkN2JlZWFlZWU4ZWRiYjBiYjM3ZWQzNTM2OGIwYTNjZDk4Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmODQ4YTMwNmIwYmZmZmIwYTY5NjExZjg1NmFjYjIwZmJmNzU5Y2IwIn0=', '2017-11-16 13:58:18');
INSERT INTO `django_session` VALUES ('cuku2ha4lye4mldcgitdm38np78uugk6', 'OWE2NWRkN2JlZWFlZWU4ZWRiYjBiYjM3ZWQzNTM2OGIwYTNjZDk4Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmODQ4YTMwNmIwYmZmZmIwYTY5NjExZjg1NmFjYjIwZmJmNzU5Y2IwIn0=', '2017-09-19 12:18:09');
INSERT INTO `django_session` VALUES ('jcttswzhsc4exfm7cdu2fjbxfz5xm8h8', 'ZDU0MWY0Y2E3YzVmN2Y5YjkzNWZhNTI5NTIxNTJlNGY3YzVmYmZiYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmODQ4YTMwNmIwYmZmZmIwYTY5NjExZjg1NmFjYjIwZmJmNzU5Y2IwIiwidXNlciI6MX0=', '2017-12-07 12:11:22');
INSERT INTO `django_session` VALUES ('u5m740w82qdqcynfmw98fopxbu3g8ixs', 'OWE2NWRkN2JlZWFlZWU4ZWRiYjBiYjM3ZWQzNTM2OGIwYTNjZDk4Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmODQ4YTMwNmIwYmZmZmIwYTY5NjExZjg1NmFjYjIwZmJmNzU5Y2IwIn0=', '2017-11-08 07:37:06');
INSERT INTO `django_session` VALUES ('uk5virknp36lmkgbrjhotyk3erwiscxg', 'ZDU0MWY0Y2E3YzVmN2Y5YjkzNWZhNTI5NTIxNTJlNGY3YzVmYmZiYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmODQ4YTMwNmIwYmZmZmIwYTY5NjExZjg1NmFjYjIwZmJmNzU5Y2IwIiwidXNlciI6MX0=', '2017-12-07 08:08:40');
INSERT INTO `django_session` VALUES ('vzdljbn2x57tk0fke674bgo6te6stz4d', 'OWE2NWRkN2JlZWFlZWU4ZWRiYjBiYjM3ZWQzNTM2OGIwYTNjZDk4Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmODQ4YTMwNmIwYmZmZmIwYTY5NjExZjg1NmFjYjIwZmJmNzU5Y2IwIn0=', '2017-09-19 12:20:05');
INSERT INTO `django_session` VALUES ('zjk25bi7awyb3vyzglsu1cc7ed25mxqc', 'OWE2NWRkN2JlZWFlZWU4ZWRiYjBiYjM3ZWQzNTM2OGIwYTNjZDk4Zjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmODQ4YTMwNmIwYmZmZmIwYTY5NjExZjg1NmFjYjIwZmJmNzU5Y2IwIn0=', '2017-10-06 09:21:46');
INSERT INTO `django_session` VALUES ('zka5f67m1j52r4vn58th8268lqnhac52', 'ZDU0MWY0Y2E3YzVmN2Y5YjkzNWZhNTI5NTIxNTJlNGY3YzVmYmZiYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmODQ4YTMwNmIwYmZmZmIwYTY5NjExZjg1NmFjYjIwZmJmNzU5Y2IwIiwidXNlciI6MX0=', '2017-12-12 16:35:04');

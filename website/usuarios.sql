-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-07-2022 a las 23:41:28
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `usuarios`
--
CREATE DATABASE IF NOT EXISTS `usuarios` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `usuarios`;

DELIMITER $$
--
-- Procedimientos
--
DROP PROCEDURE IF EXISTS `spDeleteUser`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `spDeleteUser` (IN `_idUser` INT(3))   DELETE FROM `tableuser` WHERE (`idUser`) = `_idUser`$$

DROP PROCEDURE IF EXISTS `spInsertUser`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `spInsertUser` (IN `_email` VARCHAR(150), IN `_user` VARCHAR(100), IN `_pass` VARCHAR(150))   BEGIN

INSERT INTO tableuser (`email`,`user`,`pass`) VALUES (`_email`,`_user`,`_pass`);

END$$

DROP PROCEDURE IF EXISTS `spLogin`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `spLogin` (IN `_user` VARCHAR(150), IN `_pass` VARCHAR(150))   BEGIN

SELECT * FROM tableuser WHERE `user` = _user AND `pass` = _pass;

END$$

DROP PROCEDURE IF EXISTS `spSearchId`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `spSearchId` (IN `_USER` VARCHAR(150), IN `_PASS` VARCHAR(150))   BEGIN

SELECT idUser from tableuser WHERE user =  _USER AND pass = _PASS; 

END$$

DROP PROCEDURE IF EXISTS `spSearchIdUserS`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `spSearchIdUserS` ()   BEGIN

SELECT idUserS FROM session WHERE idSession = 1;

END$$

DROP PROCEDURE IF EXISTS `spSession`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `spSession` ()   BEGIN

SELECT session FROM session WHERE idSession = 1;

END$$

DROP PROCEDURE IF EXISTS `spUpdateIdUserS`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `spUpdateIdUserS` (IN `_IDUSER` INT)   BEGIN

UPDATE session
SET idUserS = _IDUSER;

END$$

DROP PROCEDURE IF EXISTS `spUpdateSession`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `spUpdateSession` (IN `_SESSION` VARCHAR(100))   BEGIN

UPDATE session
SET session = _SESSION
WHERE idSession = 1;

END$$

DROP PROCEDURE IF EXISTS `spUpdateUser`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `spUpdateUser` (IN `_idUser` INT(5), IN `_email` VARCHAR(150), IN `_user` VARCHAR(100), IN `_pass` VARCHAR(150))   BEGIN
UPDATE `tableuser` SET 
`email`=`_email`,
`user`=`_user`,
`pass`=`_pass` 
WHERE `idUser` = `_idUser`;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$320000$0z4MUdYkT6UM2bNyig0rO6$MjmIGrW3uUmHmN07fjdLi/sWNq0FIKOCpcpb/ohdMK8=', '2022-06-11 17:51:36.074637', 1, 'david', '', '', 'danorena755@misena.edu.co', 1, 1, '2022-06-11 17:50:23.398430');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-06-11 17:47:57.855706'),
(2, 'auth', '0001_initial', '2022-06-11 17:47:58.397868'),
(3, 'admin', '0001_initial', '2022-06-11 17:47:58.525280'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-06-11 17:47:58.537283'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-06-11 17:47:58.550774'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-06-11 17:47:58.619621'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-06-11 17:47:58.677621'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-06-11 17:47:58.701642'),
(9, 'auth', '0004_alter_user_username_opts', '2022-06-11 17:47:58.715322'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-06-11 17:47:58.756167'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-06-11 17:47:58.761151'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-06-11 17:47:58.773171'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-06-11 17:47:58.798612'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-06-11 17:47:58.820631'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-06-11 17:47:58.843623'),
(16, 'auth', '0011_update_proxy_permissions', '2022-06-11 17:47:58.855626'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-06-11 17:47:58.877765'),
(18, 'sessions', '0001_initial', '2022-06-11 17:47:58.916747');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('xv8gy15uubts36fdlmzmk213x1uacq8l', '.eJxVjEEOwiAQRe_C2hAYsAWX7nsGMsOAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnERWpx-N8L4SHUHfMd6azK2ui4zyV2RB-1yapye18P9OyjYy7ceFSTwAxrtBs4WFWhLmpiBKOczApKy2RI5hZaSU8YSO448RuM9RPH-AO5lOKE:1o05Gq:AKWoj-1mcmNobp0pzmKhJZcnEUKhMi72HTG5hxNSmnE', '2022-06-25 17:51:36.077639');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `itemsapp_tableuser`
--

DROP TABLE IF EXISTS `itemsapp_tableuser`;
CREATE TABLE IF NOT EXISTS `itemsapp_tableuser` (
  `idUser` int(5) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `user` varchar(100) NOT NULL,
  `pass` varchar(150) NOT NULL,
  PRIMARY KEY (`idUser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `session`
--

DROP TABLE IF EXISTS `session`;
CREATE TABLE IF NOT EXISTS `session` (
  `idSession` int(11) NOT NULL,
  `session` varchar(100) NOT NULL,
  `idUserS` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `session`
--

INSERT INTO `session` (`idSession`, `session`, `idUserS`) VALUES
(1, 'True', 11);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tableuser`
--

DROP TABLE IF EXISTS `tableuser`;
CREATE TABLE IF NOT EXISTS `tableuser` (
  `idUser` int(5) NOT NULL AUTO_INCREMENT,
  `email` varchar(150) NOT NULL,
  `user` varchar(100) NOT NULL,
  `pass` varchar(150) NOT NULL,
  PRIMARY KEY (`idUser`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tableuser`
--

INSERT INTO `tableuser` (`idUser`, `email`, `user`, `pass`) VALUES
(1, 'email', 'user', 'pass'),
(11, '', '', ''),
(42, 'idasystem_adsi@outlook.es', 'David', 'ss'),
(43, 'rr@gmail.com', 'rr', 'rr'),
(44, 'a@gmail.com', 'ab', 'ab'),
(45, 'asd@sumama.com', 'asd', 'asd'),
(46, 'elhptadel@perreo.com', 'Pablo', '2'),
(47, 'el@asc.co', 'pablo', '1');

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

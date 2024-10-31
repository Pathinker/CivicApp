-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 31-10-2024 a las 23:09:24
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `civicapp_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador`
--

CREATE TABLE `administrador` (
  `ID_administrador` int(11) NOT NULL,
  `Nombre` varchar(100) DEFAULT NULL,
  `Correo_electronico_gobierno` varchar(100) DEFAULT NULL,
  `Numero_celular` varchar(15) DEFAULT NULL,
  `CURP` varchar(18) DEFAULT NULL,
  `Contraseña` varchar(100) DEFAULT NULL,
  `Clave_administrador` varchar(50) DEFAULT NULL,
  `Fecha_asignacion` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador_propuesta`
--

CREATE TABLE `administrador_propuesta` (
  `ID_administrador` int(11) NOT NULL,
  `ID_propuesta` int(11) NOT NULL,
  `Fecha_revision` date DEFAULT NULL,
  `Observaciones` text DEFAULT NULL,
  `Estado` enum('pendiente','en revision','aprobado','rechazado','elegido','completado') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `propuesta`
--

CREATE TABLE `propuesta` (
  `ID_propuesta` int(11) NOT NULL,
  `ID_usuario` int(11) DEFAULT NULL,
  `Nombre` varchar(100) DEFAULT NULL,
  `Descripcion` text DEFAULT NULL,
  `Numero_votos` int(11) DEFAULT NULL,
  `Fecha_creacion` date DEFAULT NULL,
  `Categoria` varchar(50) DEFAULT NULL,
  `Ubicacion` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `ID_usuario` int(11) NOT NULL,
  `Apellido_Paterno` varchar(100) DEFAULT NULL,
  `Apellido_Materno` varchar(100) DEFAULT NULL,
  `Nombre` varchar(100) DEFAULT NULL,
  `Correo_electronico` varchar(100) DEFAULT NULL,
  `RFC` varchar(13) DEFAULT NULL,
  `Numero_celular` varchar(15) DEFAULT NULL,
  `Domicilio` varchar(255) DEFAULT NULL,
  `Contraseña` varchar(100) DEFAULT NULL,
  `CURP` varchar(18) DEFAULT NULL,
  `Fecha_registro` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `voto`
--

CREATE TABLE `voto` (
  `ID_voto` int(11) NOT NULL,
  `ID_usuario` int(11) DEFAULT NULL,
  `ID_propuesta` int(11) DEFAULT NULL,
  `Fecha_voto` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administrador`
--
ALTER TABLE `administrador`
  ADD PRIMARY KEY (`ID_administrador`),
  ADD UNIQUE KEY `Correo_electronico_gobierno` (`Correo_electronico_gobierno`),
  ADD UNIQUE KEY `CURP` (`CURP`);

--
-- Indices de la tabla `administrador_propuesta`
--
ALTER TABLE `administrador_propuesta`
  ADD PRIMARY KEY (`ID_administrador`,`ID_propuesta`),
  ADD KEY `ID_propuesta` (`ID_propuesta`);

--
-- Indices de la tabla `propuesta`
--
ALTER TABLE `propuesta`
  ADD PRIMARY KEY (`ID_propuesta`),
  ADD KEY `ID_usuario` (`ID_usuario`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`ID_usuario`),
  ADD UNIQUE KEY `Correo_electronico` (`Correo_electronico`),
  ADD UNIQUE KEY `RFC` (`RFC`),
  ADD UNIQUE KEY `CURP` (`CURP`);

--
-- Indices de la tabla `voto`
--
ALTER TABLE `voto`
  ADD PRIMARY KEY (`ID_voto`),
  ADD UNIQUE KEY `UC_Voto` (`ID_usuario`,`ID_propuesta`),
  ADD KEY `ID_propuesta` (`ID_propuesta`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `administrador`
--
ALTER TABLE `administrador`
  MODIFY `ID_administrador` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `propuesta`
--
ALTER TABLE `propuesta`
  MODIFY `ID_propuesta` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `ID_usuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `voto`
--
ALTER TABLE `voto`
  MODIFY `ID_voto` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `administrador_propuesta`
--
ALTER TABLE `administrador_propuesta`
  ADD CONSTRAINT `administrador_propuesta_ibfk_1` FOREIGN KEY (`ID_administrador`) REFERENCES `administrador` (`ID_administrador`),
  ADD CONSTRAINT `administrador_propuesta_ibfk_2` FOREIGN KEY (`ID_propuesta`) REFERENCES `propuesta` (`ID_propuesta`);

--
-- Filtros para la tabla `propuesta`
--
ALTER TABLE `propuesta`
  ADD CONSTRAINT `propuesta_ibfk_1` FOREIGN KEY (`ID_usuario`) REFERENCES `usuario` (`ID_usuario`);

--
-- Filtros para la tabla `voto`
--
ALTER TABLE `voto`
  ADD CONSTRAINT `voto_ibfk_1` FOREIGN KEY (`ID_usuario`) REFERENCES `usuario` (`ID_usuario`),
  ADD CONSTRAINT `voto_ibfk_2` FOREIGN KEY (`ID_propuesta`) REFERENCES `propuesta` (`ID_propuesta`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-07-2024 a las 16:20:26
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `academia`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos`
--

CREATE TABLE `alumnos` (
  `AlumnoID` int(11) NOT NULL,
  `AlumnoDNI` varchar(12) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Apellido` varchar(50) NOT NULL,
  `FechaNacimiento` date NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Telefono` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `alumnos`
--

INSERT INTO `alumnos` (`AlumnoID`, `AlumnoDNI`, `Nombre`, `Apellido`, `FechaNacimiento`, `Email`, `Telefono`) VALUES
(1, '12345', 'Juan', 'Pérez', '2000-01-15', 'juan.perez@example.com', '123-456-7890'),
(2, '54321', 'María', 'González', '1998-03-22', 'maria.gonzalez@example.com', '234-567-8901'),
(3, '56789', 'ALEYDA', 'Martínez', '1999-05-30', 'luis.martinez@example.com', '345-678-9012'),
(4, '98765', 'ANA', 'Rodríguez', '2001-07-11', 'ana.rodriguez@example.com', '456-789-0123');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`AlumnoID`),
  ADD UNIQUE KEY `AlumnoDNI` (`AlumnoDNI`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  MODIFY `AlumnoID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cursos`
--

CREATE TABLE `cursos` (
  `CursoID` int(11) NOT NULL,
  `CursoCodigo` varchar(30) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Descripcion` text NOT NULL,
  `Duracion` int(11) NOT NULL,
  `Precio` float(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `cursos`
--

INSERT INTO `cursos` (`CursoID`, `CursoCodigo`, `Nombre`, `Descripcion`, `Duracion`, `Precio`) VALUES
(1, 'IP01', 'Introducción a la Programación', 'Curso básico de programación en diferentes lenguajes.', 8, 0.00),
(2, 'BD01', 'Bases de Datos', 'Fundamentos de bases de datos relacionales y no relacionales.', 10, 0.00),
(3, 'DW01', 'Desarrollo Web', 'Desarrollo de aplicaciones web usando HTML, CSS y JavaScript.', 12, 0.00),
(4, 'SI01', 'Seguridad Informática', 'Conceptos y prácticas de seguridad en el ámbito informático.', 6, 0.00),
(5, 'IA01', 'Inteligencia Artificial', 'Introducción a los conceptos y aplicaciones de la IA.', 14, 0.00);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`CursoID`),
  ADD UNIQUE KEY `CursoCodigo` (`CursoCodigo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cursos`
--
ALTER TABLE `cursos`
  MODIFY `CursoID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos_cursos`
--

CREATE TABLE `alumnos_cursos` (
  `AlumnoCursoID` int(11) NOT NULL,
  `AlumnoID` int(11) NOT NULL,
  `CursoID` int(11) NOT NULL,
  `FechaInscripcion` date NOT NULL,
  `Horario` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `alumnos_cursos`
--

INSERT INTO `alumnos_cursos` (`AlumnoCursoID`, `AlumnoID`, `CursoID`, `FechaInscripcion`, `Horario`) VALUES
(1, 1, 1, '2024-01-15', 'Lunes 10:00-12:00'),
(2, 2, 2, '2024-01-20', 'Martes 14:00-16:00'),
(3, 3, 3, '2024-01-25', 'Miércoles 09:00-11:00'),
(4, 4, 4, '2024-01-30', 'Jueves 15:00-17:00'),
(5, 5, 5, '2024-02-05', 'Viernes 11:00-13:00');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alumnos_cursos`
--
ALTER TABLE `alumnos_cursos`
  ADD PRIMARY KEY (`AlumnoCursoID`),
  ADD KEY `AlumnoID` (`AlumnoID`),
  ADD KEY `CursoID` (`CursoID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `alumnos_cursos`
--
ALTER TABLE `alumnos_cursos`
  MODIFY `AlumnoCursoID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `alumnos_cursos`
--
ALTER TABLE `alumnos_cursos`
  ADD CONSTRAINT `alumnos_cursos_ibfk_1` FOREIGN KEY (`AlumnoID`) REFERENCES `alumnos` (`AlumnoID`),
  ADD CONSTRAINT `alumnos_cursos_ibfk_2` FOREIGN KEY (`CursoID`) REFERENCES `cursos` (`CursoID`);
COMMIT;

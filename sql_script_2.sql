-- ----------------  CREAR UNA BASE DE DATOS
CREATE DATABASE nombre_de_tu_base_de_datos CHARACTER SET utf8mb4 
                                                 COLLATE utf8mb4_unicode_ci;


-- ------------------------- CREAR UNA TABLA
CREATE TABLE usuarios (
  dni varchar(11) NOT NULL ,
  apellidos varchar(30) NOT NULL,
  nombres varchar(30) NOT NULL,
  direccion varchar(100) NOT NULL,
  email varchar(50) NOT NULL,
  PRIMARY KEY (dni)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; 


-- ------------------------ CREAR UN INDICE
CREATE INDEX idx_apellidos ON usuarios(apellidos);

-- ------------------ CREACION DE RELACIONES ENTRE TABLAS  ----------------

-- ----------------------- CREAR TABLA E INDICE AUTOMÁTICAMENTE
CREATE TABLE trabajadores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dni VARCHAR(10) UNIQUE,           -- Genera automáticamente un índice 
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    fecha_nacimiento DATE,
    salario DECIMAL(10, 2)
);


-- ------------------------- CREA UNA TABLA CON LLAVE FORÁNEA 
CREATE TABLE dotacion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    trabajador_id INT,
    item VARCHAR(100),
    fecha DATE,
    cantidad INT,
    FOREIGN KEY (trabajador_id) REFERENCES trabajadores(id)
);

-- --------------------- << SISTEMA ACADEMIA DE CURSOS >>
-- ---------------------  SQL PARA CREACIÓN DE TABLAS 
-- Tabla Alumnos
CREATE TABLE Alumnos (
    AlumnoID INT AUTO_INCREMENT PRIMARY KEY,
    AlumnoDNI VARCHAR(12) UNIQUE NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    FechaNacimiento DATE NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Telefono VARCHAR(20) NOT NULL
);

-- Tabla Cursos
CREATE TABLE Cursos (
    CursoID INT AUTO_INCREMENT PRIMARY KEY,
    CursoCodigo  VARCHAR(30) UNIQUE NOT NULL,
    Nombre VARCHAR(100) NOT NULL,
    Descripcion TEXT NOT NULL,
    Duracion INT  NOT NULL,           -- duración en horas o semanas
    Precio FLOAT(10,2) NOT NULL
);


-- Tabla Alumnos_Cursos
CREATE TABLE Alumnos_Cursos (
    AlumnoCursoID INT AUTO_INCREMENT PRIMARY KEY,
    AlumnoID INT NOT NULL,
    CursoID INT NOT NULL,
    FechaInscripcion DATE NOT NULL,
    Horario VARCHAR(50) NOT NULL,
    FOREIGN KEY (AlumnoID) REFERENCES Alumnos(AlumnoID),
    FOREIGN KEY (CursoID) REFERENCES Cursos(CursoID)
);


-- ------------- INSERTAR DATOS EN TABLAS
-- Insertar Datos en la Tabla Alumnos

INSERT INTO Alumnos (AlumnoDNI, Nombre, Apellido, FechaNacimiento, Email, Telefono) VALUES
('12345', 'Juan', 'Pérez', '2000-01-15', 'juan.perez@example.com', '123-456-7890'),
('54321', 'María', 'González', '1998-03-22', 'maria.gonzalez@example.com', '234-567-8901'),
('56789', 'Luis', 'Martínez', '1999-05-30', 'luis.martinez@example.com', '345-678-9012'),
('98765', 'Ana', 'Rodríguez', '2001-07-11', 'ana.rodriguez@example.com', '456-789-0123'),
('11111', 'Carlos', 'López', '2002-09-05', 'carlos.lopez@example.com', '567-890-1234'),
('22222', 'Lucía', 'Fernández', '1997-11-17', 'lucia.fernandez@example.com', '678-901-2345'),
('77777', 'Miguel', 'Hernández', '1996-12-25', 'miguel.hernandez@example.com', '789-012-3456'),
('99999', 'Sofía', 'García', '1995-04-14', 'sofia.garcia@example.com', '890-123-4567'),
('44444', 'David', 'Torres', '2000-08-18', 'david.torres@example.com', '901-234-5678'),
('66666', 'Laura', 'Ramírez', '1998-06-23', 'laura.ramirez@example.com', '012-345-6789');


--  Insertar Datos en la Tabla Cursos
INSERT INTO Cursos (CursoCodigo, Nombre, Descripcion, Duracion) VALUES
('IP01', 'Introducción a la Programación', 'Curso básico de programación en diferentes lenguajes.', 8),
('BD01', 'Bases de Datos', 'Fundamentos de bases de datos relacionales y no relacionales.', 10),
('DW01', 'Desarrollo Web', 'Desarrollo de aplicaciones web usando HTML, CSS y JavaScript.', 12),
('SI01', 'Seguridad Informática', 'Conceptos y prácticas de seguridad en el ámbito informático.', 6),
('IA01', 'Inteligencia Artificial', 'Introducción a los conceptos y aplicaciones de la IA.', 14);


--  Insertar Datos en la Tabla Alumnos_Cursos
INSERT INTO Alumnos_Cursos (AlumnoID, CursoID, FechaInscripcion, Horario) VALUES 
(1, 1, '2024-01-15', 'Lunes 10:00-12:00'), 
(2, 2, '2024-01-20', 'Martes 14:00-16:00'), 
(3, 3, '2024-01-25', 'Miércoles 09:00-11:00'), 
(4, 4, '2024-01-30', 'Jueves 15:00-17:00'), 
(5, 5, '2024-02-05', 'Viernes 11:00-13:00'), 
(6, 1, '2024-02-10', 'Lunes 10:00-12:00'), 
(7, 2, '2024-02-15', 'Martes 14:00-16:00'), 
(8, 3, '2024-02-20', 'Miércoles 09:00-11:00'), 
(9, 4, '2024-02-25', 'Jueves 15:00-17:00'), 
(10, 5, '2024-03-01', 'Viernes 11:00-13:00');

-- << SQL = Structured Query Language = Lenguaje de Consultas Estructurado >>

-- ---------- PARA OBTENER DATOS DE UNA BASE DE DATOS:

SELECT campo1, campo2,..., campoN FROM Tabla WHERE condición ORDER BY campo;

SELECT alumnoDNI, apellido, nombre, email FROM alumnos ;

-- ------- PARA TRAERSE TODOS LOS REGISTROS DE UNA BD:

SELECT * FROM Tabla

-- ----------  PARA AÑADIR CONDICIONES:

SELECT campo1, campo2,..., campoN FROM Tabla WHERE condición ORDER BY campo;


-- Buscar los registros cuyo campo nombre comience por la letra 'L':
SELECT * FROM alumnos WHERE nombre LIKE 'L%';


-- Buscar si el sistema NO es insensitive (insensible):
SELECT * FROM alumnos WHERE LOWER(nombre) LIKE 'l%';
SELECT * FROM alumnos WHERE UPPER(nombre) LIKE 'L%';

-- ---- BÚSQUEDAS CON ORDENAMIENTO

SELECT * FROM Products ORDER BY Price ASC | DESC;

SELECT * FROM alumnos ORDER BY apellido ASC;

-- ------- ACTUALIZACIÓN DE DATOS EN TABLAS 

UPDATE nombre_tabla 
   SET campo1 = valor1, 
       campo2 = valor2,
       campo3 = valor3,  
       ...
WHERE condición;

UPDATE alumnos 
   SET nombre = 'Francisco', 
       email = 'francisco@dominio.com'

WHERE alumnoDNI = '11111';

-- ----- BORRADO DE DATOS EN TABLAS 

DELETE FROM nombre_tabla WHERE condición;

DELETE FROM alumnos  WHERE alumnoDNI = '55555';
DELETE FROM alumnos  WHERE alumnoDNI = '77777'; -- OJO

-- ---------- ALTERAR LA ESTRUCTURA DE LA TABLA

ALTER TABLE nombre_tabla ADD nombre_de_campo tipo_de_datos;

ALTER TABLE alumnos ADD COLUMN direccion VARCHAR(255) NOT NULL AFTER fecha_nacimiento;



CREATE DATABASE IF NOT EXISTS empresa;
USE empresa;

CREATE TABLE IF NOT EXISTS datos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_empleado VARCHAR(20) NOT NULL UNIQUE,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    cargo VARCHAR(50) NOT NULL
);

-- Insertamos datos de prueba con cara y ojos
INSERT INTO datos (id_empleado, nombre, apellido, cargo) VALUES 
('EMP-001', 'Carlos', 'Mendoza', 'Desarrollador Backend'),
('EMP-002', 'Ana', 'Gómez', 'Diseñadora UX/UI'),
('EMP-003', 'Luis', 'Martínez', 'DevOps Engineer');
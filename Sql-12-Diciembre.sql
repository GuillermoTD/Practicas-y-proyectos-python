use Cheques

CREATE SCHEMA Guillermo


CREATE TABLE Guillermo.Puesto(
    ID_Puesto INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    Descripcion NVARCHAR(50) NOT NULL
);


CREATE TABLE Guillermo.Empleado(
    ID_Empleado INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    Nombre NVARCHAR(50) NOT NULL,
    Direccion NVARCHAR(50) NOT NULL,
    Telefono CHAR(15) NOT NULL,
    Cedula CHAR(15) NOT NULL,
    ID_Puesto INT NOT NULL,
	CONSTRAINT FK_empleado_puesto FOREIGN KEY (ID_Puesto) REFERENCES Guillermo.Puesto (ID_Puesto) 
	
)


CREATE TABLE Guillermo.Producto(
	ID_Producto INT IDENTITY(1,1) PRIMARY KEY,
	Nombre NVARCHAR(80)
)


CREATE TABLE Guillermo.Sucursal(
	ID_Sucursal INT IDENTITY(1,1) PRIMARY KEY,
	Nombre NVARCHAR(50),
	Direccion NVARCHAR(50),
	Telefono char(15),
	GerenteId INT,
	CONSTRAINT FK_gerente_empleado FOREIGN KEY (GerenteId) REFERENCES  Guillermo.Empleado(ID_Empleado)
)


CREATE TABLE Guillermo.Inventario(
    ID_Producto INT NOT NULL,
    ID_Sucursal INT NOT NULL,
    Cantidad INT NOT NULL,
	CONSTRAINT FK_inventario_producto FOREIGN KEY (ID_Producto) REFERENCES  Guillermo.Producto (ID_Producto),
	CONSTRAINT FK_inventario_sucursal FOREIGN KEY (ID_Sucursal) REFERENCES Guillermo.Sucursal (ID_Sucursal)
)

CREATE TABLE Guillermo.Cliente(
	ID_Cliente INT IDENTITY(1,1) PRIMARY KEY,
	Nombre NVARCHAR(50),
	Direccion NVARCHAR(50),
	Telefono char(15),
	Cedula char(15)
)

CREATE TABLE Guillermo.Fact_Header(
    Fecha_Fact DATE NOT NULL,
    ID_Cliente INT NOT NULL,
    ID_Sucursal INT NOT NULL,
    NO_Fact INT NOT NULL,	
	CONSTRAINT PK_factura_header PRIMARY KEY (Fecha_Fact,ID_Cliente,ID_Sucursal,NO_Fact),
	CONSTRAINT FK_factura_cliente FOREIGN KEY (ID_Cliente) REFERENCES  Guillermo.Cliente (ID_Cliente),
	CONSTRAINT FK_factura_sucursal FOREIGN KEY (ID_Sucursal) REFERENCES Guillermo.Sucursal (ID_Sucursal)
)	

CREATE TABLE Guillermo.Fact_Detail(
    Fecha_Fact DATE NOT NULL,  
    Cantidad INT NOT NULL,
    Precio INT NOT NULL,	
	NO_Fact INT NOT NULL,
)
-----------------PROCEDURES--------------------------
-------------------INSERTS----------------------------

CREATE PROCEDURE Guillermo.SP_INSERT_CLIENTES
	@ID_Cliente INT OUT,
	@Nombre NVARCHAR(50),
	@Direccion NVARCHAR(50),
	@Telefono char(15),
	@Cedula char(15)

AS 
BEGIN
	INSERT INTO Guillermo.Cliente(Nombre,Direccion,Telefono,Cedula)
							VALUES(@Nombre ,@Direccion ,@Telefono ,@Cedula)
END


CREATE PROCEDURE Guillermo.SP_INSERT_EMPLEADO
	@ID_EMPLEADO INT OUT,
	@Nombre NVARCHAR(50),
	@Direccion NVARCHAR(50),
	@Telefono CHAR(15),
	@Cedula CHAR(15),
	@ID_Puesto INT
AS 
BEGIN
	INSERT INTO Guillermo.Empleado(Nombre,Direccion, Telefono,  Cedula,  ID_Puesto)
							VALUES(@Nombre, @Direccion, @Telefono, @Cedula, @ID_Puesto)
END


CREATE PROCEDURE Guillermo.SP_INSERT_INVENTARIO
	@ID_Producto INT,
    @ID_Sucursal INT,
    @Cantidad INT

AS 
BEGIN
	INSERT INTO Guillermo.Inventario(ID_Sucursal,Cantidad)
							VALUES(@ID_Sucursal,@Cantidad)
END

CREATE PROCEDURE Guillermo.SP_INSERT_PRODUCTO
	@ID_Producto INT,
	@Nombre NVARCHAR(80)

AS 
BEGIN
	INSERT INTO Guillermo.Producto(ID_Producto,Nombre)
							VALUES(@ID_Producto,@Nombre)
END


CREATE PROCEDURE Guillermo.SP_INSERT_PUESTO
	@ID_Puesto INT,
	@Descripcion NVARCHAR

AS 
BEGIN
	INSERT INTO Guillermo.Puesto(ID_Puesto,Descripcion)
							VALUES(@ID_Puesto,@Descripcion)
END


CREATE PROCEDURE Guillermo.SP_INSERT_SUCURSAL
	@ID_Sucursal INT,
	@Nombre NVARCHAR(50),
	@Direccion NVARCHAR(50),
	@Telefono char(15),
	@GerenteId INT

AS 
BEGIN
	INSERT INTO Guillermo.Sucursal(Nombre,Direccion,Telefono,GerenteId)
							VALUES(@Nombre,@Direccion,@Telefono,@GerenteId)
END




CREATE PROCEDURE Guillermo.SP_INSERT_FACT_DETAIL
	@Fecha_Fact DATE,  
    @Cantidad INT,
    @Precio INT,	
	@NO_Fact INT

AS 
BEGIN
	INSERT INTO Guillermo.Fact_Detail(Fecha_Fact,Cantidad,Precio,NO_Fact)
							VALUES(@Fecha_Fact,@Cantidad,@Precio,@NO_Fact)
END

 

CREATE PROCEDURE Guillermo.SP_INSERT_FACT_HEADER
	@Fecha_Fact DATE,
    @ID_Cliente INT ,
    @ID_Sucursal INT ,
    @NO_Fact INT 

AS 
BEGIN
	INSERT INTO Guillermo.Fact_Header(Fecha_Fact,NO_Fact)
							VALUES(@Fecha_Fact,@NO_Fact)
END




----------------DELETES----------------------

CREATE PROCEDURE Guillermo.SP_DELETE_PRODUCTO
	@ID_Producto INT

AS 
BEGIN
	DELETE FROM Guillermo.Producto WHERE ID_Producto = @ID_Producto
END



CREATE PROCEDURE Guillermo.SP_DELETE_CLIENTE
	@ID_Cliente INT

AS 
BEGIN
	DELETE FROM Guillermo.Cliente WHERE ID_Cliente = @ID_Cliente
END


CREATE PROCEDURE Guillermo.SP_DELETE_EMPLEADO
	@ID_Empleado INT

AS 
BEGIN
	DELETE FROM Guillermo.Empleado WHERE ID_Empleado = @ID_Empleado
END



CREATE PROCEDURE Guillermo.SP_DELETE_PUESTO
	@ID_Puesto INT

AS 
BEGIN
	DELETE FROM Guillermo.Puesto WHERE ID_Puesto = @ID_Puesto
END


CREATE PROCEDURE Guillermo.SP_DELETE_INVENTARIO
	@ID_Inventario INT

AS 
BEGIN
	DELETE FROM Guillermo.Inventario WHERE ID_Inventario = @ID_Inventario
END


CREATE PROCEDURE Guillermo.SP_DELETE_FACT_HEADER
    @NO_Fact INT

AS 
BEGIN
	DELETE FROM Guillermo.Fact_Header WHERE NO_Fact = @NO_Fact
END


CREATE PROCEDURE Guillermo.SP_DELETE_FACT_DETAIL
    @NO_Fact INT

AS 
BEGIN
	DELETE FROM Guillermo.Fact_Detail WHERE NO_Fact = @NO_Fact
END


CREATE PROCEDURE Guillermo.SP_DELETE_SUCURSAL
    @ID_Sucursal INT

AS 
BEGIN
	DELETE FROM Guillermo.Sucursal WHERE @ID_Sucursal = @ID_Sucursal
END

----------------------UPDATES---------------------------


/*ALTER TABLE Guillermo.Inventario ADD ID_Inventario int identity(1,1)*/
EXECUTE Guillermo.SP_DELETE_PRODUCTO 1

select * from Guillermo.Producto


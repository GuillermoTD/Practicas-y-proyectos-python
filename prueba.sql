

USE Cheques

CREATE SCHEMA tapia

CREATE table tapia.guillermo
( EmployeeID int IDENTITY(1,1) PRIMARY KEY,
  FirstName nvarchar(50) NOT NULL,  
  LastName nvarchar(50) NOT NULL
);

ALTER TABLE tapia.guillermo ADD Identification char(11)
ALTER TABLE tapia.guillermo ADD Address varchar(500)

ALTER TABLE tapia.guillermo ADD CONSTRAINT create_date  DEFAULT GETDATE() FOR create_date
ALTER TABLE tapia.guillermo ADD CONSTRAINT  Identification  not null


ALTER TABLE tapia.guillermo ALTER COLUMN Identification char(11) NOT NULL 

insert into tapia.guillermo ( FirstName,LastName,Identification)
values ('Juana','Mendez',null)

select * from  tapia.guillermo 
  
update tapia.guillermo
  set Identification = (SELECT b.EmployeeID 
                          FROM tapia.guillermo AS b
					     WHERE b.EmployeeID = tapia.guillermo.EmployeeID)



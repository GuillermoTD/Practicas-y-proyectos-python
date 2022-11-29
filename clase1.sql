USE Cheques
CREATE table dbo.pedro
( EmployeeID int IDENTITY(1,1) PRIMARY KEY,
  FirstName nvarchar(50) NOT NULL,  
  LastName nvarchar(50) NOT NULL
);

ALTER TABLE dbo.pedro ADD Identification char(11)
ALTER TABLE dbo.pedro ADD Address varchar(500)

ALTER TABLE dbo.pedro ADD CONSTRAINT create_date  DEFAULT GETDATE() FOR create_date
ALTER TABLE dbo.pedro ADD CONSTRAINT  Identification  not null


ALTER TABLE dbo.pedro ALTER COLUMN Identification char(11) NOT NULL 

insert into dbo.pedro ( FirstName,LastName,Identification)
values ('Juana','Mendez',null)

select * from  dbo.pedro AS a
where  EmployeeID = 3
  
update dbo.pedro
  set Identification = (SELECT b.EmployeeID 
                          FROM dbo.pedro AS b
					     WHERE b.EmployeeID = dbo.pedro.EmployeeID)
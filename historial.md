1 try { . "c:\Users\Estudiante\AppData\Local\Programs\Microsoft VS Code\4fe60c8b1c\resources\app\out\...
   2 (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& c:\Users\Estudiante\Downloa...
   3 & c:/Users/Estudiante/Downloads/DatosPython/venv/Scripts/python.exe c:/Users/Estudiante/Downloads/D...
   4 docker build -t aplicacion .                                                                          
   5 docker run -d -p 3000:5000 --name pythonapp aplicacion                                                
   6 docker save -o mypython.tar aplicacion                                                                
   7 docker load mypython.tar                                                                              
   8 docker load -i mypython.tar                                                                           
   9 docker run -d -p 3000:5000 --name pythonapp aplicacion                                                
  10 docker pull mysql:8.0                                                                                 
  11 docker run -d --name mysqlserver -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=empresa -p 3306:3306 
  12 docker run -d --name mysqlserver -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=empresa -p 8080:3306 
  13 docker run -d --name mysqlserver -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=empresa -p 8080:33...
  14 docker exec mysqlserver mysqldump -u root -p123456 empresa > empresa.sql   
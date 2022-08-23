from multiprocessing import connection
import mysql.connector
from mysql.connector import errorcode

try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password=''
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `TEST2`;")

cursor.execute("CREATE DATABASE `TEST2`;")

cursor.execute("USE `TEST2`;")

cursor.execute("CREATE TABLE PAIS (ID int PRIMARY KEY AUTO_INCREMENT, NOME VARCHAR(255), SIGLA char(3));")

cursor.execute("CREATE TABLE ESTADO (ID int PRIMARY KEY AUTO_INCREMENT, NOME VARCHAR(255), SIGLA CHAR(2), ID_PAIS INT);")

cursor.execute("CREATE TABLE CIDADE (ID int PRIMARY KEY AUTO_INCREMENT, NOME VARCHAR(255), ID_ESTADO INT);")

cursor.execute("""INSERT INTO PAIS (NOME, SIGLA) VALUES ('BRASIL', 'BRA'), ('ESTADOS UNIDOS', 'EUA');""")

cursor.execute("""INSERT INTO ESTADO (NOME, SIGLA, ID_PAIS) VALUES 
('Acre', 'AC', 1),
('Alagoas', 'AL', 1),
('Amapa', 'AP', 1),
('Amazonas', 'AM', 1),
('Bahia', 'BA', 1),
('Ceara', 'CE', 1),
('Distrito Federal', 'DF', 1),
('Espirito Santo', 'ES', 1),
('Goias', 'GO', 1),
('Maranhao', 'MA', 1),
('Mato Grosso', 'MT', 1),
('Minas Gerais', 'MG', 1),
('Alasca', 'AK', 2),
('Alabama', 'AL', 2),
('Arkansas', 'AR', 2),
('Arizona', 'AZ', 2),
('California', 'CA', 2),
('Colorado', 'CO', 2),
('Connectcut', 'CT', 2),
('Delaware', 'DE', 2),
('Florida', 'FL', 2),
('Georgia', 'GA', 2),
('Havai', 'HI', 2),
('Iowa', 'IA', 2),
('Idaho', 'ID', 2),
('Ilinoes', 'IL', 2),
('Indiana', 'IN', 2);
""")


cursor.execute(""" INSERT INTO CIDADE (NOME, ID_ESTADO) VALUES 
('Rio Branco', 1),
('Cruzeiro do Sul', 1),
('Anadia', 2),
('Arapiraca', 2),
('Macapa', 3),
('Mazagao', 3),
('Anori', 4),
('Apui', 4),
('Salvador', 5),
('Camari', 5),
('Fortaleza', 6),
('Caucaia', 6),
('Brasilia', 7),
('Sobrandinho', 7),
('Cachoeira de Itapemirim', 8),
('Vitoria', 8),
('Barro Alto', 9),
('Caudazinha', 9),
('Brejo', 10),
('Codo', 10),
('Cuiaba', 11),
('Sorriso', 11),
('Belo Horizonte', 12),
('Uberlandia', 12),
('Homer', 13),
('Fairbanks', 13),
('Mobile', 14),
('Alburn', 14),
('Fort Smith', 15),
('Hot Springs', 15),
('Tucson', 16),
('Phoenix', 16),
('Los Angeles', 17),
('Sao Francisco', 17),
('Denver', 18),
('Colorado Springs', 18),
('New Haven', 19),
('Greenwich', 19),
('Dover', 20),
('Newark', 20),
('Miami', 21),
('Orlando', 21),
('Augusta', 22),
('Macon', 22),
('Hawi', 23),
('Volcano', 23),
('Des Moines', 24),
('Ames', 24),
('Boise City', 25),
('Idaho Falls', 25),
('Chicago', 26),
('Springs Fields', 26),
('Indianapolis', 27),
('Gary', 27);
""")

conn.commit()
cursor.close()
conn.close()

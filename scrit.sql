-- MySQL dump 10.13  Distrib 8.0.45, for Linux (x86_64)
--
-- Host: localhost    Database: stock_final
-- ------------------------------------------------------
-- Server version	8.0.45-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `inscription`
--

DROP TABLE IF EXISTS `inscription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inscription` (
  `id_inscription` int NOT NULL AUTO_INCREMENT,
  `nom_utilisateur` varchar(100) NOT NULL,
  `prenom_utilisateur` varchar(100) NOT NULL,
  `mot_de_passe` varchar(100) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_inscription`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inscription`
--

LOCK TABLES `inscription` WRITE;
/*!40000 ALTER TABLE `inscription` DISABLE KEYS */;
INSERT INTO `inscription` VALUES (1,'Binetou','Gueye','cbc29da1d7e4611f7bf89ad5239c742446accdc1873acf9594ccf30deb6fdc1a','binetouguey@gmail.com'),(2,'Gueye','Binetou','242d6021445109dda6f82c5029ad3c428af0d5d1af941799920e8984bc71c543','binetouguey@gmail.com'),(3,'Gueye','Sokhna','8b2747bb8d4eb43c88e81db8ba0a5cef23b524b3080a7910d114b1f1f27b6cb8','sokhnagueye@gmail.com'),(4,'Diop','Mamour','0340fb10681ff8e75dd95eec58494602063c9cc4cb5368576d8a495d281237b0','mamourdiop@gmail.com'),(5,'Drame','Fatoumata','42316eefca31554e2be46cedcbc2d237066dc11dfd8c5b6761ebc5cf228ac64c','fatoumatadrame@gmail.com'),(6,'niang','awa','90038ccc9b93431446629f67d7783a547d5cc68f2f8149d2c40ed003a57022c2','awaniang@gmail.com');
/*!40000 ALTER TABLE `inscription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produits`
--

DROP TABLE IF EXISTS `produits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produits` (
  `id` int NOT NULL AUTO_INCREMENT,
  `designation` varchar(100) NOT NULL,
  `categorie` varchar(50) NOT NULL,
  `quantite` int NOT NULL DEFAULT '0',
  `prix_unitaire` int DEFAULT NULL,
  `disponibilite` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produits`
--

LOCK TABLES `produits` WRITE;
/*!40000 ALTER TABLE `produits` DISABLE KEYS */;
INSERT INTO `produits` VALUES (1,'biscrem','biscuit',15,150,1),(2,'pressea ananas','Jus',3,1000,1),(3,'biscit bisco','Biscuit',10,50,1),(4,'Cake','Patisserie',15,100,1),(5,'Beurre jadida','Beurre',10,1000,1),(6,'Sucre moulu','Sucre',20,600,1),(7,'Sandale','Chaussure',5,500,1),(8,'Cafe stick ','Cafe',20,100,1),(13,'coco butter','lait de corps',2,100,1),(14,'nivea','lait de corps',10,2000,1),(16,'tablette chocolat','chocolat',11,2000,1);
/*!40000 ALTER TABLE `produits` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-12  8:55:06

-- phpMyAdmin SQL Dump
-- version 5.1.1-1.el7.remi
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 10, 2021 at 12:31 AM
-- Server version: 10.4.21-MariaDB-log
-- PHP Version: 7.4.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `BookWormDB`
--

-- --------------------------------------------------------

--
-- Table structure for table `authors`
--
CREATE TABLE `authors` (
  `author_id` int(11) NOT NULL,
  `author_first_name` varchar(45) NOT NULL,
  `author_last_name` varchar(45) NOT NULL,
  `book_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `authors`
--

INSERT INTO `authors` (`author_id`, `author_first_name`, `author_last_name`, `book_id`) VALUES
(1, 'Cormac', 'McCarthy', 1);

-- --------------------------------------------------------

--
-- Table structure for table `books`
--
CREATE TABLE `books` (
  `book_id` int(11) NOT NULL AUTO_INCREMENT,
  `book_name` varchar(255) NOT NULL,
  `book_pages` smallint(6) NOT NULL,
  `book_year` smallint(6) NOT NULL,
  `book_publisher` varchar(255) NOT NULL,
  `book_genre` varchar(255) NOT NULL,
  `book_author_fname` varchar(255) NOT NULL,
  `book_author_lname` varchar(255) NOT NULL,
  `rental_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`book_id`, `book_name`, `book_pages`, `book_year`, `book_publisher`, `book_genre`, `book_author_fname`, `book_author_lname`, `rental_id`) VALUES
(1, 'Blood Meridian', 337, 1985, 'Random House', 'Southern Gothic', 'Cormac', 'McCarthy', 1);

-- --------------------------------------------------------

--
-- Table structure for table `books_and_authors`
--
CREATE TABLE `books_and_authors` (
  `books_book_id` int(11) NOT NULL,
  `author_author_id` int(11) NOT NULL,
  PRIMARY KEY (books_book_id, author_author_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `books_and_authors`
--

INSERT INTO `books_and_authors` (`books_book_id`, `author_author_id`) VALUES
(1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `rentals`
--
CREATE TABLE `rentals` (
  `rental_id` int(11) NOT NULL AUTO_INCREMENT,
  `rental_date` varchar(255) NOT NULL,
  `rental_length` varchar(255) NOT NULL,
  `subscriber_id` int(11) NOT NULL,
  PRIMARY KEY (`rental_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `rentals`
--

INSERT INTO `rentals` (`rental_id`, `rental_date`, `rental_length`, `subscriber_id`) VALUES
(1, '2021-08-11', '14', 1);

-- --------------------------------------------------------

--
-- Table structure for table `subscribers`
--
CREATE TABLE `subscribers` (
  `subscriber_id` int(11) NOT NULL,
  `subscriber_first_name` varchar(255) NOT NULL,
  `subscriber_last_name` varchar(255) NOT NULL,
  `subscriber_address` varchar(255) NOT NULL,
  `subscriber_phone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `subscribers`
--

INSERT INTO `subscribers` (`subscriber_id`, `subscriber_first_name`, `subscriber_last_name`, `subscriber_address`, `subscriber_phone`) VALUES
(1, 'Example', 'Exampleton', '123 Washington St', 1234567890);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authors`
--
ALTER TABLE `authors`
  ADD PRIMARY KEY (`author_id`),
  ADD KEY `fk_book_id` (`book_id`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD KEY `fk_rental_id` (`rental_id`);

--
-- Indexes for table `books_and_authors`
--
ALTER TABLE `books_and_authors`
  ADD KEY `fk_books_book_id` (`books_book_id`),
  ADD KEY `fk_author_author_id` (`author_author_id`);

-- ALTER TABLE `books_and_authors`
-- ADD CONSTRAINT `bna_pk` PRIMARY KEY (books_book_id, author_author_id)

--
-- Indexes for table `rentals`
--
ALTER TABLE `rentals`
  ADD KEY `fk_subscriber_id` (`subscriber_id`);

--
-- Indexes for table `subscribers`
--
ALTER TABLE `subscribers`
  ADD PRIMARY KEY (`subscriber_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `authors`
--
ALTER TABLE `authors`
  MODIFY `author_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `subscribers`
--
ALTER TABLE `subscribers`
  MODIFY `subscriber_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `authors`
--
-- ALTER TABLE `authors`
--   ADD CONSTRAINT `fk_book_id` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `books`
--
ALTER TABLE `books`
  ADD CONSTRAINT `fk_rental_id` FOREIGN KEY (`rental_id`) REFERENCES `rentals` (`rental_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `books_and_authors`
--
ALTER TABLE `books_and_authors`
  ADD CONSTRAINT `fk_author_author_id` FOREIGN KEY (`author_author_id`) REFERENCES `authors` (`author_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_books_book_id` FOREIGN KEY (`books_book_id`) REFERENCES `books` (`book_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `rentals`
--
ALTER TABLE `rentals`
  ADD CONSTRAINT `fk_subscriber_id` FOREIGN KEY (`subscriber_id`) REFERENCES `subscribers` (`subscriber_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

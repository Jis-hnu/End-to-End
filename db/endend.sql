SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


-- Database: `endend`

CREATE DATABASE IF NOT EXISTS `endend` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `endend`;


-- Table structure for table `login`


CREATE TABLE IF NOT EXISTS `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_type` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;


-- Dumping data for table `login`


INSERT INTO `login` (`id`, `user_type`, `username`, `password`) VALUES
(1, 'Admin', 'admin@gmail.com', 'admin'),
(2, 'HR', 'vishak@gmail.com', 'vishak');


-- Table structure for table `tbl_amount`


CREATE TABLE IF NOT EXISTS `tbl_amount` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `vehiclename` varchar(50) NOT NULL,
  `amount` varchar(50) NOT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;


-- Table structure for table `tbl_card`


CREATE TABLE IF NOT EXISTS `tbl_card` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cnum` int(50) NOT NULL,
  `exdate` date NOT NULL,
  `cvv` int(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;



-- Table structure for table `tbl_category`


CREATE TABLE IF NOT EXISTS `tbl_category` (
  `catid` int(11) NOT NULL AUTO_INCREMENT,
  `catname` varchar(50) NOT NULL,
  PRIMARY KEY (`catid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `tbl_category`
--

INSERT INTO `tbl_category` (`catid`, `catname`) VALUES
(1, 'bus'),
(2, 'car'),
(3, 'torrus');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_driverreg`
--

CREATE TABLE IF NOT EXISTS `tbl_driverreg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_driver_request`
--

CREATE TABLE IF NOT EXISTS `tbl_driver_request` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `drid` int(50) NOT NULL,
  `vehid` int(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_feedback`
--

CREATE TABLE IF NOT EXISTS `tbl_feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `drivername` varchar(50) NOT NULL,
  `feedback` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `tbl_feedback`
--

INSERT INTO `tbl_feedback` (`id`, `drivername`, `feedback`) VALUES
(1, 'Akhil', 'Gud work'),
(2, 'Das', 'Gud work'),
(3, 'Ravikumar', 'Gudd');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_hrreg`
--

CREATE TABLE IF NOT EXISTS `tbl_hrreg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `tbl_hrreg`
--

INSERT INTO `tbl_hrreg` (`id`, `name`, `address`, `phone`, `email`, `password`) VALUES
(1, 'vishak', 'aluva', '9746658469', 'vishak@gmail.com', 'vishak');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_hr_request`
--

CREATE TABLE IF NOT EXISTS `tbl_hr_request` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hrid` int(50) NOT NULL,
  `vehid` int(50) NOT NULL,
  `reqdate` date NOT NULL,
  `retdate` date NOT NULL,
  `status` int(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `tbl_hr_request`
--

INSERT INTO `tbl_hr_request` (`id`, `hrid`, `vehid`, `reqdate`, `retdate`, `status`) VALUES
(1, 2, 1, '0000-00-00', '0000-00-00', 0);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_insurance`
--

CREATE TABLE IF NOT EXISTS `tbl_insurance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `regno` varchar(50) NOT NULL,
  `exdate` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `tbl_insurance`
--

INSERT INTO `tbl_insurance` (`id`, `regno`, `exdate`) VALUES
(1, '1', '2019-10-18');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_payment`
--

CREATE TABLE IF NOT EXISTS `tbl_payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `driverid` int(50) NOT NULL,
  `paydate` date NOT NULL,
  `status` varchar(50) NOT NULL,
  `tamnt` bigint(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_service`
--

CREATE TABLE IF NOT EXISTS `tbl_service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `regno` varchar(50) NOT NULL,
  `servicedate` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `tbl_service`
--

INSERT INTO `tbl_service` (`id`, `regno`, `servicedate`) VALUES
(1, '1', '2019-10-18');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_vehicle`
--

CREATE TABLE IF NOT EXISTS `tbl_vehicle` (
  `vehid` int(11) NOT NULL AUTO_INCREMENT,
  `catid` int(50) NOT NULL,
  `vehiclename` varchar(50) NOT NULL,
  `regno` varchar(50) NOT NULL,
  PRIMARY KEY (`vehid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `tbl_vehicle`
--

INSERT INTO `tbl_vehicle` (`vehid`, `catid`, `vehiclename`, `regno`) VALUES
(1, 2, 'maruthy', 'kl72323');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_work`
--

CREATE TABLE IF NOT EXISTS `tbl_work` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `did` int(50) NOT NULL,
  `work` varchar(50) NOT NULL,
  `wdate` date NOT NULL,
  `estimatedkm` int(50) NOT NULL,
  `estimateddays` int(50) NOT NULL,
  `wrkload` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `tbl_work`
--

INSERT INTO `tbl_work` (`id`, `did`, `work`, `wdate`, `estimatedkm`, `estimateddays`, `wrkload`, `status`) VALUES
(1, 3, 'loading', '2019-10-18', 3, 2, 'water', 'Alloted');

-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 07, 2024 at 12:03 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hipertensi`
--

-- --------------------------------------------------------

--
-- Table structure for table `detail`
--

CREATE TABLE `detail` (
  `id` int(11) NOT NULL,
  `grade_id` int(11) NOT NULL,
  `saran` text NOT NULL,
  `solusi` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `detail`
--

INSERT INTO `detail` (`id`, `grade_id`, `saran`, `solusi`) VALUES
(48, 1, 'Pertahankan pola makan sehat.', 'Teruskan konsumsi makanan sehat seperti buah-buahan dan sayuran.'),
(49, 1, 'Lakukan aktivitas fisik teratur.', 'Lakukan aktivitas fisik minimal 150 menit per minggu.'),
(50, 1, 'Pantau tekanan darah secara rutin.', 'Rutin memantau tekanan darah untuk memastikan tetap optimal.'),
(51, 1, 'Hindari stres.', 'Kelola stres dengan teknik relaksasi.'),
(52, 2, 'Pertahankan pola hidup sehat.', 'Lanjutkan pola makan sehat dan olahraga teratur.'),
(53, 2, 'Kurangi konsumsi garam.', 'Batasi konsumsi garam untuk menjaga tekanan darah.'),
(54, 2, 'Monitor tekanan darah secara berkala.', 'Lakukan pemeriksaan tekanan darah secara berkala.'),
(55, 2, 'Hindari rokok dan alkohol.', 'Kurangi atau hentikan konsumsi rokok dan alkohol.'),
(56, 3, 'Modifikasi pola makan.', 'Kurangi makanan tinggi lemak dan garam, tingkatkan asupan buah dan sayur.'),
(57, 3, 'Tingkatkan aktivitas fisik.', 'Tingkatkan intensitas dan frekuensi olahraga.'),
(58, 3, 'Kelola berat badan.', 'Usahakan mencapai berat badan ideal.'),
(59, 3, 'Relaksasi dan tidur cukup.', 'Pastikan tidur cukup dan kelola stres dengan baik.'),
(60, 4, 'Konsultasi medis.', 'Mulai berkonsultasi dengan dokter untuk penanganan lebih lanjut.'),
(61, 4, 'Ubah gaya hidup.', 'Implementasikan perubahan signifikan dalam gaya hidup.'),
(62, 4, 'Aktivitas fisik rutin.', 'Lakukan aktivitas fisik secara teratur dengan intensitas yang sesuai.'),
(63, 4, 'Pengurangan stres.', 'Gunakan teknik relaksasi untuk membantu menurunkan tekanan darah.'),
(64, 5, 'Pengobatan.', 'Terima pengobatan sesuai anjuran dokter.'),
(65, 5, 'Monitoring ketat.', 'Pantau tekanan darah secara teratur dan catat hasilnya.'),
(66, 5, 'Perubahan gaya hidup.', 'Terapkan perubahan gaya hidup termasuk diet dan olahraga.'),
(67, 5, 'Konseling dan edukasi.', 'Ikuti program konseling untuk memahami dan mengelola hipertensi.'),
(68, 6, 'Perawatan medis segera.', 'Segera temui dokter atau pergi ke rumah sakit untuk perawatan medis mendesak.'),
(69, 6, 'Pengobatan intensif.', 'Ikuti semua instruksi pengobatan yang diberikan dokter.'),
(70, 6, 'Pola hidup ketat.', 'Terapkan diet ketat rendah garam dan tinggi serat.'),
(71, 6, 'Pemantauan teratur.', 'Pantau tekanan darah secara ketat dan laporkan perubahan kepada dokter.'),
(72, 7, 'Konsultasi dokter.', 'Diskusikan strategi pengelolaan dengan dokter.'),
(73, 7, 'Perubahan diet.', 'Fokus pada diet rendah garam dan tinggi serat.'),
(74, 7, 'Lakukan aktivitas fisik.', 'Lakukan aktivitas fisik teratur dengan pengawasan dokter jika diperlukan.'),
(75, 7, 'Kelola faktor risiko.', 'Identifikasi dan kelola faktor risiko lain seperti diabetes dan obesitas.');

-- --------------------------------------------------------

--
-- Table structure for table `grade`
--

CREATE TABLE `grade` (
  `id` int(11) NOT NULL,
  `cgrade` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `grade`
--

INSERT INTO `grade` (`id`, `cgrade`) VALUES
(1, 'Optimal'),
(2, 'Normal'),
(3, 'High_normal'),
(4, 'Grade_1'),
(5, 'Grade_2'),
(6, 'Grade_3'),
(7, 'Isolated_systemic_hypertension');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `detail`
--
ALTER TABLE `detail`
  ADD PRIMARY KEY (`id`),
  ADD KEY `grade_id` (`grade_id`);

--
-- Indexes for table `grade`
--
ALTER TABLE `grade`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `detail`
--
ALTER TABLE `detail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=76;

--
-- AUTO_INCREMENT for table `grade`
--
ALTER TABLE `grade`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `detail`
--
ALTER TABLE `detail`
  ADD CONSTRAINT `detail_ibfk_1` FOREIGN KEY (`grade_id`) REFERENCES `grade` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

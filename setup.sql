-- إنشاء قاعدة البيانات
CREATE DATABASE IF NOT EXISTS dark_db;
USE dark_db;

-- إنشاء جدول المستخدمين (المستهدف)
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    secret_note VARCHAR(255),
    privilege_level VARCHAR(20)
);

-- زرع البيانات (هذه التي سنستخرجها بـ Sqlmap)
INSERT INTO users (username, password, email, secret_note, privilege_level) VALUES 
('admin_root', 'Dark_Master_2026_!!', 'admin@shadow.net', 'مفتاح الدخول للسيرفر هو: SH-990', 'SUPER_ADMIN'),
('larbi_dev', 'Chakour_Safe_82', 'moh216784@gmail.com', 'بوت التداول جاهز في المجلد السري', 'DEVELOPER'),
('finance_mgr', 'Money_Maker_$$$', 'finance@target.com', 'الرصيد المتاح هو 10,000$', 'MANAGER'),
('test_user', '123456', 'test@test.com', 'مجرد حساب تجريبي', 'USER');


<?php
// إعدادات الاتصال (ستحتاج لتغييرها عند رفعه على استضافة حقيقية)
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "dark_db";

// إنشاء الاتصال
$conn = new mysqli($servername, $username, $password, $dbname);

// التحقق من الاتصال
if ($conn->connect_error) {
    die("فشل الاتصال: " . $conn->connect_error);
}

// الثغرة القاتلة: استقبال المعرف دون أي حماية
$id = $_GET['id'];
$sql = "SELECT username, email, password FROM users WHERE id = $id";

$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo "<div style='color:#00ff00; background:#000; padding:10px; border:1px solid #00ff00;'>";
        echo "👤 المستخدم: " . $row["username"]. " - 📧 البريد: " . $row["email"]. "<br>";
        echo "</div>";
    }
} else {
    echo "<p style='color:red;'>لا يوجد نتائج لهذا المعرف.</p>";
}
$conn->close();
?>


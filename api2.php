<?php
$conn = mysqli_connect("localhost", "root", "", "test_db");
$status = 'OK';
$content = [];
$id = $_GET['id'];
if (mysqli_connect_errno()) {
    $status = 'ERROR';
    $content = mysqli_connect_error();
}
$query = "SELECT * FROM table1 where id = '$id'";

if ($result = mysqli_query($conn, $query)) {
    while ($row = mysqli_fetch_assoc($result)) {
        $content[] = $row;
    }
}
$data = ["status" => $status, "content" => $content];

header('Content-type: application/json');
echo json_encode($data);
?>
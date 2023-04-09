<?php
$conn = mysqli_connect("localhost", "root", "", "jobfid");
$status = 'OK';
$content = [];
if (mysqli_connect_errno()) {
    $status = 'ERROR';
    $content = mysqli_connect_error();
}
$query = "SELECT * FROM users";

if ($result = mysqli_query($conn, $query)) {
    while ($row = mysqli_fetch_assoc($result)) {
        $content[] = $row;
    }
}
$data = ["status" => $status, "content" => $content];

header('Content-type: application/json');
echo json_encode($data);
?>
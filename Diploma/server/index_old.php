<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>Тег TABLE</title>
 </head>
 <body>
 
  <table border="1" width="100%" cellpadding="2">
   <tr>
    <th>Unique ID</th>
    <th>UserName</th>
    <th>Download</th>
   </tr>
   <tr>
   <?php
  $host = 'localhost';  // Хост
  $user = 'root';    // Имя  пользователя
  $pass = ''; //  вами пароль пользователю
  $db_name = 'db_diplom';   // Имя базы данных
  $link = mysqli_connect($host, $user, $pass, $db_name); // Соединяемся с базой
  $sql = mysqli_query($link, 'SELECT * FROM `output_infos`');
  while ($result = mysqli_fetch_array($sql)) {
    echo "<tr><td>{$result['unique_id']}</td><td>{$result['User']}</td><td><a href='http://192.168.1.2/upload/{$result['unique_id']}.zip'>Download</a></td></tr>";
  }
  if (!$link) {
    echo 'Не могу соединиться с БД. Код ошибки: ' . mysqli_connect_errno() . ', ошибка: ' . mysqli_connect_error();
    exit;
  }
?>
  </tr>
 </table>
 </body>
</html>
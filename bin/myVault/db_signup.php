<?php 

define('DB_HOST', '127.0.0.1'); 
define('DB_NAME', 'myvault'); 
define('DB_USER','root'); 
define('DB_PASSWORD',''); 

$con=mysql_connect(DB_HOST,DB_USER,DB_PASSWORD) or die("Failed to connect to MySQL: " . mysql_error()); 
$db=mysql_select_db(DB_NAME,$con) or die("Failed to connect to MySQL : " . mysql_error()); 

function NewUser() 
	{  
		$fname = $_POST['fname']; 
		$lname = $_POST['lname']; 
		$username = $_POST['username']; 
		$password = $_POST['password']; 
					
		$query = "INSERT INTO login (fname,lname,username,password) VALUES ('$fname','$lname','$username','$password')"; 
		$data = mysql_query ($query)or die(mysql_error()); 
			
			if($data) 
				{ 
					header("location: index.php");
				}
				
	} 
function SignUp() 
	{ 
		if(!empty($_POST['username']))
		{ 
			$query = mysql_query("SELECT * FROM login WHERE username = '$_POST[username]' AND password = '$_POST[password]'") or die(mysql_error()); 
			if(!$row = mysql_fetch_array($query) or die(mysql_error())) 
				{ 
					NewUser(); 
				} 
		else 
			{ 
				header("location: index.php");
			} 
		} 
	} 
if(isset($_POST['signup'])) 
	{   
		SignUp(); 
	} 
?>
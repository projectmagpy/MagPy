<?php
session_start();
$a=$_POST["shname"];
$u=$_POST["url"];
$username=$_SESSION['login_user'];
$arr2 = str_split($u, 7);
$key=$arr2[0];


if ($key=="http://" || $key=="https:/")
{
	if (file_exists($username))
	{
		chdir($username);
		if (file_exists($a)) 
			{
					echo "<!DOCTYPE html>
					<html>
					<head>
					<meta charset=".'"UTF-8"'.">".'<meta http-equiv="refresh"'.' content="3;url=http://127.0.0.1/tiny" />'."
					<title>#Short.Me || Simplifying life !</title>
					<link href='http://fonts.googleapis.com/css?family=Titillium+Web:400,300,600' rel='stylesheet' type='text/css'>
					<link rel=".'"stylesheet"'. 'href="css/normalize.css">
					<link rel="stylesheet" href="css/style.css" media="screen" type="text/css" />
					</head>
					<body>'."<br><br><br><br><br><br><br><br><br><br><h1>Please choose other short link.<br> This short link <a href="."http://127.0.0.1/tiny/".$a.">http://127.0.0.1/tiny/".$a."</a> already exists. </h1>".
					"<script src='http://codepen.io/assets/libs/fullpage/jquery.js'></script>".
					'<script src="js/index.js"></script>
					</body>'.
					"</html>";
			} 
		else 
			{
					mkdir($a);
					
					$mylinks = fopen("links.txt", "w") or die("Unable to open file!");
					$links=$u;
					fwrite($mylinks, $links);
					fclose($mylinks);
					chdir($a);
					$myfile = fopen("index.html", "w") or die("Unable to open file!");
					$txt = "<html>
							<head>
							<meta http-equiv=".'"refresh"'.'content="0; url='.$u.'"'." />
							</head>
							</html>";
					fwrite($myfile, $txt);
					fclose($myfile);
					echo "<!DOCTYPE html>
							<html>
							<head>
							<meta charset=".'"UTF-8"'.">
							<title>#Short.Me || Simplifying life !</title>
							<link href='http://fonts.googleapis.com/css?family=Titillium+Web:400,300,600' rel='stylesheet' type='text/css'>
							<link rel=".'"stylesheet"'. 'href="css/normalize.css">
							<link rel="stylesheet" href="css/style.css" media="screen" type="text/css" />
							</head>
							<body>'."<br><br><br><br><br><br><br><br><br><br><h1>Your Shortened url ! <br><a href="."http://127.0.0.1/tiny/".$a.">http://127.0.0.1/tiny/".$a."</a></h1>".
							'<h1><a href="shortme.php">[<< Add new]</a>
							<a href="logout.php">[Exit ! >>]</a></h1>
							"<script src='."'http://codepen.io/assets/libs/fullpage/jquery.js'></script>".
							'<script src="js/index.js"></script>
							</body>'.
							"</html>";

			}

	
	}
	else
	{
	mkdir($username);
	chdir($username);
	
	if (file_exists($a)) 
		{
			echo "<!DOCTYPE html>
				<html>
				<head>
				<meta charset=".'"UTF-8"'.">".'<meta http-equiv="refresh"'.' content="3;url=http://127.0.0.1/tiny" />'."
				<title>#Short.Me || Simplifying life !</title>
				<link href='http://fonts.googleapis.com/css?family=Titillium+Web:400,300,600' rel='stylesheet' type='text/css'>
				<link rel=".'"stylesheet"'. 'href="css/normalize.css">
				<link rel="stylesheet" href="css/style.css" media="screen" type="text/css" />
				</head>
				<body>'."<br><br><br><br><br><br><br><br><br><br><h1>Please choose other short link.<br> This short link <a href="."http://127.0.0.1/tiny/".$a.">http://127.0.0.1/tiny/".$a."</a> already exists. </h1>".
				"<script src='http://codepen.io/assets/libs/fullpage/jquery.js'></script>".
				'<script src="js/index.js"></script>
				</body>'.
				"</html>";
		} 
	else 
		{
			mkdir($a);
			$mylinks = fopen("links.txt", "w") or die("Unable to open file!");
			$links=$u;
			fwrite($mylinks, $links);
			fclose($mylinks);
			chdir($a);
			$myfile = fopen("index.html", "w") or die("Unable to open file!");
			$txt = "<html>
					<head>
					<meta http-equiv=".'"refresh"'.'content="0; url='.$u.'"'." />
					</head>
					</html>";
					fwrite($myfile, $txt);
					fclose($myfile);
					echo "<!DOCTYPE html>
					<html>
					<head>
					<meta charset=".'"UTF-8"'.">
					<title>#Short.Me || Simplifying life !</title>
					<link href='http://fonts.googleapis.com/css?family=Titillium+Web:400,300,600' rel='stylesheet' type='text/css'>
					<link rel=".'"stylesheet"'. 'href="css/normalize.css">
					<link rel="stylesheet" href="css/style.css" media="screen" type="text/css" />
					</head>
					<body>'."<br><br><br><br><br><br><br><br><br><br><h1>Your Shortened url ! <br><a href="."http://127.0.0.1/tiny/".$a.">http://127.0.0.1/tiny/".$a."</a></h1>".
					'<h1><a href="shortme.php">[<< Add new]</a>
					<a href="logout.php">[Exit ! >>]</a></h1>
					"<script src='."'http://codepen.io/assets/libs/fullpage/jquery.js'></script>".
					'<script src="js/index.js"></script>
					</body>'.
					"</html>";
		}
	}

}
else
{
	echo "<!DOCTYPE html>
	<html>
	<head>
	<meta charset=".'"UTF-8"><meta http-equiv="refresh" content="3;url=http://127.0.0.1/tiny" />
	<title>#Short.Me || Simplifying life !</title>
	<link href='."'http://fonts.googleapis.com/css?family=Titillium+Web:400,300,600' rel='stylesheet' type='text/css'>
	<link rel=".'"stylesheet"href="css/normalize.css">
    <link rel="stylesheet" href="css/style.css" media="screen" type="text/css" />
	</head>
	<body><br><br><br><br><br><br><br><br><br><br><br><h1>Sorry ! There is an error in your link<br> please copy the exact link from the tab<br> PS : check whether the link is preceeding with "http://" or "https://"</h1><script src='."'http://codepen.io/assets/libs/fullpage/jquery.js'></script><script".' src="js/index.js"></script>
	</body>'."</html>";
}

?>











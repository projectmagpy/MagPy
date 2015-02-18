<?php
include('session.php');
echo "<!DOCTYPE html>
<html>

<head>

  <meta charset=".'"UTF-8">

  <title>#Short.Me || Simplifying life !</title>

  <link href='."'http://fonts.googleapis.com/css?family=Titillium+Web:400,300,600' rel='stylesheet' type='text/css'>

  <link rel=".'"stylesheet" href="css/normalize.css">

    <link rel="stylesheet" href="css/style.css" media="screen" type="text/css" />

</head>

<body>
<br><br>
  <div class="form">

      <div class="tab-content">
        <div id="signup">   
		
          <h1>#Short.Me</h1>

          <form action="tiny.php" method="post">
          <div class="field-wrap">
            <label>
              link to shorten:<span class="req">*</span>
            </label>
            <input type="text"required autocomplete="off" name="url"/>
          </div>

          <div class="field-wrap">
            <label>
             http://paulii.tk/tiny/:<span class="req">*</span>
            </label>
            <input type="text"required autocomplete="off" name="shname"/>
          </div>

          <button type="submit" class="button button-block"/>Get Started</button>

          </form>

        </div>

        <div id="login">   
         
        </div>

      </div><!-- tab-content -->

</div> <!-- /form -->

  <script src='."'http://codepen.io/assets/libs/fullpage/jquery.js'></script>

  <script src=".'"js/index.js"></script>

</body>

</html>';
?>
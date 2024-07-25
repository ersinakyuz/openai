<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ask me</title>
    <!-- Favicon Link -->
    <link rel="icon" href="/favicon.ico" type="image/x-icon">
    <!-- Alternatif Favicon Link -->
    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
    <!-- Apple Touch Icon -->
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">

    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <form action="ai.php" method="post">
        <label for="user_input">Enter your question:</label><br>
        <textarea id="user_input" name="user_input" ></textarea><br>
        <input type="submit" value="Submit">
    </form>

    <?php
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $user_input = $_POST['user_input'];
        
        // Send request to the Python backend
        $url = 'http://127.0.0.1:5000/process';
        $data = array('user_input' => $user_input);
        $options = array(
            'http' => array(
                'header'  => "Content-type: application/json\r\n",
                'method'  => 'POST',
                'content' => json_encode($data),
            ),
        );
        $context  = stream_context_create($options);
        $result = file_get_contents($url, false, $context);
        
        if ($result === FALSE) {
            echo '<p>Error</p>';
        } else {
            $response = json_decode($result, true);
            $formatted_response = nl2br(htmlspecialchars($response['result']));
            echo '<div class="response">';
	    echo '<p>' . $formatted_response . '</p>';
	    echo '</div>';
	}
    }
    ?>
</body>
</html>


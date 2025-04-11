

<!-- 
  This is the main entry point for the Svelte frontend application.
  The frontend development server usually runs on http://localhost:5173.
  The code below fetches data from the backend API and displays it.
-->

<script>
  // Declare a variable to store the message received from the backend.
  let message;

  /**
   * Send a GET request to the backend API using the built-in fetch() function.
   * The fetch() function is a native web API that allows us to make HTTP requests.
   * Here, it sends a GET request to 'http://127.0.0.1:8000/hello', which is the endpoint
   * we set up in our FastAPI backend.
   * fetch() returns a Promise that resolves to the response of the request.
  */
  fetch("http://127.0.0.1:8000/hello")
    .then((response) => {
    response.json().then((json) => {
      message = json.message;
    });
  });
</script>
 

<!--
  Render the message inside an h1 element on the web page.
  Initially, 'message' is undefined, but once the API call is successful,
  the greeting message returned from the backend will be displayed here.
-->
<h1>message: {message}</h1>
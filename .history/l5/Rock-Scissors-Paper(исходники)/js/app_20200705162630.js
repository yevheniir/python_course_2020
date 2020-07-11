function user_choice(choice){
    const Http = new XMLHttpRequest();
    Http.setRequestHeader('Content-Type', 'application/j');
    const url='http://localhost:5000/rps/' + choice;
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
        console.log("Response: " + Http.responseText)
      }
}